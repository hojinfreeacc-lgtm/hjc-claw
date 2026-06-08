"""
core/ai_brain.py — AI 추론 엔진
==============================
OpenAI 또는 로컬 Ollama를 사용하여 텍스트 분석, 코드 생성, 요약을 수행합니다.
"""

import os
import json
import requests
from typing import Dict, Any, Optional

class AIBrain:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
        self.model = os.getenv("HJC_AI_MODEL", "gpt-4o")
        self.use_ollama = os.getenv("HJC_USE_OLLAMA", "false").lower() == "true"
        self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")

    def ask(self, prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
        """LLM에게 질문하고 답변을 받습니다."""
        if self.use_ollama:
            return self._ask_ollama(prompt, system_prompt)
        return self._ask_openai(prompt, system_prompt)

    def generate_code(self, task: str) -> str:
        """작업 설명을 바탕으로 실행 가능한 파이썬 코드를 생성합니다."""
        prompt = f"Write a clean, executable Python script for the following task: {task}. Return ONLY the code without any explanation or markdown backticks."
        system_prompt = "You are an expert Python automation engineer. Output raw code only."
        code = self.ask(prompt, system_prompt)
        # 마크다운 백틱 제거 로직
        code = code.replace("```python", "").replace("```", "").strip()
        return code

    def _ask_openai(self, prompt: str, system_prompt: str) -> str:
        if not self.api_key:
            return "Error: OPENAI_API_KEY not found. Please set it in your environment."
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.2
        }
        try:
            response = requests.post(f"{self.base_url}/chat/completions", headers=headers, json=data)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            return f"AI Error (OpenAI): {str(e)}"

    def _ask_ollama(self, prompt: str, system_prompt: str) -> str:
        data = {
            "model": "llama3",
            "prompt": f"System: {system_prompt}\nUser: {prompt}",
            "stream": False
        }
        try:
            response = requests.post(self.ollama_url, json=data)
            response.raise_for_status()
            return response.json()["response"]
        except Exception as e:
            return f"AI Error (Ollama): {str(e)}"
