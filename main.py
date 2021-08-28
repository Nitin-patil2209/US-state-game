from turtle import Turtle, Screen
import pandas
data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].to_list()
screen = Screen()
i = 1
turtleg = Turtle()
screen.title("U.S State Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtleg.shape(img)

while i <= 51:
    screenprompt = screen.textinput(title=f"{i} Guess state", prompt="Enter state name")
    if screenprompt in list_of_states:
        state_name = Turtle()
        state_name.hideturtle()
        city = data[data.state == screenprompt]
        x = int(city.x)
        y = int(city.y)
        state_name.penup()
        state_name.goto(x,y)
        state_name.write(screenprompt)
        i += 1

screen.mainloop()