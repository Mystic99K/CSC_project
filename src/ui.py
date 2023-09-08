from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt
from rich.layout import Layout
from rich.align import Align
from rich.table import Table
from utils import *
from rich import box

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
        os.system('clear')
        
        table = Table(show_header=True, header_style="bold bright_magenta",border_style='bright_yellow' , show_lines=True, box=box.DOUBLE_EDGE)
        table.add_column("METRIC",justify="center",min_width=10)
        table.add_column("IMPERIAL",justify="center",min_width=10)

        table.add_row("Celsius", "Fahrenheit")
        table.add_row("Kph", "Mph")
        table.add_row("mb", "in")
        table.add_row("mm", "in")
        table.add_row("km", "mi")
        
        main_console.print(table)

        print("1. Metric\n2. Imperal\n3. Both")
        unitpref = input("Enter unit preference:")
        
        if unitpref == '1':
            setting = 0  #Metic
            return setting
        elif unitpref == '2':
            setting = 1  #Impirial
            return setting
        elif unitpref == '2':
            setting = 3  #Impirial
            return setting
        else:
            input("Error: Invalid input (ENTER): ")
        