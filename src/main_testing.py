from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt

console = Console()
err_console = Console(stderr=True, style="bold red")

tex_color = "#58ACDB"
bg_color = "#6DE5F2"

menu = Text()
menu.append(f"""[Currently logged in as Guest]\n""", style="italic red")
menu.append("1. Login\n")
menu.append("2. Show weather\n")
menu.append("3. Options\n")
menu.append("4. Exit program\n")

console.print( 
    Panel(
        menu,
        title="MAIN MENU", 
        subtitle="",
        style=f"{tex_color}"
    ),
)
choice = Prompt.ask("Enter your option", style=f"{tex_color}")

print(choice, type(choice))

# err_console.print( 
#     Panel(
#         menu,
#         title="MAIN MENU", 
#         subtitle=""
#     )
# )