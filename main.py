from pygame import *

back = (200,255,255)
win_height = 500
win_width = 700
window = display.set_mode((win_width,win_height))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self,filename,x,y,w,h,speed):
        self.image = transform.scale(image.load(filename),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 480:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 480:
            self.rect.y += self.speed

rocket_l = Player("platform_v0.png",50,200,50,200,5)
rocket_r = Player("platform_v0.png",600,200,50,200,5)
ball = GameSprite('ball_p.png',350,200,70,70,5)

clock = time.Clock()
FPS =60
game = True

while game:
    window.fill(back)
    rocket_l.reset()
    rocket_r.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False

    rocket_l.update_l()
    rocket_r.update_r()


    display.update()
    clock.tick(FPS)