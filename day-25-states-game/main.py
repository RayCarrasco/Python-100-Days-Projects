import turtle
from engine import Engine


def main():
    screen = turtle.Screen()
    screen.title('U.S. States Game')
    image_path = 'blank_states_img.gif'
    screen.addshape(image_path)
    turtle.shape(image_path)
    engine = Engine()

    game_is_on = True
    while game_is_on:
        answer_state = screen.textinput(
            title=f'{engine.get_score()}/50 Guess the State',
            prompt="What's another state's name?"
        ).title()
        engine.is_an_estate(answer_state)
        if engine.score == 50:
            game_is_on = False
            print('You Completed ;)')
        if answer_state == 'Exit':
            break
    engine.get_dont_guessed_states()


if __name__ == '__main__':
    main()
