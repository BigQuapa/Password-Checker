"""
    Program: Drawing a Circle
    
"""
# Author: Shahakar Patel 

import math
from turtle import Turtle, Screen

def drawCircle(t, x, y, radius):
    """Draws a circle with the given center point and radius."""
    # Move the turtle to the starting position
    t.penup()
    t.goto(x, y - radius)  # Position at the top of the circle
    t.pendown()
    
    # Calculate the distance to move per step
    step_distance = 2.0 * math.pi * radius / 120.0
    
    # Draw the circle in 120 steps
    for _ in range(120):
        t.forward(step_distance)
        t.left(3)  # Turn 3 degrees

def main():
    # Create a screen to display the drawing
    screen = Screen()
    screen.setup(width=600, height=600)
    
    # Initialize the turtle
    t = Turtle()
    t.speed(0)  # Set to maximum drawing speed
    
    # Circle parameters
    x = 50
    y = 75
    radius = 100
    
    # Draw the circle
    drawCircle(t, x, y, radius)
    
    # Keep the window open until clicked
    screen.mainloop()

if __name__ == "__main__":
    main()
