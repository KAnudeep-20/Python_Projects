from turtle import Turtle, Screen
import turtle as T
import random

# TURTLE RACE
screen = Screen()
screen.setup(500, 400)  # width=500, height=400 of screen
       #This make us see a pop-up on the screen which will allow us to make the bet
user_bet = screen.textinput(title="Make your bet", prompt="Which trutle will win the race? Enter a colour: ")
y_positions = [-50, -20, 10, 40, 70]
colors = ["red", "green", "yellow", "blue", "purple"]
 # Making multiple trutles
racing_turtles = []
for i in range(5):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.up()
    tim.goto(-230, y_positions[i])
    racing_turtles.append(tim)

  # Starting the race
israce_on = False
if(user_bet):
    israce_on = True
    while(israce_on):
        for turtle in racing_turtles:
            if(turtle.xcor() > 230):  # 230 because a turtle shape is off 40/40 so if we want to che k which crossed first we need to check the half body of turtle crossed 250 i.e., 250-20
                winner_turtle = turtle.pencolor()
                if(winner_turtle==user_bet):
                    print(f"You've won! The {winner_turtle} turtle is the winner!")
                    israce_on = False
                    break
                else:
                    print(f"You've lost! The {winner_turtle} turtle is the winner!")
                    israce_on = False
                    break 
            turtle.forward(random.randint(1, 10))

screen.exitonclick()