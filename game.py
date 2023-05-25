import pygame as pg
from sys import exit as sysexit
pg.init()

# Screen
screen = pg.display.set_mode((800,800))
SCREEN_WIDTH,SCREEN_HEIGHT = screen.get_width(),screen.get_height()
pg.display.set_caption("")
MID_SCREEN = SCREEN_WIDTH / 2

# Clock
clock = pg.time.Clock()

# Sprites
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
        self.image = pg.transform.scale(pg.image.load("link/link.jpg").convert_alpha(),(50,50)) 
        self.rect = self.image.get_rect(center = (MID_SCREEN,MID_SCREEN))
        self.direction = "d"
        self.ani_index = 0

    def movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            self.direction = "u"
            self.rect.y -= 5
            self.ani_index += 0.2
        elif key[pg.K_s]:
            self.direction = "d"
            self.rect.y += 5
            self.ani_index += 0.2
        elif key[pg.K_a]:
            self.direction = "l"
            self.rect.x -= 5
            self.ani_index += 0.2
        elif key[pg.K_d]:
            self.direction = "r"
            self.rect.x += 5
            self.ani_index += 0.2

    def animation(self):
        if self.ani_index >= 9: self.ani_index = 0
        
        if self.direction == "u":
            self.image = up[int(self.ani_index)]
        elif self.direction == "d":
            self.image = down[int(self.ani_index)]
        elif self.direction == "l":
            self.image = left[int(self.ani_index)]
        elif self.direction == "r":
            self.image = right[int(self.ani_index)]

    def update(self):
        self.movement()
        self.animation()
        
        screen.blit(self.image,self.rect)

# Instances
player = Player()

# Game Loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sysexit()

    screen.fill("black")
    player.update()

    pg.display.update()
    clock.tick(60)  