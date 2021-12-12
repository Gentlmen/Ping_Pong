from pygame import *
from random import randint

score = 0 
lost = 0 
 
win_width = 700
win_height = 500
display.set_caption("Ping_Pong")
window = display.set_mode((win_width, win_height))

class GameSprite(sprite.Sprite):
 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
       
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

class Enemy(GameSprite):
   
    def update(self):
        self.rect.y += self.speed
        global lost
       
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

while run:
   
    for e in event.get():
        if e.type == QUIT:
            run = False