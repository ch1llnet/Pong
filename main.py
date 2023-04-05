from pygame import *
from random import randint

font.init()
mixer.init()
clock = time.Clock()

w = 700
h = 500
s_x = 3
s_y = 3

win = display.set_mode((700, 500))

display.set_caption('Pong')
bg = transform.scale(image.load('SQui.jpg'), (700, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 490:
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 490:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global rand, s_x, s_y
        self.rect.x -= s_x
        self.rect.y -= s_y
        if sprite.collide_rect(astron1, potato):
            s_x *= -1
            s_y *= -1
            if rand == 1:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed

        if sprite.collide_rect(astron2, potato):
            s_x *= -1
            s_y *= -1
            if rand == 1:
                self.rect.y += self.speed
            else:
                self.rect.y -= self.speed

        if self.rect.y >= 460 or self.rect.y <= 20:
            self.rect.y *= -1






astron1 = Player('racket.png', 10, 250, 5)
astron2 = Player('racket.png', 640, 250, 5)
potato = Ball('ball-tr.png', 350, 250, 3)



font = font.Font(None, 70)
wins = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (255, 0, 0))

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        win.blit(bg, (0, 0))

        #potato.rect.x += s_x
        #potato.rect.y += s_y

        astron1.update()
        astron1.reset()

        astron2.update2()
        astron2.reset()

        potato.update()
        potato.reset()


    rand = randint(1, 2)

   # elif wins >= 10:
        # win.blit(wins, (200, 200))
        #finish = True

    display.update()
    clock.tick(120)
