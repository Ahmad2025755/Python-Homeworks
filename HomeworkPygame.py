import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 300))

dice = [
    pygame.image.load("One.jpg"),
    pygame.image.load("images.png"),
    pygame.image.load("3.png"),
    pygame.image.load("4.jpeg"),
    pygame.image.load("5.png"),
    pygame.image.load("6.jpeg")
]

current = dice[random.randint(0, 5)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current = dice[random.randint(0, 5)]  

    screen.fill((255, 255, 255))
    screen.blit(current, (100, 50))
    pygame.display.flip()

pygame.quit()