import sys
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# 플러그인 로드 (임포트하는 것만으로 registry에 등록됨)
from .plugins import file_plugin, security_plugin, mole_plugin, ai_web_plugin
from .core.decision import DecisionEngine
from .core.executor import Executor
from .utils.memory import Memory

console = Console()

from rich.status import Status
from rich.table import Table
from rich.live import Live

def main():
    # API 키 체크 안내
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("HJC_USE_OLLAMA"):
        console.print("[yellow]💡 Tip: Set OPENAI_API_KEY to unlock full AI capabilities (Manus-style).[/yellow]")

    console.print(Panel(
        "[bold cyan]HJC CLAW v1.1.0 (AI Edition)[/bold cyan]\n"
        "[dim]The Ultimate Hybrid AI Automation & Security Agent[/dim]\n"
        "[blue]Integrated: AI Brain + Open Claw + Null Claw + Security[/blue]",
        title="[bold white]System Ready[/bold white]",
        border_style="cyan",
        padding=(1, 2)
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

            with Status("[bold yellow]Analyzing intent...[/bold yellow]", spinner="dots") as status:
                # 1. 분석
                analysis = engine.analyze(user_input)
                status.update(f"[bold blue]Executing: {analysis['intent']}[/bold blue]")

                # 2. 실행
                result = executor.execute(analysis)
            
            # 3. 결과 출력
            console.print(Panel(result, title=f"[bold green]✓ {analysis['intent']} Result[/bold green]", border_style="green"))

        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted by user. Type 'exit' to quit.[/yellow]")
        except Exception as e:
            console.print(f"[bold red]Error:[/] {str(e)}")

if __name__ == "__main__":
    main()
