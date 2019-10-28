from asciimatics.screen import Screen
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene


def display(screen):
    effects = [
        Cycle(
            screen,
            FigletText("WELCOME TO", font='big'),
            int(screen.height / 2 - 8)),
        Cycle(
            screen,
            FigletText("PYCON!", font='big'),
            int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])



def demo():
    Screen.wrapper(display)
