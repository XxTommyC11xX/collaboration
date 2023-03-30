import pygame, tools

pygame.init()

class Player:
    def __init__(self, pos: tuple[int, int]) -> None:
        self.image = pygame.Surface()
        self.rect = self.image.get_rect(center = pos)
        self.screen = pygame.display.get_surface()
        self.velocity = pygame.Vector2(0,0)
        self.speed = 5
        self.termvel = 50

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.velocity.y -= self.speed
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.velocity.x -= self.speed
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.velocity.y += self.speed
        elif keys[pygame.K_d] or keys[pygame.K_DOWN]:
            self.velocity.x += self.speed

    def movement(self):
        self.rect.center += self.velocity
        self.velocity.x = tools.clamp(self.velocity.x, -self.termvel, self.termvel)
        self.velocity.y = tools.clamp(self.velocity.y, -self.termvel, self.termvel)


    def update(self) -> None:
        self.screen.blit(self.image, self.rect)
        self.get_input()
        self.movement()
