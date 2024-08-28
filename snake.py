from turtle import Turtle

pos = [(0, 0), (-20, 0), (-40, 0)]
Move = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

  def __init__(self):
    self.seg = []
    self.create_snake()
    self.head=self.seg[0]
    
  def move_left(self):
    if self.seg[0].heading() != RIGHT:
      self.seg[0].setheading(LEFT)
      
  def move_right(self):
    if self.seg[0].heading() != LEFT:
      self.seg[0].setheading(RIGHT)

  def move_down(self):
    if self.seg[0].heading() != UP:
      self.seg[0].setheading(DOWN)
      
  def move_up(self):
    if self.seg[0].heading() != DOWN:
      self.seg[0].setheading(UP)

  def create_snake(self):
    for position in pos:
      self.add_snake(position)

  def add_snake(self,position):
      turt = Turtle(shape="square")
      turt.penup()
      turt.goto(position)
      turt.color("white")
      self.seg.append(turt)

  def extend(self):
    self.add_snake(self.seg[-1].position())
    

  def move(self):
    for i in range(len(self.seg) - 1, 0, -1):
      new_x = self.seg[i - 1].xcor()
      new_y = self.seg[i - 1].ycor()
      self.seg[i].goto(new_x, new_y)
    self.seg[0].forward(Move)
    
