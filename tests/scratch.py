from rich.layout import Layout

from rich import print
from rich.table import Table

# Create a table
table = Table(show_header=True, header_style="bold magenta")
table.add_column("METRIC")
table.add_column("IMPERIAL")

# Add rows to the table
table.add_row("Celsius", "Fahrenheit")
table.add_row("Kph", "Mph")
table.add_row("mb", "in")
table.add_row("mm", "in")
table.add_row("km", "Miles")

# Print the table
print(table)

print("1. Metric\n2. Imperal")
unitpref = input("Enter unit preference:")