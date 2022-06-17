import turtle
from turtle import *

n = 10
fibo_arr = []
a = 1
b = 1

# Build fibonacci array
for num in range(n):
    fibo_arr.append(a)
    c = a + b
    a = b
    b = c

nr_squares = len(fibo_arr)
factor = 3

# Function for drawing a square
def draw_square(side_length):
    for i in range(4):
        forward(side_length)
        right(90)

# Draw fibonacci grid
penup()
pencolor('blue')
goto(50,50) # Move starting point right and up
pendown()

for i in range(nr_squares):
    draw_square(factor*fibo_arr[i])  # Draw square
    penup()                          # Move to new corner as starting point
    forward(factor*fibo_arr[i])
    right(90)
    forward(factor*fibo_arr[i])
    pendown()

# Draw quarter circles with fibonacci numbers as radius
penup()
goto(50,50)     # Move to starting point
setheading(0)   # Face the turtle to the right
pencolor('red')
pendown()

for i in range(nr_squares):
    circle(-factor*fibo_arr[i],90)  # Minus sign to draw clockwise

turtle.done()


