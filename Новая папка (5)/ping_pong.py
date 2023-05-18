from pygame import *
font.init()
back = (200, 255, 255)
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def __init__(self,player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__(player_image, player_x, player_y, player_width, player_height)
        self.speed = player_speed
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 345:
            self.rect.y += self.speed

class Player2(GameSprite):
    def __init__(self,player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__(player_image, player_x, player_y, player_width, player_height)
        self.speed = player_speed
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 20:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed
class Ball(GameSprite):
    def update(self):
        global speed_x
        global speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 480 or ball.rect.y<0:
            speed_y *= -1
        if sprite.collide_rect(ball, rocets1) or sprite.collide_rect(ball, rocets2):
            speed_x *= -1
window = display.set_mode((700, 500))
display.set_caption("Ping Pong")
clock = time.Clock()
speed_x = 2
speed_y = 2
window.fill(back)
rocets1 = Player1('rocets.png', 40, 250, 30, 150, 3)
rocets2 = Player2('rocets.png', 660, 250, 30, 150, 3)
ball = Ball('ball.png', 350, 250, 50, 50)
game = True
finish = False
font = font.Font(None, 60)
lose1 = font.render('PLAYER 1 LOSE!', True, (255, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (255, 0, 0))
FPS = 50
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        rocets1.update_1()
        rocets2.update_2()
        ball.update()
        rocets1.reset()
        rocets2.reset()
        ball.reset()
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (350, 250))
    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (350, 250))
    clock.tick(FPS)
    display.update()