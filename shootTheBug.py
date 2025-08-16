import pgzrun
import random

# screen dimensions
WIDTH = 1200
HEIGHT = 600

# defining colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# create a ship and one enemy (optional single bug, not used)
ship = Actor('galaga')
bug = Actor('bug')
ship.pos = (WIDTH // 2, HEIGHT - 60)

# speed of the ship
speed = 5

# define a list for bullets and enemies
bullets = []
enemies = []

# starting score
score = 0

# add one starting enemy
enemies.append(Actor('bug'))
enemies[-1].x = 10
enemies[-1].y = -100  # starts off-screen

# KEY PRESS EVENT - fire bullet when space is pressed
def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('bullet'))
        # place bullet at ship's current position
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50

# MAIN UPDATE FUNCTION
def update():
    global score

    # Move ship left or right
    if keyboard.left:
        ship.x -= speed
        if ship.x <= 0:
            ship.x = 0
    elif keyboard.right:
        ship.x += speed
        if ship.x >= WIDTH:
            ship.x = WIDTH

    # Update bullets
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)  # remove off-screen bullets
        else:
            bullet.y -= 10

    # Update enemies
    for enemy in enemies:
        enemy.y += 5

        # if enemy reaches bottom, reset to top
        if enemy.y >= HEIGHT:
            enemy.y = -100
            enemy.x = random.randint(50, WIDTH - 50)

        # check for collision with bullets
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemy)
                break  # avoid modifying list while looping

# DRAW FUNCTION
def draw():
    screen.clear()
    screen.fill(BLUE)

    # draw all bullets
    for bullet in bullets:
        bullet.draw()

    # draw all enemies
    for enemy in enemies:
        enemy.draw()

    # draw ship last (on top)
    ship.draw()

    # display the score
    displayScore()

# DISPLAY SCORE FUNCTION
def displayScore():
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=40, color=WHITE)

pgzrun.go()
