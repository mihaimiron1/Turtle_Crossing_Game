from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:  # Adjust the frequency of car creation
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-230, 240))  # Random y position
            self.cars.append(new_car)
            new_car.setheading(180)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)


    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
    
    def reset(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
        
    
