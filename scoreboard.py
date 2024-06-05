from turtle import Turtle
fp = open("score.txt","r")
high_score = fp.read()
high_score = int(high_score)
fp.close()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.h_score = high_score
        self.color("white")       
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highest Score: {self.h_score}",align="center", font=("Arial",20,"normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        if self.score> self.h_score:
            self.h_score = self.score
        self.write(f"Game Over\nScore: {self.score}, Highest Score: {self.h_score}",align="center", font=("Arial",24,"normal"))
    