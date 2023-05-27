import pygame as pg
from sys import exit as sysexit
pg.init()

# Screen
screen = pg.display.set_mode((800,800))
SCREEN_WIDTH,SCREEN_HEIGHT = screen.get_width(),screen.get_height()
pg.display.set_caption("crappy ripoff Zelda")
MID_SCREEN = SCREEN_WIDTH / 2
bg_img = pg.image.load("ground.png").convert_alpha()

# Clock
clock = pg.time.Clock()

# Functions
def clamp(value: int | float, min: int | float, max: int | float):
    if value > max:
        return max
    elif value < min:
        return min
    return value

def render(text: str, coords: tuple[int, int], colour, font: pg.font.Font, align: str ="center"):
    """align defaults to center if no arguments given\n
    Align options:\n
    center, left, right, topleft, topright
    """
    screen = pg.display.get_surface()
    surface: pg.Surface = font.render(text,False,colour)
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

# Sprites

link_img = pg.transform.scale(pg.image.load("link/link.jpg").convert_alpha(), (50,50))

up = []
down = []
left = []
right = []

up_attack = []
down_attack = []
left_attack = []
right_attack = []

for sprite in range(0,9): up.append(pg.transform.scale(pg.image.load(f"link/move_up/move_up{sprite}.png").convert_alpha(),(50,50)))
for sprite in range(0,9): down.append(pg.transform.scale(pg.image.load(f"link/move_down/move_down{sprite}.png").convert_alpha(),(50,50)))
for sprite in range(0,9): left.append(pg.transform.scale(pg.image.load(f"link/move_side/move_side{sprite}.png").convert_alpha(),(50,50)))
for sprite in range(0,9): right.append(pg.transform.scale(pg.transform.flip(pg.image.load(f"link/move_side/move_side{sprite}.png").convert_alpha(),True,False),(50,50)))

for sprite in range(0,5): up_attack.append(pg.transform.scale(pg.image.load(f"link/attack-up/attack-up{sprite}.png").convert_alpha(),(50,50)))
for sprite in range(0,5): down_attack.append(pg.transform.scale(pg.image.load(f"link/attack-down/attack-down{sprite}.png").convert_alpha(),(50,50)))
for sprite in range(0,5): left_attack.append(pg.transform.scale(pg.image.load(f"link/attack-side/attack-side{sprite}.png").convert_alpha(),(50,50)))
for sprite in range(0,5): right_attack.append(pg.transform.scale(pg.transform.flip(pg.image.load(f"link/attack-side/attack-side{sprite}.png").convert_alpha(),True,False),(50,50)))

class Player():
    def __init__(self):
        self.image = pg.transform.scale(link_img,(50,50)) 
        self.rect = self.image.get_rect(center = (MID_SCREEN,MID_SCREEN))
        self.direction = "d"
        self.ani_index = 0

    def movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_w] or key[pg.K_UP]:
            self.direction = "u"
            self.rect.y -= 5
            self.ani_index += 0.2
        elif key[pg.K_s] or key[pg.K_DOWN]:
            self.direction = "d"
            self.rect.y += 5
            self.ani_index += 0.2
        elif key[pg.K_a] or key[pg.K_LEFT]:
            self.direction = "l"
            self.rect.x -= 5
            self.ani_index += 0.2
        elif key[pg.K_d] or key[pg.K_RIGHT]:
            self.direction = "r"
            self.rect.x += 5
            self.ani_index += 0.2
        else:
            self.image = link_img
            self.ani_index = 0

    def keep_in_bounds(self):
        self.rect.x = clamp(self.rect.x, 0, SCREEN_WIDTH-self.rect.width)
        self.rect.y = clamp(self.rect.y, 0, SCREEN_HEIGHT-self.rect.height)

    def animation(self):
        if self.ani_index >= 9:
            self.ani_index = 0
        if self.direction == "u":
            self.image = up[int(self.ani_index)]
        elif self.direction == "d":
            self.image = down[int(self.ani_index)]
        elif self.direction == "l":
            self.image = left[int(self.ani_index)]
        elif self.direction == "r":
            self.image = right[int(self.ani_index)]

    def update(self):
        self.animation()
        self.movement()
        self.keep_in_bounds()
        screen.blit(self.image,self.rect)

# Instances
player = Player()

# Game Loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sysexit()

    screen.blit(bg_img, (0,0))
    player.update()

    pg.display.update()
    clock.tick(60)
