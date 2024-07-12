from turtle import Turtle
import time
from turtle import Screen
from player import Player 
from car_manager import CarManager 
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.up,"Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_cars()
    
    carmanager.move_cars()
    for car in carmanager.all_cars :
        if car.distance(player) < 20 :
            game_is_on = False 
            score.game_over()

        if player.finish_line () :
            player.starting_position()
            carmanager.level_up()
            score.increase_level()
        

screen.exitonclick()