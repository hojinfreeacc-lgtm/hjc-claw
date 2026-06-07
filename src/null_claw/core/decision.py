"""
core/decision.py — 의도 결정 엔진
================================
키워드 가중치, 퍼지 매칭, 정규표현식을 결합하여 최적의 의도를 판별합니다.
"""

import re
import difflib
from typing import Dict, Any, List, Tuple
from .registry import registry

class DecisionEngine:
    def __init__(self):
        self.registry = registry

    def analyze(self, text: str) -> Dict[str, Any]:
        """사용자 입력을 분석하여 최적의 의도와 파라미터를 반환합니다."""
        normalized = text.lower().strip()
        intents = self.registry.get_all_intents()
        
        scores = []
        for intent_name, info in intents.items():
            score = self._calculate_score(normalized, info["keywords"])
            if score > 0:
                scores.append((score, intent_name, info))

        # 가장 높은 점수의 의도 선택
        if not scores:
            return self._unknown(text)

        scores.sort(key=lambda x: x[0], reverse=True)
        best_score, best_intent, best_info = scores[0]

        # 파라미터 추출 (간소화된 버전, 실제로는 더 복잡한 로직 가능)
        params = self._extract_params(text, best_intent)

        return {
            "intent": best_intent,
            "plugin": best_info["plugin"],
            "action": best_info["action"],
            "params": params,
            "confidence": round(best_score, 2),
            "dangerous": best_info["dangerous"],
            "raw": text
        }

    def _calculate_score(self, text: str, keywords: List[str]) -> float:
        """정확 매칭과 퍼지 매칭의 가중치 합산을 계산합니다."""
        max_score = 0.0
        for kw in keywords:
            kw = kw.lower()
            # 1. 정확 포함 매칭 (가장 높은 가중치)
            if kw in text:
                score = 0.8 + (len(kw) / 100) # 긴 키워드 우선
                max_score = max(max_score, score)
            
            # 2. 퍼지 매칭 (부분 일치)
            words = text.split()
            for word in words:
                if len(word) < 2: continue
                ratio = difflib.SequenceMatcher(None, word, kw).ratio()
                if ratio > 0.7:
                    score = ratio * 0.7
                    max_score = max(max_score, score)
        
        return max_score

    def _extract_params(self, text: str, intent: str) -> Dict[str, Any]:
        """정규표현식을 이용한 파라미터 추출."""
        params = {}
        
        # 경로 추출 (따옴표 안 또는 일반적인 경로 패턴)
        paths = re.findall(r'[\'"]([^\'"]+)[\'"]|(/[a-zA-Z0-9._/-]+)|([a-zA-Z]:\\[a-zA-Z0-9._\\-]+)', text)
        extracted_paths = [p[0] or p[1] or p[2] for p in paths]
        if extracted_paths:
            params["paths"] = extracted_paths

        # URL 추출
        urls = re.findall(r'https?://[^\s]+', text)
        if urls:
            params["url"] = urls[0]

        # 확장자 추출
        exts = re.findall(r'\.([a-zA-Z0-9]+)', text)
        if exts:
            params["extension"] = exts[0]

        return params

    def _unknown(self, raw: str) -> Dict[str, Any]:
        return {
            "intent": "unknown",
            "plugin": None,
            "action": None,
            "params": {},
            "confidence": 0.0,
            "dangerous": False,
            "raw": raw
        }
