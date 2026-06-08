"""
core/executor.py — 실행 엔진
==========================
판별된 의도에 따라 플러그인 메서드를 호출하고 결과를 처리합니다.
"""

import sys
from rich.console import Console
from rich.panel import Panel
from typing import Dict, Any
from .registry import registry
from .interpreter import CodeInterpreter
from .ai_brain import AIBrain

console = Console()

class Executor:
    def __init__(self, memory=None):
        self.registry = registry
        self.memory = memory
        self.interpreter = CodeInterpreter()
        self.ai = AIBrain()

    def execute(self, analysis: Dict[str, Any]) -> str:
        """분석된 명령을 실행합니다."""
        if analysis["intent"] == "unknown":
            return "명령을 이해하지 못했습니다. '도움말'을 입력해 보세요."

        # 가드레일: 위험 명령 확인
        if analysis["dangerous"]:
            console.print(f"\n[bold red]⚠ 위험한 명령이 감지되었습니다: {analysis['intent']}[/]")
            confirm = input("   정말로 실행하시겠습니까? (y/N): ").lower()
            if confirm != 'y':
                return "실행이 취소되었습니다."

        plugin_name = analysis["plugin"]
        action_name = analysis["action"]
        params = analysis["params"]

        plugin_instance = self.registry.get_plugin(plugin_name)
        if not plugin_instance:
            return f"오류: 플러그인 '{plugin_name}'을 찾을 수 없습니다."

        try:
            # 1. AI 전용 작업 (Manus 스타일)
            if analysis.get("use_ai") and analysis["intent"] == "ai_task":
                return self.ai.ask(analysis["params"]["query"])

            # 2. 특수 의도: 동적 코드 실행 (Open Claw 스타일)
            if analysis.get("use_interpreter"):
                code = self.interpreter.generate_code_from_intent(analysis["intent"], params, analysis["raw"])
                if code:
                    res = self.interpreter.execute_code(code)
                    result = res["output"] if res["success"] else f"Error: {res['error']}"
                else:
                    result = "Error: Could not generate code for this intent."
            else:
                # 3. 일반 플러그인 실행 (Null Claw 스타일)
                method = getattr(plugin_instance, action_name)
                result = method(**params)
            
            # 메모리 기록
            if self.memory:
                self.memory.save(analysis, "success", str(result))
                
            return result
        except Exception as e:
            error_msg = f"실행 중 오류 발생: {str(e)}"
            if self.memory:
                self.memory.save(analysis, "failure", error_msg)
            return error_msg
