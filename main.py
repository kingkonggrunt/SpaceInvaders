import pygame
from src.PyGameAssets import PyGameImage
from random import randint
from numpy import random

pygame.init()

## Asset loading
icon = pygame.image.load("assets/001-alien-pixelated-shape-of-a-digital-game.png")

# Spaceship
spaceship = PyGameImage("assets/001-spaceship.png")
spaceship.start_coords(370, 480)
spaceship.set_boundary(x_lower=0, x_upper=736)
spaceship.speed = 0

# Bullet
_bullet = pygame.image.load("assets/001-bullet.png")
bullet = PyGameImage("assets/001-bullet.png")
bullet.start_coords(0, 480)  # off screen
bullet.speed = -0.5
bullet.state = False  # Bullet is not fired yet/Not rendered on screen
bullet.start_x_on_fire = 490  # Starting position of the bullet once rendered

# Alien
alien = PyGameImage("assets/001-alien-pixelated-shape-of-a-digital-game.png")
alien.start_coords(randint(0,736), randint(50,150))
alien.set_boundary(x_lower=0, x_upper=736)
alien.speed = 0.20
alien.step_down = 8

# Background
background = PyGameImage("assets\pf-s96-pm-0042-01.jpg")
background.start_coords(-200,-200)


## Set display size, window name, and window icon
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("SpaceInvaders")
pygame.display.set_icon(icon)

def fire_bullet(bullet, x, y):
    bullet.state = True
    screen.blit(_bullet, (x + 16), (y + 10))
    # bullet.render(screen)
## Game Score
score = 0

## collision Detection
def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt((math.pow(alienX - bulletX, 2))
    + (math.pow(alienY - bulletY, 2)))
    while distance < 27:
        return True
    return False


## Run Game
running = True
while running:
    for event in pygame.event.get():


        ## Quit Game
        if event.type == pygame.QUIT:
            running = False


        ## Keystroke Detection
        if event.type == pygame.KEYDOWN:
            # Moving spaceship with arrow keys
            if event.key == pygame.K_LEFT:
                spaceship.speed = -0.3
            if event.key == pygame.K_RIGHT:
                spaceship.speed = 0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    spaceship.speed = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                spaceship.speed = 0

            # bullet firing (only when bullet is not rendered)
            if event.key == pygame.K_SPACE:
                if bullet.state == False:
                    bullet.state = True
                    bullet.start_coords(spaceship.x + 16, bullet.start_x_on_fire)
                    bullet.render(screen)


    ## Set Background Fill (RGB). Interacts with pygame.display.update()
    screen.fill((255, 255, 255))


    ## Move and Draw Assets
    background.move(axis=1, amount=random.normal(0, 0.008))
    background.move(axis=0, amount=random.normal(0, 0.008))
    spaceship.move(axis=1, amount=spaceship.speed)

    # Alien movement. Once the alien has reach on of it's x boundaries. Flip the direction
    # That the alien goes in the x direction and move the alien downwards.
    alien.move(axis=1, amount=alien.speed)
    if alien.x == alien.x_bound_upper:
        alien.speed = alien.speed/-1
        alien.move(axis=0, amount=alien.step_down)
    if alien.x == alien.x_bound_lower:
        alien.speed = alien.speed/-1
        alien.move(axis=0, amount=alien.step_down)


    # Draw/Render Assets
    background.render(screen)
    spaceship.render(screen)
    alien.render(screen)


    # Bullet movement. When the bullet has left the screen, reset the position.
    # If the bullet is "rendered". Increase the y coordinate of bullet and rerendered
    if bullet.y < 0 :
        bullet.state = False
        bullet.start_coords(0, bullet.start_x_on_fire)
    if bullet.state is True:
        bullet.start_coords(bullet.x, bullet.y)
        bullet.render(screen)
        bullet.y += bullet.speed


    ## Bullet and Alien Collsion. Reset bullet, add score and remove alien.
    collision = isCollision(alien.x, alien.y, bullet.x, bullet.y)
    if collision:
        bullet.state = False
        bullet.start_coords(0, bullet.start_x_on_fire)
        score += 1
    pygame.display.update()

    pass
