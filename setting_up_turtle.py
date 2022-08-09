from turtle import Turtle, Screen
import random

screen_obj = Screen()
screen_obj.setup(height=400, width=500)
screen_obj.colormode(255)

y_axis = -150
list_obj = []

# Creating 5 turtle objects from the Turtle class.
for i in range(1, 6):
    turtle_obj = Turtle()
    list_obj.append(turtle_obj)
    turtle_obj.shape("turtle")
    # 3 set of random numbers from 1 to 255 represent r,g,b scale.
    turtle_obj.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    turtle_obj.penup()
    turtle_obj.goto(-240, y_axis)
    y_axis = y_axis + 70

#print(list_obj)

# Moving turtle
def move_object(turtle_obj):
    turtle_obj.speed(1)
    turtle_obj.forward(10)

# Selecting one turtle object from list of Turtle objects and moving it forward.
for y in range (0,500):
    turle_fwd = random.choice(list_obj)
    turtle_position = turle_fwd.pos()
    #print(turtle_position)
    move_object(turle_fwd)
    if turtle_position[0] >= 235.00:
        print(f"{turle_fwd} {turle_fwd.color()} won the race")
        break


screen_obj.exitonclick()
