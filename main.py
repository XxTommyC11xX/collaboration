import pygame
from sys import exit as sysexit

pygame.init()

WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Collaborative project")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sysexit()

    # act like I added something new here

    pygame.display.update()
    clock.tick(60)
