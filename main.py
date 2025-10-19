from ai_engine import explain_bug
from rich.console import console
from rich.markdown import markdown

console = console()
def main():
  console.print("[bold green ]AI debugging Assistant[/bold green]\n")
  error_log = console.input("[bold yellow]Paste your error log:[/blod yellow]\n")

console.print("\n[bold cyan]Analyzing...[/bold cyan]\n")
result = explain_bug(error_log)
console.print(markdown(result))

if __name__=="__main__":
  main()
