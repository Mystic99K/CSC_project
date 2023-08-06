from rich.console import Console
from rich.text import Text


console = Console()

menu = Text()

tex_color = "#58ACDB"
bg_color = "#6DE5F2"


menu.append("\n=========================MAIN MENU=========================\n", style=f"{tex_color} on {bg_color}")
menu += f"""[Currently logged in as Guest]\n"""
menu += "1. Login\n"
menu += "2. Show weather\n"
menu += "3. Options\n"
menu += "4. Exit program\n"

console.print(menu)