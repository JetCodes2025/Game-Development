import pgzrun
from random import randint
#pygame standards for deciding the title of your game window. 
TITLE = "Game Shoot"
#set teh width and height of the game screen 
WIDTH = 500
HEIGHT = 500
#variable to store a message displayed on the screen.
message = " "
#adding actor to the game 
alien = Actor('alien.png')
alien.pos = 50,50

#default function which will be called to update the screen
def draw():
    #screen is an another bulit-in object.
    screen.clear()
    screen.fillcolor=(128,0,0)
#place the actor 
    alien.draw()
    screen.draw.text(message, center = (400,100), fontsize = 30)
#place the alien 
def place_alien():
    alien.x = randint(50, WIDTH-50)
    alien.y = randint(50, HEIGHT-50)
def mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot"
        place_alien()
    else:
        message = "You missed"
place_alien()
pgzrun.go()
        
