from rich.console import Console # styling directly in print statements
from rich.theme import Theme

# Defining custom themes using dictionary
custom_themes = Theme(
    {
        "general": "blue", 
        "error": "red bold",
        "success": "green bold",
        "title": "#FF8000"
    }
)
# Setting print console from rich
console = Console(color_system="standard", theme=custom_themes) # standard bcoz cmd supports 16 colors