import pygame

pygame.init()

def clamp(value: int | float, min: int | float, max: int | float):
    if value > max:
        return max
    elif value < min:
        return min
    return value

def render(text,coords,colour, font, align="center"):
    """align defaults to center if no arguments given\n
    Align options:\n
    center, left, right, topleft, topright
    """
    screen = pygame.display.get_surface()
    surface = font.render(text,False,colour)
    if align == "center":
        rectangle = surface.get_rect(center = coords)
    elif align == "left":
        rectangle = surface.get_rect(midleft = coords)
    elif align == "right":
        rectangle = surface.get_rect(midright = coords)
    elif align == "topleft":
        rectangle = surface.get_rect(topleft = coords)
    elif align == "topright":
        rectangle = surface.get_rect(topright = coords)
    else:
        raise Exception()
    screen.blit(surface, rectangle)