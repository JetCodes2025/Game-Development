import pgzrun
import random

# --- screen ---
WIDTH  = 1200
HEIGHT = 600

# --- colors ---
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)

# --- actors ---
ship = Actor('galaga')
ship.pos = (WIDTH // 2, HEIGHT - 60)

speed = 5
score = 0

# bullets & enemies
bullets = []
enemies = []

# start with a few enemies
for _ in range(5):
    e = Actor('bug')
    e.x = random.randint(50, WIDTH - 50)
    e.y = random.randint(-300, -100)  # start off-screen above
    enemies.append(e)


# --- UI ---
def displayScore():
    screen.draw.text(str(score), (50, 30), color=WHITE, fontsize=42)


# --- input Shooting bullets ---
def on_key_down(key):
    if key == keys.SPACE:
        b = Actor('bullet') 
        b.x = ship.x
        b.y = ship.y - 50
        bullets.append(b) 
# Game Loop (Update Function)
life = 3
game_over = False
def update(): 
    global score, life, game_over
    #ship movement 
    if keyboard.left:
        ship.x -= speed
    if keyboard.right:
        ship.x += speed
    ship.x = max(0,min(WIDTH, ship.x)) #stops the ship going out of the screen
    #Bullet movement 
    for bullet in bullets[:]:
        if bullet.y <=0:
            bullets.remove(bullet)
        else:
            bullet.y -=10
    #enemy movement and collisions
    for enemy in enemies[:]:
        enemy.y += 5  #enemies will fall down.
        #if enemy reaches to the bottom, reset the bullets position.
        if enemy.y >= HEIGHT:
            enemy.y= -100
            enemy.x = random.randint(50, WIDTH - 50)
        for bullet in bullets[:]: 
            if enemy.colliderect(bullet):
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemy)
            new_e = Actor()  



    


    




