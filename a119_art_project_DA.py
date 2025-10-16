import turtle
import random
import itertools

# turtle list
turtles = []

# different turtle lists
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", 
                 "darkred", "darkblue", "lime", "salmon", "indigo", "brown"]
turtle_drawshape = ["circle", "triangle", "square", "star", "hexagon"]

# square func
def draw_square(size, color):
    t.color(color)
    for _ in range(4):
        t.forward(size)
        t.right(90)

# triangle func
def draw_triangle(size, color):
    t.color(color)
    for _ in range(3):
        t.forward(size)
        t.right(120)

# circle func
def draw_circle(radius, color):
    t.color(color)
    t.circle(radius)

# star func
def draw_star(size, color):
    t.color(color)
    for _ in range(5):
        t.forward(size)
        t.right(144)

# hexagon func
def draw_hexagon(size, color):
    t.color(color)
    for _ in range(6): 
        t.forward(size)
        t.right(60)

num = int(input("How many turtles? "))
counter = 0

# set turtle shape
for s in itertools.cycle(turtle_shapes):
    if counter < num:
        t = turtle.Turtle(shape=random.choice(turtle_shapes))
        t.speed(0)
        t.pensize(random.randint(5, 21))
        t.penup()
        t.goto(random.randint(-300, 301), random.randint(-300, 301))
        t.pendown()
        turtles.append(t)
        counter = counter + 1
    elif counter >= num:
        break

# set turtle drawing shape
for t in turtles:
    draw_shape = random.choice(turtle_drawshape)
    if draw_shape == "circle":
        draw_circle(random.randint(20, 101), random.choice(turtle_colors))
    elif draw_shape == "triangle":
        draw_triangle(random.randint(20, 101), random.choice(turtle_colors))
    elif draw_shape == "square":
        draw_square(random.randint(20, 101), random.choice(turtle_colors))
    elif draw_shape == "star":
        draw_star(random.randint(20, 101), random.choice(turtle_colors))
    elif draw_shape == "hexagon":
        draw_hexagon(random.randint(20, 101), random.choice(turtle_colors))

wn = turtle.Screen()
wn.mainloop()