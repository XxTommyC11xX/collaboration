import pygame, tools
import player as player_module
from sys import exit as sysexit

pygame.init()

WIDTH, HEIGHT = 800, 800
CENTERX, CENTERY = WIDTH/2, HEIGHT/2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collaborative project")
clock = pygame.time.Clock()

player = player_module.Player((CENTERX, CENTERY))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sysexit()

    player.update()

    pygame.display.update()
    clock.tick(60)
