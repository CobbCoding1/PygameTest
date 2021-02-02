import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('space-ship.png')
playerX = 608
playerY = 650
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_a):
                playerX_change = -0.5
            elif(event.key == pygame.K_d):
                playerX_change = 0.5

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_a or event.key == pygame.K_d):
                playerX_change = 0

    playerX += playerX_change

    if(playerX <= 0):
        playerX = 0
    elif(playerX >= 1248):
        playerX = 1248

    player(playerX, playerY)
    pygame.display.update()
