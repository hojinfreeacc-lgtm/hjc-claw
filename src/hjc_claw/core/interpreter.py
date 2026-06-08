"""
core/interpreter.py — 동적 코드 실행기
====================================
사용자의 복잡한 명령을 파이썬 코드로 변환(Rule-based)하여 즉석에서 실행합니다.
"""

import sys
import io
import traceback
from typing import Dict, Any
from rich.console import Console
from rich.syntax import Syntax
from .ai_brain import AIBrain

console = Console()

class CodeInterpreter:
    def __init__(self):
        self.globals = {}
        self.ai = AIBrain()
        # 기본적으로 유용한 라이브러리 미리 임포트
        exec("import os, sys, shutil, datetime, math, re, pathlib", self.globals)

    def execute_code(self, code: str) -> Dict[str, Any]:
        """파이썬 코드를 실행하고 출력과 에러를 캡처합니다."""
        stdout = io.StringIO()
        stderr = io.StringIO()
        
        # 실행 전 코드 출력 (투명성)
        console.print("\n[bold blue]🛠 동적 코드 실행 중...[/bold blue]")
        console.print(Syntax(code, "python", theme="monokai", line_numbers=True))

        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = stdout
        sys.stderr = stderr

        success = True
        try:
            exec(code, self.globals)
        except Exception:
            success = False
            traceback.print_exc()
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

        output = stdout.getvalue()
        error = stderr.getvalue()

        return {
            "success": success,
            "output": output if output else "코드 실행 완료 (출력 없음)",
            "error": error
        }

    def generate_code_from_intent(self, intent: str, params: Dict[str, Any], raw_text: str = "") -> str:
        """분석된 의도와 파라미터를 바탕으로 실행 가능한 코드를 생성합니다."""
        # 1. 규칙 기반 템플릿 (빠름)
        if intent == "file_search_complex":
            ext = params.get("extension", "*")
            return f"import pathlib\nfor p in pathlib.Path('.').rglob('*.{ext}'): print(f'Found: {{p}}')"
        
        # 2. AI 기반 코드 생성 (Manus 스타일)
        if self.ai.api_key or self.ai.use_ollama:
            return self.ai.generate_code(raw_text)
            
        return ""
