import pygame

pygame.init()

# Asset loading
icon = pygame.image.load("assets/001-alien-pixelated-shape-of-a-digital-game.png")
spaceship = pygame.image.load("assets/001-spaceship.png")
alien = pygame.image.load("assets\001-alien-pixelated-shape-of-a-digital-game.png")

# Set display size, window name, and window icon
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("SpaceInvaders")
pygame.display.set_icon(icon)


# Starting Cooridinates of the Spaceship
spaceshipX = 370
spaceshipY = 480

# Starting Coordinates of the alien
alienX = None
alienY = None

# Spaceship movement
X_offset = 0 

# Alien movement
X_offset_alien = 0

# def player():
#     screen.blit(spaceship, (spaceshipX, spaceshipY))

# Run Game
running = True
while running:
    for event in pygame.event.get():
        # Quit Game
        if event.type == pygame.QUIT:
            running = False

        # Keystroke detection
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_offset = -0.1
            if event.key == pygame.K_RIGHT:
                X_offset = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                X_offset = 0

    # Set Background Fill (RGB). Interacts with pygame.display.update()
    screen.fill((255, 255, 255))

    # Draw Shipship
    spaceshipX += X_offset

    # Setting shipship boundary
    if spaceshipX <= 0:
        spaceshipX = 0
    elif spaceshipX >= 736:
        spaceshipX = 736
    screen.blit(spaceship, (spaceshipX, spaceshipY))

    pygame.display.update()

    pass
