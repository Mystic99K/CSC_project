from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt

console = Console(color_system='truecolor')
err_console = Console(stderr=True, style="bold red")

prompt_color = "#FFF175"
tex_color = "#64EB51"
bg_color = "#3E9EFF "

menu = Text()
menu.append(f"""[Currently logged in as Guest]\n""", style=f"{prompt_color}")
menu.append("1. Login\n", style=f"{tex_color}")
menu.append("2. Show weather\n", style=f"{tex_color}")
menu.append("3. Options\n", style=f"{tex_color}")
menu.append("4. Exit program\n", style=f"{tex_color}")

console.print( 
    Panel(
        menu,
        title="MAIN MENU", 
        subtitle="",
        style=f"{bg_color}"
    ),
)
choice = Prompt.ask("Enter your option")

print(choice, type(choice))

# err_console.print( 
#     Panel(
#         menu,
#         title="MAIN MENU", 
#         subtitle=""
#     )
# )