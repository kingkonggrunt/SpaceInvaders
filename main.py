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

## Run Game
running = True
while running:
    for event in pygame.event.get():
        ## Quit Game
        if event.type == pygame.QUIT:
            running = False

        ## Moving spaceship with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceship.speed = -0.3
            if event.key == pygame.K_RIGHT:
                spaceship.speed = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                spaceship.speed = 0

    ## Set Background Fill (RGB). Interacts with pygame.display.update()
    screen.fill((255, 255, 255))

    ## Move and Draw Assets
    background.move(axis=1, amount=random.normal(0, 0.009))
    background.move(axis=0, amount=random.normal(0, 0.009))

    spaceship.move(axis=1, amount=spaceship.speed)

    # Move the alien down as it hits the boundaries moving left and right
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

    pygame.display.update()

    pass
