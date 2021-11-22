import pygame
from pygame import mixer
from src.PyGameAssets import PyGameImage, PyGameFont
from entities.entities import Alien
import math
from numpy import random

pygame.init()

## Asset loading
icon = pygame.image.load("assets/001-alien-pixelated-shape-of-a-digital-game.png")

# Font/Text Renderer
score_display = PyGameFont()
score_display.start_coords(45, 7)

# Spaceship
spaceship = PyGameImage("assets/001-spaceship.png")
spaceship.start_coords(370, 480)
spaceship.set_boundary(x_lower=0, x_upper=736)
spaceship.speed = 0

# Bullet
_bullet = pygame.image.load("assets/001-bullet.png")
bullet = PyGameImage("assets/001-bullet.png")
bullet.start_coords(0, 480)  # off screen
bullet.speed = -1.5
bullet.state = False  # Bullet is not fired yet/Not rendered on screen
bullet.start_x_on_fire = 490  # Starting position of the bullet once rendered

# Alien
no_of_aliens = 10
aliens = []
for alien in range(no_of_aliens):
    aliens.append(Alien())
# alien = Alien()

# Background
background = PyGameImage("assets\pf-s96-pm-0042-01.jpg")
background.start_coords(-200,-200)

# Background Music
mixer.music.load('assets/background.wav')
mixer.music.play(-1)

## Set display size, window name, and window icon
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("SpaceInvaders")
pygame.display.set_icon(icon)

## Game Score
score = 0

## collision Detection
def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt((math.pow(alienX - bulletX, 2))
    + (math.pow(alienY - bulletY, 2)))
    while distance < 27:
        return True
    return False

## Game Over Function
game_over_display = PyGameFont(size=64)
game_over_display.start_coords(200, 250)


## Run Game
game_over = False
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

            # bullet firing (only when bullet is not rendered)
            if event.key == pygame.K_SPACE:
                if bullet.state == False:
                    bullet.state = True
                    bullet_sound = mixer.Sound('assets/laser.wav')
                    bullet_sound.play()
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
    for alien in aliens:
        alien.move_to_player()
        ## Game Over
        if alien.y > 440:
            if alien.y < 2000:
                for alien in aliens:
                    alien.start_coords(alien.x, alien.y + 2000)
            game_over = True
            break

    # Draw/Render Assets
    background.render(screen)
    spaceship.render(screen)
    for alien in aliens:
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
    for alien in aliens:
        collision = isCollision(alien.x, alien.y, bullet.x, bullet.y)
        if collision:
            bullet.state = False
            explosion_sound = mixer.Sound('assets/explosion.wav')
            explosion_sound.play()
            bullet.start_coords(0, bullet.start_x_on_fire)
            score += 1
            alien.respawn()

    if game_over:
        game_over_display.render(screen, "GAME OVER")
    score_display.render(screen, f"Score: {score}")
    pygame.display.update()

    pass
