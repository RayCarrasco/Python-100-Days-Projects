from random import choice
from colorgram import extract
from turtle import Turtle, Screen


def extract_colors(path, number_colors):
    """
    ('path/image.jpg') Use colorgram to return a color list
    """
    colors = extract(
        path,
        number_colors
    )
    colors_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        temp_tuple = (r, g, b)
        colors_list.append(temp_tuple)
    colors_list.remove(colors_list[0])
    colors_list.remove(colors_list[0])
    return colors_list


def draw(color_list):
    """"
    Draw an arrange of dots of 10x10 like Hirst modern art.
    """
    tim = Turtle()
    tim.speed(0)
    screen = Screen()
    screen.colormode(255)
    screen.bgcolor((254, 255, 245))
    #screen.screensize(canvwidth=700, canvheight=700)
    tim.hideturtle()
    tim.penup()
    y = -225
    for i in range(9):
        tim.sety(y + i * 50)
        tim.setx(-225)
        for _ in range(9):
            tim.dot(20, choice(color_list))
            tim.forward(50)

    screen.exitonclick()


def main():
    """"main function"""
    path = 'C:\\Users\\rymnd\\PycharmProjects\\day-18-start\\media\\dots.jpg'
    number_colors = 30
    colors = extract_colors(path, number_colors)
    draw(colors)


main()
