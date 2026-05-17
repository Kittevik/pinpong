from pygame import *
font.init()

back = (200,255,255)
win_height = 650
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

class Ball(GameSprite):
    def __init__(self,filename,x,y,w,h,speed):
        super().__init__(filename,x,y,w,h,speed)
        self.speed_x = self.speed
        self.speed_y = self.speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y > 450 or self.rect.y <0:
            self.speed_y *= -1
        
        if self.rect.colliderect(rocket_l) or self.rect.colliderect(rocket_r):
            self.speed_x *= -1
            self.speed_y *= -1
        


rocket_l = Player("platform_v0.png",50,200,50,200,5)
rocket_r = Player("platform_v0.png",600,200,50,200,5)
ball = Ball('ball_p.png',350,200,70,70,5)

font1 = font.Font(None,40)
txt = font1.render('Score:',True,(0,0,0))
txt_l = font1.render('0',True,(0,0,0))
txt_r = font1.render('0',True,(0,0,0))

window.blit(txt_l,(50,50))
window.blit(txt_r,(650,50))

score_l = 0
score_r = 0




clock = time.Clock()
FPS =60
game = True

while game:
    window.fill(back)
    window.blit(txt_l,(20,30))
    window.blit(txt_r,(550,40))
    window.blit(txt,(20,10))
    window.blit(txt,(550,20))
    rocket_l.reset()
    rocket_r.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    if ball.rect.x <0:
        score += 1
        txt_r = font1.render(str(score_r),True,(0,0,0))
        ball.rect.x = 350
        ball.rect.y = 200
        ball.speed_x *= -1

    if ball.rect.x > 670:
        score_l += 1
        txt_l = font1.render(str(score_l),True,(0,0,0))
        ball.rect.x = 350
        ball.rect.y = 200
        ball.speed_x *= -1

    rocket_l.update_l()
    rocket_r.update_r()
    ball.update()

    display.update()
    clock.tick(FPS)