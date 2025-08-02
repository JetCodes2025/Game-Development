import pgzrun
from random import randint
#pygame standard for adding the title and with height of the game screen.
TITLE="Shoot The Alien"
#screen setup 
WIDTH=500
HEIGHT=500
#variable to store a message 
message=" "
score=0
#adding the character 
alien=Actor('alien') 
alien.pos=60,60
#function to update the screen 
def draw():
    screen.clear()
    screen.fill((128,0,128))
    #place the actor 
    alien.draw()
    screen.draw.text(message,center=(400,100),fontsize=35)
    screen.draw.text("Score " +str(score),center=(100,100),fontsize=35)
#place the alien randomly on the screen
def place_alien():
    alien.x = randint(50,WIDTH-50)
    alien.y = randint(50,HEIGHT-50)
#mouse event 
def on_mouse_down(pos):
    global message 
    global score
    if alien.collidepoint(pos):
        message="Good Shot"
        score +=2
        place_alien()
    else:
        message="You Missed"
place_alien()
pgzrun.go()
#more code add timer, Add a score counter 🧮

# Add a timer ⏲️

# Add a sound effect 🔊


    

