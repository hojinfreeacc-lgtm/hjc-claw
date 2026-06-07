import sys
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# 플러그인 로드 (임포트하는 것만으로 registry에 등록됨)
from .plugins import file_plugin
from .core.decision import DecisionEngine
from .core.executor import Executor
from .utils.memory import Memory

console = Console()

def main():
    console.print(Panel.fit(
        "[bold cyan]HJC CLAW[/bold cyan]\n[dim]Local Automation Agent (No-LLM)[/dim]",
        border_style="cyan"
    ))

    engine = DecisionEngine()
    memory = Memory()
    executor = Executor(memory=memory)

    while True:
        try:
            user_input = Prompt.ask("\n[bold green]>>>[/bold green]")
            
            if user_input.lower() in ["exit", "quit", "종료"]:
                console.print("[yellow]Goodbye![/yellow]")
                break

            # 1. 분석
            analysis = engine.analyze(user_input)
            
            # 2. 분석 정보 표시 (디버그용/투명성)
            console.print(f"[dim]인식: {analysis['intent']} (신뢰도: {analysis['confidence']*100}%)[/dim]")

            # 3. 실행
            result = executor.execute(analysis)
            
            # 4. 결과 출력
            console.print(Panel(result, title="[bold green]Result[/bold green]", border_style="green"))

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted by user. Type 'exit' to quit.[/yellow]")
        except Exception as e:
            console.print(f"[bold red]Error:[/] {str(e)}")

if __name__ == "__main__":
    main()
