# Calculate area of different rectangles - WITH functions
print("=== WITH FUNCTIONS (Good Reusability) ===")

def calculate_rectangle_area(length, width):
    """Reusable function to calculate rectangle area"""
    return length * width

def display_result(name, length, width, area):
    """Reusable function to display results"""
    print(f"{name}: {length} x {width} = {area}")

# Same calculations, but using reusable functions
rectangles = [
    ("Rectangle 1", 10, 5),
    ("Rectangle 2", 8, 3),
    ("Rectangle 3", 15, 7),
    ("Rectangle 4", 12, 4),
    ("Rectangle 5", 20, 10)
]

for name, length, width in rectangles:
    area = calculate_rectangle_area(length, width)
    display_result(name, length, width, area)

print()