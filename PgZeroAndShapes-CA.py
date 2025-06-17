# import pgzrun
# from pygame import Rect
# from random import randint

# WIDTH = 300
# HEIGHT = 300

# def draw():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)

#     width = WIDTH
#     height = HEIGHT - 200

#     for i in range(20):
#         rect = Rect((0, 0), (width, height))
#         rect.center = 150, 150
#         screen.draw.rect(rect, (r, g, b))

#         r = max(0, r - 10)
#         g = min(255, g + 10)

#         width -= 10
#         height += 10

# pgzrun.go()

import pgzrun
from random import randint
from pygame import Rect
WIDTH = 300
HEIGHT = 300

def draw():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    width  = WIDTH
    height = HEIGHT - 200
    for i in range(20):
        rect = Rect((0,0),(width,height))
        rect.center = 150,150
        screen.draw.rect(rect,(r,g,b))


        r = max(0, r - 10)
        g = min(255, g + 10)

        width -= 10
        height += 10
pgzrun.go()
