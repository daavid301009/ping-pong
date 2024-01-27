from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 345:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed 
font.init() 
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))  
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))
back = (80, 38, 167)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
ball = GameSprite('мячик.png', 200, 200, 50, 50, 5)
racket_l = Player('ракетка.png', 30, 200, 50, 150, 4)
racket_r = Player('ракетка.png', win_width - 80, 200, 50, 150, 4)
game = True
finish = False
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if ball.rect.x < 50:
            finish = True
            window.blit(lose1, (200,200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200,200))
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 50  or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            speed_x *= -1
        window.fill(back)
        racket_l.update_l()
        racket_r.update_r()
        ball.reset()
        racket_l.reset()
        racket_r.reset()
    display.update()
    clock.tick(FPS) 