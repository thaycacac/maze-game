import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("A Maze Game")
screen.setup(700, 700)

#declare list
walls = []
levels = []

#create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#lv1
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXXE         XXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X      XX  XXX        XXX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"XE               XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX        TXXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXXE             X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XX     E   XXXX        XX",
"XXXX               T    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#setup level
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            position_x = -288 + (x * 24)
            position_y = 288 - (y * 24)
            if character == "X":
                pen.goto(position_x, position_y)
                pen.stamp()
                #add coordinates to wall list
                walls.append((position_x, position_y))

pen = Pen()
setup_maze(level_1)
