# This function imports the math function need for Pi.
import math

# Function to calculate the surface area of a cylinder 
def calculate_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

# This will be the function to calulcate the volume 
def calculate_volume(radius, height):
    return math.pi * radius**2 * height

# Get user input for radius and height
radius = float(input("Please enter the radius of the cylinder: "))
height = float(input("Please enter the height of the cylinder: "))

# Calculate surface area and volume
surface_area = calculate_surface_area(radius, height)
volume = calculate_volume(radius, height)

# Output the results
print(f"Surface area of the cylinder is {surface_area:.2f} square units.")
print(f"Volume of the cylinder is {volume:.2f} cubic units.")