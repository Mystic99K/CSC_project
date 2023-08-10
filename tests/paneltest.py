from rich import print
from rich.panel import Panel
from rich.columns import Columns

# Create three panels
panel1 = Panel("Panel 1 content")
panel2 = Panel("Panel 2 content")
panel3 = Panel("Panel 3 content")

# Put them in a Columns object
columns = Columns([panel1, panel2, panel3])

# Print the columns
print(columns)