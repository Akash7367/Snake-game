from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_up, "Up")

is_on = True
while is_on:
  screen.update()
  snake.move()
  time.sleep(0.1)
  scoreboard.update_score()
  
  #detect collision with food
  if snake.seg[0].distance(food)<15:
        food.refress()
        snake.extend()
        scoreboard.increase_score()
    
  #detect collision with wall
  if snake.seg[0].xcor()<-300 or snake.seg[0].xcor()>280 or snake.seg[0].ycor()<-280 or snake.seg[0].ycor()>300:
    is_on=False
    scoreboard.game_over()
    
  #detect collision with body
  for segment in snake.seg:
    if segment==snake.seg[0]:
      pass#we cen use slicing at the place of if use for segment in snake.seg[1:] then not need to write this if statement
    elif snake.seg[0].distance(segment)<10:
      is_on=False
      scoreboard.game_over()
    
screen.exitonclick()