from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich import box

selected_prof = {}

console = Console()
err_console = Console(stderr=True, style="bold red")

tex_color = "green"
bg_color = "#6DE5F2"
theme = 'black'


if selected_prof:
    menu = f"""[Currently logged in as '{selected_prof["name"]}']\n"""
else:
    menu = f"""[Currently logged in as Guest]\n"""
menu += "1. Login\n"
menu += "2. Show weather\n"
menu += "3. Options\n"
if selected_prof:
    menu += "4. Logout\n"
    menu += "5. Exit program\n"
else:
    menu += "4. Exit program\n"



console.print(Panel(menu,title='Main Menu', style=f"bright_cyan on {theme}",border_style='bright_yellow',box=box.DOUBLE_EDGE))

choice = Prompt.ask("Enter your option")

print(choice, type(choice))

