import time

from map_writer import MapWriter
import pandas
import turtle
from turtle import Turtle, Screen
diagram = "blank_states_img.gif"
states_doc = pandas.read_csv("50_states.csv")
correct_answers = []
writers = []
states_to_learn = {"states to learn": []}
screen = Screen()

screen.addshape(diagram)
screen.title("U.S. States Game")
turtle.shape(diagram)

while len(writers) != 50:  # main game loop
    answer = (screen.textinput(f"{len(correct_answers)}/ 50 states guessed correctly",
                               "Type the name of a U.S. state:")).title()
    if answer == "Exit":
        # if user types "exit" or "Exit", this loop prints a csv of all missed answers, and exits the game
        if not states_doc["state"].all() in correct_answers:
            states_to_learn["states to learn"].extend(states_doc.state)
            for s in states_to_learn["states to learn"]:
                if s in correct_answers:
                    states_to_learn["states to learn"].remove(s)
            learning_df = pandas.DataFrame(states_to_learn)
            learning_df.to_csv("states_to_learn")
            break
        time.sleep(1)
        screen.bye()
    else:
        # this loop iterates over state doc, and if user guesses correctly,
        # instantiates a Turtle object flagging the proper location of the state on the map
        for row in states_doc["state"]:
            if not (states_doc["state"] == answer).any():
                break
            else:
                if answer not in correct_answers:
                    writer_frame = (states_doc.loc[states_doc["state"] == answer]).iloc[0]
                    correct_answers.append(answer)
                    writer_tuple = (writer_frame.state, int(writer_frame.x), int(writer_frame.y))
                    writer = MapWriter(writer_tuple)
                    if writer:
                        writers.append(writer)
                        break
                    else:
                        break
                else:
                    break
    time.sleep(.5)

# Sequence to close out the game when all states have been guessed correctly
if len(writers) == 50:
    final_boss = MapWriter(("Congratulations! You win!", -210, 0))
    time.sleep(3)
    screen.bye()




