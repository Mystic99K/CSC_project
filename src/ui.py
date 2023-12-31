from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.layout import Layout
from rich.align import Align

main_console = Console(color_system="standard")
w_console = Console(color_system="standard",height=8)
align = "center"  #Change this to left or center

def print_menu(console, heading, tex_color,border_color, menu):
    menu_pan = Panel(
        Align(menu,align),
        title = heading,
        border_style = border_color,
        subtitle = "",
        style=f"{tex_color}",
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


