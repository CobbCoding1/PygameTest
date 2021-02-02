import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1280, 720))

background = pygame.image.load('background.png')

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('space-ship.png')
playerX = 608
playerY = 650
playerX_change = 0

enemyImg = pygame.image.load('space-ship.png')
enemyX = random.randint(0, 1248)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

bulletImg = pygame.image.load('space-ship.png')
bulletX = 0
bulletY = 650
bulletX_change = 0
bulletY_change = 40
bullet_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

running = True

while running:
    screen.fill((0, 0, 0))

    screen.blit(background, (250, 60))

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False

        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_a):
                playerX_change = -5
            elif(event.key == pygame.K_d):
                playerX_change = 5

        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_a or event.key == pygame.K_d):
                playerX_change = 0

    playerX += playerX_change

    if(playerX <= 0):
        playerX = 0
    elif(playerX >= 1248):
        playerX = 1248

    enemyX += enemyX_change

    if(enemyX <= 0):
        enemyX_change = 4
        enemyY += enemyY_change
    elif(enemyX >= 1248):
        enemyX_change = -4
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
