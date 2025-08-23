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
game_over= False
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
    screen.draw.text("Score: {}".format(str(score)), (50, 30), color=WHITE, fontsize=42)
def lives():
    screen.draw.text("Lives Remaining:  {}".format(str(life)), (800, 30), color=WHITE, fontsize=42)



# --- input ---
def on_key_down(key):
    if key == keys.SPACE:
        b = Actor('bullet')
        b.x = ship.x
        b.y = ship.y - 50
        bullets.append(b)

life =3 #remaining lives
# --- game loop ---
def update():
    global score, life,game_over

    # move the ship
    if keyboard.left:
        ship.x -= speed
    if keyboard.right:
        ship.x += speed
    ship.x = max(0, min(WIDTH, ship.x))  # clamp to screen

    # move bullets (iterate over a copy so we can remove safely)
    for bullet in bullets[:]:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    # move enemies and handle collisions
    for enemy in enemies[:]:
        enemy.y += 5

        # recycle enemy when it exits the bottom
        if enemy.y >= HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(50, WIDTH - 50)

        # check collision with any bullet
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemy)
                # spawn a new enemy at the top to keep action going
                new_e = Actor('bug')
                new_e.x = random.randint(50, WIDTH - 50)
                new_e.y = random.randint(-300, -100)
                enemies.append(new_e)
                break  # this enemy is gone; stop checking it
        #check in for the collision with the ship
        if enemy.colliderect(ship):
            life = life -1
            enemies.remove(enemy)
            #respawn the enemy 
            new_e= Actor("bug")
            new_e.x= random.randint(50, WIDTH - 50)
            new_e.y =random.randint(-300, -100)
            enemies.append(new_e)
            if life <=0:
                game_over = True

        

# --- draw ---
def draw():
    screen.clear()
    screen.fill(BLUE)

    if game_over:
        screen.draw.text("Game Over", center=(WIDTH//2, HEIGHT//2), color="white",fontsize=60)
        screen.draw.text("Final score {}".format(score), center=(WIDTH//2,HEIGHT//2 + 80),color="white", fontsize=60)
        
    else:
        for bullet in bullets:
            bullet.draw()
        for enemy in enemies:
            enemy.draw()

        ship.draw()
        displayScore()
        lives()
pgzrun.go()