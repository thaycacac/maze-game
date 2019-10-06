import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("A Maze Game")
screen.setup(700, 700)


treasures = []
walls = []
levels = []

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        
        self.color("white")
        self.penup()
        self.speed(0)

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.goto(x, y)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.hp=100
        
    def up(self):
        x=self.xcor()
        y=self.ycor()
        if (x,y+24) not in walls:
            self.goto(x,y+24)
            
    def down(self):
        x=self.xcor()
        y=self.ycor()
        if (x,y-24) not in walls:
            self.goto(x,y-24)

              
    def right(self):
        x=self.xcor()
        y=self.ycor()
        if (x+24,y) not in walls:
            self.goto(x+24,y)

    def left(self):
        x=self.xcor()
        y=self.ycor()
        if (x-24,y) not in walls:
            self.goto(x-24,y)
            
    def is_collission(self,other):
        if self.xcor() == other.xcor() & self.ycor() == other.ycor():
            return True
        else:
            return False
         
level_1 = [ 
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXXXE         XXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXXT XXXXX",
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
"XXX         TXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXXE             X",
"XX T XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XX     E   XXXX        XX",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            position_x = -288 + (x * 24)
            position_y = 288 - (y * 24)
            if character == "X":
                pen.goto(position_x, position_y)
                pen.stamp()
                walls.append((position_x, position_y))
            elif character == "P":
                player.goto((position_x, position_y))
            elif character == "T" :
                treasures.append(Treasure(position_x, position_y))

pen = Pen()
player = Player()

turtle.listen()
turtle.onkey(player.up,"Up")
turtle.onkey(player.down,"Down")
turtle.onkey(player.right,"Right")
turtle.onkey(player.left,"Left")

setup_maze(level_1)

while True:
    for treasure in treasures:
        if player.is_collission(treasure):
            print("co linh")
