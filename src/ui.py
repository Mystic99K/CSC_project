from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.align import Align

main_console = Console(color_system="standard")

def print_menu(console, heading, tex_color, border_color, menu, menu_align = "left"):
    if menu_align == "left":
        menu_pan = Panel(
            Align.left(menu),
            title = heading,
            border_style = border_color,
            subtitle = "",
            style=f"{tex_color}"
        )
    elif menu_align == "center":
        menu_pan = Panel(
            Align.center(menu),
            title = heading,
            border_style = border_color,
            subtitle = "",
            style=f"{tex_color}"
        )
    elif menu_align == "right":
        menu_pan = Panel(
            Align.right(menu),
            title = heading,
            border_style = border_color,
            subtitle = "",
            style=f"{tex_color}"
        )
    
    console.print(menu_pan)
    
# print_menu(
#     main_console,
#     "MAIN MENU",
#     "#58ACDB",
#     "",
#     Text()
#         .append(f"""[Currently logged in as Guest]\n""", style="italic red")
#         .append("1. Login\n")
#         .append("2. Show weather\n")
#         .append("3. Options\n")
#         .append("4. Exit program\n")
# )