from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt

console = Console()
err_console = Console(stderr=True, style="bold red")

# tex_color = "#58ACDB"
# bg_color = "#6DE5F2"

choice = Prompt.ask("Enter your option")

# print(choice, type(choice))

# console.print( 
#     Panel(
#         menu,
#         title="MAIN MENU", 
#         subtitle="",
#         style=f"{tex_color}"
#     ),
# )
# choice = Prompt.ask("Enter your option")

# print(choice, type(choice))

# err_console.print( 
#     Panel(
#         menu,
#         title="MAIN MENU", 
#         subtitle=""
#     )
# )

# import rich

# def ask_input(message):
#   """Asks the user for input in a rich panel."""
#   panel = rich.panel(message)
#   text_input = rich.TextInput(prompt="Enter your input: ")
#   panel.append(text_input)

#   return text_input.run()

# if __name__ == "__main__":
#   input = ask_input("Enter your name: ")
#   print(f"Your name is {input}")
