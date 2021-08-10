import pandas
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "normal")


class Engine(Turtle):
    """
    Game engine to guess the U.S. State turtle game
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()

        self.file_path = '50_states.csv'
        self.data = self.get_data()
        self.states_list = self.get_states()
        self.score = 0
        self.guessed_states = []

    def get_data(self):
        return pandas.read_csv(self.file_path)

    def get_states(self):
        return self.data.state.to_list()

    def get_score(self):
        """
        Provides the current score
        """
        return self.score

    def is_an_estate(self, answer_state):
        """"
        Verify if the state exists, if so then is written in the map with its coordinates and the score is updated.
        Take as parameter the name of the state
        """
        if answer_state in self.states_list:
            self.write_state(answer_state)
            self.score += 1
            self.guessed_states.append(answer_state)

    def write_state(self, answer_state):
        state_data = self.data[self.data.state == answer_state]
        state_name = state_data.state.item()
        x = int(state_data.x)
        y = int(state_data.y)

        self.goto(x, y)
        self.write(f"{state_name}", align=ALIGNMENT, font=FONT)

    def get_dont_guessed_states(self):
        """
        Creates a cvs file with the states that were not guessed
        """
        # states_to_study = self.states_list
        # for guessed in self.guessed_states:
        #     states_to_study.remove(guessed)

        states_to_study = [state for state in self.states_list if state not in self.guessed_states]

        to_study = {'Missing State(s)': states_to_study}
        missing_states = pandas.DataFrame(to_study)
        missing_states.to_csv('Missing_states.csv')
