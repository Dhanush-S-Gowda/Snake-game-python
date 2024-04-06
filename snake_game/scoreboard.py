from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_game/data.txt", "r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.update_score()
        self.hideturtle()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game/data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()