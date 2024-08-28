from turtle import Turtle
allignment="center"
Font=("arial", 17, "normal")
class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score=0
    self.color("white")
    self.penup()
    self.goto(0,269)
    self.hideturtle()
    self.update_score()
    
  def update_score(self):
    self.write(f"Score: {self.score}", align=allignment, font=Font)

  def game_over(self):
    self.goto(0,0)
    self.write(f"GAME OVER \nYour Scoce: {self.score}", align=allignment, font=Font)
    

  def increase_score(self):
    self.score+=10
    self.clear()
    self.update_score()
    