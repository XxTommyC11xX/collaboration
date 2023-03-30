import pygame

pygame.init()

class Player:
    def __init__(self, pos: tuple[int, int]) -> None:
        self.image = pygame.Surface()
        self.rect = self.image.get_rect(center = pos)
        self.screen = pygame.display.get_surface()

    def update(self) -> None:
        self.screen.blit(self.image, self.rect)