from turtle import Screen
from turtle_crossing_classes import Frogger, Scoreboard, Car
import random
from time import sleep

# Screen Setup
screen = Screen()
screen.setup(500, 800)
screen.tracer(0)
screen.bgpic("Images/Back_Image.png")
screen.update()

# Scoreboard & Intro Message Call
scoreboard = Scoreboard()
scoreboard.intro()
screen.update()
sleep(3)
scoreboard.update_scoreboard()

# Car Image Upload
shapes_list = []
for i in range(1, 8):
    screen.addshape(f"Images/{i}.gif")
    shapes_list.append(f"Images/{i}.gif")
back_shapes_list = []
for i in range(10, 17):
    screen.addshape(f"Images/{i}.gif")
    back_shapes_list.append(f"Images/{i}.gif")

# Frogger Setup with Keyboard Functionality
screen.listen()
frog = Frogger()
screen.onkeypress(frog.up, "Up")
screen.onkeypress(frog.down, "Down")
screen.update()

# Position cars
y_positions_left = [-312.5 + 50 * o for o in range(12)]
y_positions_right = [-337.5 + 50 * o for o in range(12)]

# Game Variables
go_car = []
game = True
velocity = 4
spawn_chance = 200

# Game Functionality / Main-Loop
while game:
    # Spawn cars
    spawn_draw = random.randint(0, spawn_chance)
    if spawn_draw <= 10:
        car = Car()
        car.go_right_car(shapes_list[random.randint(0, 6)], (-312.5 + 50 * random.randint(0, 11)))
        go_car.append(car)
        car2 = Car()
        car2.go_left_car(back_shapes_list[random.randint(0, 6)], (-337.5 + 50 * random.randint(0, 11)))
        go_car.append(car2)

    # Move cars
    if len(go_car) > 0:
        for car in go_car:
            car.forward(velocity)  # Move based on time
            if car.distance(frog) <= 10:
                scoreboard.splat()
                scoreboard.new_high_score()
                game = False
        sleep(.01)
    screen.update()

    if frog.ycor() >= 325:
        scoreboard.player_score += 1
        scoreboard.update_scoreboard()
        frog.setposition(0,-337.5 - 25)
        for y in go_car:
            y.forward(1000)
        velocity += 3
        if 50 < spawn_chance:
            spawn_chance -= 10
        elif 30 < spawn_chance <= 50:
            spawn_chance -= 4
        elif 20 < spawn_chance <= 30:
            spawn_chance -= 1
        screen.update()
screen.exitonclick()

# How to move to GitHub
# git remote add origin https://github.com/your-username/your-repo.git
# For this app: git remote add origin https://github.com/dlopezkluever/Turtle-Crossing-Game.git

# git config --global user.email "dlopezkluever@gmail.com"
# git config --global user.name "Daniel Lopez"