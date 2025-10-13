import turtle as trtl
import random

# create an empty list of turtles
my_turtles = []

direction = 90

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]
turtle_size = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
turtle_length = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = random.choice(turtle_colors)
  t.color(new_color)
  t.fillcolor(new_color)
  new_size = random.choice(turtle_size)
  t.pensize(new_size)
  new_length = random.choice(turtle_length)
  my_turtles.append(t)

#  starting points for turtles
startx = 0
starty = 0

# moves the turtles
for t in my_turtles:
  t.setheading(direction)
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.right(45)
  t.forward(new_length)
  direction = t.heading()
  length = random.randint(50, 101)

# after each turtle, move the starting points
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
