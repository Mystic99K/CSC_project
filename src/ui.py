from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils import *

main_console = Console(color_system="standard")
align = "left"  #Change this to left or center

def print_menu(console, heading, tex_color,border_color, menu):
    menu_pan = Panel(
        Align(menu,align),
        title = heading,
        border_style = border_color,
        subtitle = "",
        style=f"{tex_color}",
    ) 
    
    console.print(menu_pan)
    
#     print_menu(
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


def unit_menu():
    while True:
        cls()
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("METRIC")
        table.add_column("IMPERIAL")

        table.add_row("Celsius", "Fahrenheit")
        table.add_row("Kph", "Mph")
        table.add_row("mb", "in")
        table.add_row("mm", "in")
        table.add_row("km", "Miles")
        
        main_console.print(table)

        print("1. Metric\n2. Imperal")
        unitpref = input("Enter unit preference:")
        
        if unitpref == '1':
            setting = 1  #Metic
            return setting
        elif unitpref == '2':
            setting = 0  #Impirial
            return setting
        else:
            input("Error: Invalid input (ENTER): ")
        