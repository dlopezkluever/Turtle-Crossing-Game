from turtle import Turtle, ontimer

class Frogger(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.setpos(0,(-337.5-25))
        self.color("green")
        self.penup()

    def up(self):
        self.forward(25)

    def down(self):
        self.backward(25)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        # self.shape("turtle")
        self.penup()
        # self.color("green")

    def go_right_car(self, list, y_cor_list):
        self.shape(list)
        self.setposition(-260, y_cor_list)
        self.setheading(0)


    def go_left_car(self, list_item, y_cor):
        self.shape(list_item)
        self.setheading(180)
        self.setposition(260, y_cor)

def write_with_border(text, x, y, font=("Arial", 24, "bold"), border_color="black", text_color="white", seconds=10):
    turtle_for_writing = Turtle()
    turtle_for_writing.hideturtle()
    turtle_for_writing.penup()

    # Draw border
    offsets = [(4, 4), (-4, -4), (-4, 4), (4, -4)]
    turtle_for_writing.color(border_color)
    for dx, dy in offsets:
        turtle_for_writing.goto(x + dx, y + dy)
        turtle_for_writing.write(text, align="center", font=font)

    # Draw main text
    turtle_for_writing.color(text_color)
    turtle_for_writing.goto(x, y)
    turtle_for_writing.write(text, align="center", font=font)
    # Schedule clearing after 'duration' milliseconds
    ontimer(turtle_for_writing.clear, seconds)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        with open("high_score.txt") as file_score:
            self.high_score = int(file_score.read())
        self.player_score = 0
        self.update_scoreboard()

    def intro(self):
        self.color("gold", "white")

        write_with_border('"Hey Tubby the Turtle, This\nParty is cRaZzZzY!! Wya??"', 0, 180,
                               font=("Ariel", 22, "normal"), border_color="black", text_color="white", seconds=10)

        write_with_border("Don't get Ran Over; Use the\nUp & Down keys to move!", 0, -190,
                               font=("Ariel", 12, "normal"), border_color="black", text_color="white", seconds=10)

    def update_scoreboard(self):
        self.clear()
        write_with_border(f"High Score: {self.high_score}  Level: {self.player_score + 1}", -0, -390, font=("Courier", 20, "normal"), border_color="black", text_color="white")


    def splat(self):
        self.pencolor("gold")
        self.goto(0, 0)
        if self.player_score == 1:
            self.write(f"SPLAT! (You Died)\n{self.player_score} Party Attended!", align = "center", font=("Ariel", 30, "normal"))
        else:
            self.write(f"SPLAT! (You Died)\n{self.player_score} Parties Attended!", align = "center", font=("Ariel", 30, "normal"))

    def new_high_score(self):
        if self.player_score > self.high_score:
            with open("high_score.txt", mode='w') as file_score:
                file_score.write(f"{self.player_score}")
            self.color("red")
            self.goto(0, -130)
            self.write(f"New High Score!\n{self.player_score} Parties Attended!", align = "center", font=("Ariel", 30, "normal"))
        else:
            return
