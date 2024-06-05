pos = 285.0
neg = -285.0


from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import *
import time






screen = Screen()
screen.setup(width = 600, height= 600)
screen.bgcolor("black")

screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.title("Snake Game")




screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


 
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:    #Detect Food
        food.refresh()
        snake.increase()
        scoreboard.increase_score()

    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > pos or y > pos or x < neg or y < neg :   #Detect Wall
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[2::]:
        if snake.head.distance(segment)<10:
            scoreboard.game_over()
            game_is_on = False


f = open("score.txt",'w')
f.write(str(scoreboard.h_score))
    
    
        
        












screen.exitonclick()