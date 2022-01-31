from turtle import Turtle, Screen
from Snake import Snake
import time

#screen commands
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

#imported snake from the snake game
snake = Snake()


#definited the controls
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right,'Right')


#game loop created
game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
