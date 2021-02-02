import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('space-ship.png')
pygame.display.set_icon(icon)

running = True

while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False


    screen.fill((0, 0, 255))
    pygame.display.update()
