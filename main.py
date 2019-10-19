#thaycacac
import turtle
import math
import random
import time
import game_easy

map_easy = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXXE         XXXXXX      XXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXXXX  XX  XXXXXX",
    "X       XX  XXXXXX  XXXX     XX    XXXX",
    "X      XX  XXX        XX  XX XX     XXX",
    "XXXXXX  XX  XXX                 XXX  XX",
    "XXXXXX  XX  XXXXXX  XXXXX     XXXXX   X",
    "XXXXXX  XX    XXXX  XXXXX        XX  XX",
    "X  XXX        XXXX  XXXXXXXXXX   XXXXXX",
    "X  XXX  XXXXXXXXX          XXXX  XXXXXX",
    "X         XXXXXXXXXXXXXXX  XXXX  XXXXXX",
    "XE               XXXXXXXX  XXXX    XXXX",
    "XXXXXXXXXXXX     XXXXX  X    XXXX  XXXX",
    "XXXXXXXXXXXXXXX  XXXXX  XXX  XXXX  XXXX",
    "XXX  XXXXXXXXXX         XXX  XXXX    XX",
    "XXX                     XXXXXXX    XXXX",
    "XXX        TXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXXXX      XXXXXX",
    "XXXXXXXXXXE             XXXXX     XXXXX",
    "XX   XXXXX              XXXXXXXX  XXXXX",
    "XX   XXXXXXXXXXXXX  XXXXXXXXXXXX  XXXXX",
    "XX    XXXXXXXXXXXX  X      XXXXX    XXX",
    "XX     E   XXXX        XX     XXXX  XXX",
    "XXXX               TXXXXXXXX  XXXX  XXX",
    "XXXXXXXXXXXXXXXX        XXXX        HXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

map_medium = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXXE         XXXXXX      XXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXXXX  XX  XXXXXX",
    "X      TXX  XXXXXX  XXXX     XX   TXXXX",
    "X E    XX  XXX       EXX  XX XX     XXX",
    "XXXXXX  XX  XXX              E  XXX  XX",
    "XXXXXX  XX  XXXXXX  XXXXX     XXXXX   X",
    "XXXXXX  XX    XXXX  XXXXX        XX  XX",
    "X  XXX        XXXX  XXXXXXXXXX   XXXXXX",
    "X  XXX  XXXXXXXXX   E      XXXX  XXXXXX",
    "X         XXXXXXXXXXXXXXX  XXXX  XXXXXX",
    "XE               XXXXXXXX  XXXX    XXXX",
    "XXXXXXXXXXXX     XXXXX TX    XXXX  XXXX",
    "XXXXXXXXXXXXXXX  XXXXX  XXX  XXXX  XXXX",
    "XXX TXXXXXXXXXX         XXX  XXXX   TXX",
    "XXXE                    XXXXXXX   EXXXX",
    "XXX        TXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXXXX      XXXXXX",
    "XXXXXXXXXXE             XXXXX     XXXXX",
    "XXE  XXXXX             EXXXXXXXX  XXXXX",
    "XX   XXXXXXXXXXXXX  XXXXXXXXXXXX EXXXXX",
    "XX    XXXXXXXXXXXX  X      XXXXX    XXX",
    "XX     E   XXXX        XX     XXXX  XXX",
    "XXXXT              TXXXXXXXX  XXXX  XXX",
    "XXXXXXXXXXXXXXXX       TXXXX    E   HXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

map_hard = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP     XT   X     X X  XT       XT    X",
    "X X XX     EX X X X XX         EX XXXXX",
    "X X XXXXXXX X XXX X  X XXXXXXXX X    EX",
    "X XXXE    X X   X XX X X        XXXXX X",
    "X X   X X X XXX X    X XXXXXXXX X     X",
    "X X XXXXX X     XXXXXX  X       X XXXXX",
    "X X XE TX XXXXXXX       X XXXXXXX X   X",
    "X X X X X       X X X XXX       X X X X",
    "X X X X XXXXXXX X X X XXXXXXXXX X X X X",
    "X X X X X   X X X X X X         X X X X",
    "X X X X       X   X   X XXXXX XXX   X X",
    "X X X XXXXXXXXXXXXX XXX X X XXX XXXXX X",
    "XT  X    X             EX             X",
    "XXXXXXXX X XXXXXXXXXT   X X X XXXXX XXX",
    "X        X         XXXXXXXX XXXT  XXX X",
    "XXXXXXXX X XXXXXXX X     EXE          X",
    "X        X       X X X XX XXXXXXXXXXX X",
    "X X XXX XXXXXXXX X X X X          X X X",
    "X X XTX X      X X X X X X  TXXXX X X X",
    "X X    EX X XX X X X XXXXXXXXX    X X X",
    "X XXXXXXX X X  X XXX X       X XXXX X X",
    "X X     X XXXX X     X X X X X        X",
    "X X X X X XT   XXXXXXX X T X XXXXXXXX X",
    "X   X X   XXXX        EXXXXX         HX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]


def main():
    screen = turtle.Screen()
    screen.tracer(0)

    easy = "easy.gif"
    medium = "medium.gif"
    hard = "hard.gif"
    screen.addshape(easy)
    screen.addshape(medium)
    screen.addshape(hard)

    # create level
    class Level(turtle.Turtle):

        level = ""

        def __init__(self, level, position_y):
            turtle.Turtle.__init__(self)
            self.shape(level)
            self.penup()
            self.goto(0, position_y)
            self.level = level
            self.onclick(self.play_game)

        def play_game(self, x, y):
            if self.level == "easy.gif":
                turtle.clearscreen()
                game_easy.init_game("easy", map_easy)
            elif self.level == "medium.gif":
                turtle.clearscreen()
                game_easy.init_game("medium", map_medium)
            else:
                turtle.clearscreen()
                game_easy.init_game("hard", map_hard)

    # add level
    level_easy = Level(easy, -120)
    level_medium = Level(medium, -170)
    level_hard = Level(hard, -220)

    screen.bgpic("introduction.png")
    screen.title("Maze Game")
    screen.setup(1000, 740)
    screen.tracer(0)


main()
