
f = open("data.csv", "r")
# Read and process the file
data = [line.strip().split(",") for line in f]  # Read each line and split by commas
f.close()

# Find the max width of each column
col_widths = [max(len(row[i]) for row in data) for i in range(len(data[0]))]

# Create horizontal border
horizontal_border = "+".join("-" * (w + 2) for w in col_widths)
horizontal_border = f"+{horizontal_border}+"

# Print the table
print(horizontal_border)  # Top border
for i, row in enumerate(data):
    row_str = "| " + " | ".join(row[j].ljust(col_widths[j]) for j in range(len(row))) + " |"
    print(row_str)
    if i == 0:  # Print border after the header
        print(horizontal_border)
print(horizontal_border)  # Bottom border
