#-----import statements-----
import turtle
import random
import leaderboard

#-----game configuration----
spot_color = "pink"
spot_shape = "circle"
spot_size = 2
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
sizes = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000 #1000 represents 1 second
timer_up = False
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("Please enter your name: ")

#-----initialize turtle-----
spot = turtle.Turtle()
spot.speed(0)
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)

score_writer = turtle.Turtle()
score_writer.speed(0)
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 250)
score_writer.pendown()
score_writer.showturtle()

counter = turtle.Turtle()
counter.speed(0)
counter.hideturtle()
counter.penup()
counter.goto(250, 250)
counter.pendown()
counter.showturtle()

#-----game functions--------
def spot_clicked(x, y):
    global timer_up
    if timer_up == False:
       change_color()
       change_size()
       change_position()
       update_score()
    else:
       spot.hideturtle()

def change_position():
    new_xpos = random.randint(-300, 300)
    new_ypos = random.randint(-300, 300)
    spot.hideturtle()
    spot.penup()
    spot.goto(new_xpos, new_ypos)
    spot.pendown()
    spot.showturtle()

def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
   global timer, timer_up
   counter.clear()
   if timer <= 0:
      counter.write("Time's Up", font=font_setup)
      timer_up = True
      manage_leaderboard()
   else:
      counter.write("Timer: " + str(timer), font=font_setup)
      timer -= 1
      counter.getscreen().ontimer(countdown, counter_interval) 

def change_color():
   spot.fillcolor(random.choice(colors))
   spot.stamp()
   spot.fillcolor(spot_color)

def change_size():
   spot.shapesize(random.choice(sizes))

def manage_leaderboard():
  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = leaderboard.get_names(leaderboard_file_name)
  leader_scores_list = leaderboard.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    leaderboard.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    leaderboard.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    leaderboard.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)

#-----events----------------
spot.onclick(spot_clicked)
wn = turtle.Screen()
wn.bgcolor("gray")
wn.ontimer(countdown(), counter_interval)
wn.mainloop()