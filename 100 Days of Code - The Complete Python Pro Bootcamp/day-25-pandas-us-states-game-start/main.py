import turtle
import pandas
from numpy.ma.core import shape

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("The U.S. States Game")

screen.addshape(IMAGE)
turtle.shape(IMAGE)

def get_mouse_click_coordinates(x,y):
    print (x,y)


# screen.onscreenclick(get_mouse_click_coordinates)

# turtle.mainloop()

data = pandas.read_csv("50_states.csv")

states = data["state"]
xcor = data["x"]
ycor = data["y"]
# for _ in range(len(data)):
#     states.concat(data["state"])
#     xcor.concat(data["x"])
#     ycor.concat(data["x"])
print(states)

used = []
states_left = True
writer = turtle.Turtle()
writer.penup()
answer_state = screen.textinput("Guess the state",prompt="What is a state?").title()
while states_left:

    if answer_state == "New york":
        answer_state = "New York"
    elif answer_state == "New jersey":
        answer_state = "New Jersey"
    elif answer_state == "Exit":
        break

    # for item in range(0,len(states)):
    if states.isin([answer_state]).any():
        if answer_state not in used:
            used.append(answer_state)

        index = states[states ==answer_state].index
        # print(data[data.state == str(answer_state)])
        writer.goto(int(xcor[index]),int(ycor[index]))
        writer.write(f"{answer_state}", font=("Arial",11,"normal"))

    else:
        pass

    # if answer_state:
    #     pass
    answer_state = screen.textinput(title=f"{len(used)}/50 correct",prompt="What is another state?").title()

final = []
for state in states:
    if state not in used:
        final.append(state)

df = pandas.Series(final)
df.to_csv("states_to_learn.csv", index = False)
# with open("states_to_learn.csv",mode ="w") as to_learn:
#     to_learn.csv(final)



screen.exitonclick()