from turtle import Turtle,Screen
import random

class Food(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.color("blue")
    self.shape("circle")
    self.shapesize(0.5,0.5)
    self.speed("fastest")
    self.refress()
    
  def refress(self):
    x=random.randrange(-260,260)
    y=random.randrange(-260,260)
    self.goto(x,y)
    