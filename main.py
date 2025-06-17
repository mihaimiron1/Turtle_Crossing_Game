import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing Game")
screen.listen()

score = Scoreboard()
player = Player()
car = CarManager()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    car.create_car()
    car.move_cars()

    if player.at_finish_line():
        player.reset_position()
        score.increase_score()
        car.increase_speed()
        car.reset()
    # Check for collision with cars
    for c in car.cars:
        if player.distance(c) < 30:
            game_is_on = False
            
        
    



    time.sleep(0.1)
    screen.update()

score.game_over()
screen.exitonclick()

