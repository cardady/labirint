from pygame import *
'''Необходимые классы'''

#класс-родитель для спрайтов
class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

        
    def draw_wall(self):

        window.blit(self.image, (self.rect.x, self.rect.y))


class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
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
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    direction = "up"
    def update(self):
        if self.rect.y <=10:
            self.direction = "down"
        if self.rect.y >= win_height - 85:
            self.direction = "up"

        if self.direction == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Enemy3(GameSprite):
    direction = "up"
    def update(self):
        if self.rect.y <=30:
            self.direction = "down"
        if self.rect.y >= win_height - 85:
            self.direction = "up"

        if self.direction == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

 
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("pole_bitvi.jpg"), (win_width, win_height))

w1 = Wall(110, 36, 185, 100, 20, 380, 10)
w2 = Wall(110, 36, 185, 100, 480, 450, 10)
w3 = Wall(110, 36, 185, 100, 20, 10, 380)
w4 = Wall(110, 36, 185, 300, 135, 10, 345)
w5 = Wall(110, 36, 185, 200, 120, 10, 360)
w6 = Wall(110, 36, 185, 100, 200, 0, 10)
w7 = Wall(110, 36, 185, 300, 135, 70, 10)
w8 = Wall(110, 36, 185, 370, 135, 10, 50)
w9 = Wall(110, 36, 185, 470, 20, 10, 100)
w10 = Wall(110, 36, 185, 470, 100, 10, 170)
w11 = Wall(110, 36, 185, 410, 270, 70, 10)
w13 = Wall(110, 36, 185, 400, 270, 10, 100)
w14 = Wall(110, 36, 185, 540, 380, 10, 100)
w15 = Wall(110, 36, 185, 510, 380, 80, 10)


 
#Персонажи игры:
player = Player('hhero.png', 5, win_height - 80, 4)
monster = Enemy('ohranik1.png', win_width - 80, 280, 2)
monster2 = Enemy2('ohranik2.png', win_width - 80, 280, 4)
monster3 = Enemy3('ohranik2.png', win_width - 470, 100, 10)

final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
 
game = True
finish = False
clock = time.Clock()
FPS = 60
 
font.init()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN!!!', True, (255,215,0))
lose = font.render('YOU LOSE(', True, (180, 0, 0))

#музыка
mixer.init()
mixer.music.load('Fonk.ogg')
mixer.music.play(-1)
mixer.music.set_volume(0.2)
mixer.music.play()
kick = mixer.Sound('kick.ogg')
kick.set_volume(0.1)
money = mixer.Sound('money.ogg')
kick.set_volume(0.1)
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()
        monster2.update()
        monster3.update()
        

        player.reset()
        monster.reset()
        monster2.reset()
        monster3.reset()
        
        final.reset()
        
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()





        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, monster2) or sprite.collide_rect(player, monster3) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11) or sprite.collide_rect(player, w13) or sprite.collide_rect(player, w14) or sprite.collide_rect(player, w15):
            finish = True
            window.blit(lose, (200, 200))
            kick.play()
        
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200, 200))
            money.play()

    display.update()
    clock.tick(FPS)

