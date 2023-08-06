from rich.console import Console
from rich.text import Text


console = Console()

menu = Text()


menu.append("\n=========================MAIN MENU=========================\n", style="bold magenta")


menu += f"""[Currently logged in as Guest]\n"""
menu += "1. Login\n"
menu += "2. Show weather\n"
menu += "3. Options\n"
menu += "4. Exit program\n"

print(menu)