from pygame import *
from random import randint
 
 
 
mixer.init()
mixer.music.load('space.mp3')
mixer.music.play()
 
 
font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)
 
 
img_back = "galaxy.jpg" 
img_hero = "platform.jpg"
img_enemy = "mach.jpg"

win_width = 1000
win_height = 700
display.set_caption("Ping_Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

class GameSprite(sprite.Sprite):
 
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       
        sprite.Sprite.__init__(self)
 
       
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
       
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

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

run = True 
while run:
   
    for e in event.get():
        if e.type == QUIT:
            run = False
