import pgzrun 
from random import randint
WIDTH=600
HEIGHT=500
score=0
game_over=False

# bee object
bee=Actor("bee")
bee.pos=100,100

#flower object 
flower=Actor("flower")
flower.pos=200,200

#draw function 
def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    #screen.draw.text("Welcome To bumblebee and Flower Game ", color="black", center=(10,10))
    screen.draw.text("Score : "+ str(score), color="black", topleft=(10,10))
    if game_over:
        screen.fill("pink")
        screen.draw.text("Time's Up!! Your final score is: "+str(score), midtop=(WIDTH/2,10), fontsize=40, color="red")
#function to move the flower on the screen.
def place_flower():
    flower.x=randint(70, (WIDTH-70))
    flower.y=randint(70, (HEIGHT-70))
def times_up():
    global game_over
    game_over=True
#game update 
def update():
    global score 
    if keyboard.left:
        bee.x = bee.x- 3
    if keyboard.right:
        bee.x= bee.x + 3
    if keyboard.up:
        bee.y = bee.y - 3
    if keyboard.down:
        bee.y=bee.y + 3
    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score = score + 10
        place_flower()
clock.schedule(times_up, 60.0)
pgzrun.go()    







