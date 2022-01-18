import turtle as t
import random

class Screen():
    my_screen = t.Screen()
    my_screen.screensize(canvwidth=800, canvheight=600)
    my_screen.bgcolor("black")
    my_screen.title("lynni's Pong")
    my_screen.exitonclick()

my_screen = Screen()
my_screen()