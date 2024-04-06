#Создай собственный Шутер!
from pygame import *
from random import randint
font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 36)
font.init()
font = font.Font(None, 70)
win = font.render('sdasd', True, (255, 215, 0))
lose = font.render('dasdd', True, (180, 0, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, image1, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(image1), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Bullet(GameSprite):
    def __init__(self, image1, speed, x, y):
        super().__init__(image1, speed, x, y)
        


        
        self.image = transform.scale(image.load(image1), (10, 15))
    def update (self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
class Bomba(GameSprite):
    def __init__(self, image1, speed, x, y,):
        super().__init__(image1, speed, x, y)
        


        
        self.image = transform.scale(image.load(image1), (50, 50))
    def update (self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 65:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 65:
            self.rect.x += self.speed
    def fire(self):

            bullet = Bullet('bullet.png', 10, self.rect.centerx, self.rect.top)
            bullets.add(bullet)
    def bom(self):
            bomba = Bomba('bullet.png', 5, self.rect.centerx, self.rect.top)
            bombas.add(bomba)
            
lost = 0
score = 0
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed + randint(0, 5)
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(0,win_width - 65)
            self.rect.y = 0
            lost = lost + 1

class meteor(GameSprite):
    #класс метеорита
    def update(self):
        global lost 
        self.rect.y
        global lost
        self.rect.y += self.speed + randint(0, 3)
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(0,win_width)
            self.rect.y = 0
            lost = lost + 1
#создай окно игры
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
#сам метеорит
background = transform.scale(image.load('galaxy.jpg'), (win_width, win_height))
clock = time.Clock()
FPS = 60
game = True
finish = False
ship = Player('rocket.png',12, 2,win_height - 100)
asreroid = sprite.Group()
asreroid.add(meteor("asteroid.png", 0, randint(0, win_width - 65),0))
asreroid.add(meteor("asteroid.png", 0, randint(0, win_width - 65),0))
#враги
monsters = sprite.Group()
monsters.add(Enemy("ufo.png", 0, randint(0, win_width - 65),0))
monsters.add(Enemy("ufo.png", 0, randint(0, win_width - 65),0))
monsters.add(Enemy("ufo.png", 0, randint(0, win_width - 65),0))
monsters.add(Enemy("ufo.png", 0, randint(0, win_width - 65),0))
monsters.add(Enemy("ufo.png", 0, randint(0, win_width - 65),0))

bullets = sprite.Group()

bombas = sprite.Group()
#стрелять пулями и бомбами
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
              ship.fire()  
            if e.key == K_q:


                #fire_sound.play()
                

                ship.bom()
    if not finish:
        window.blit(background, (0, 0))
#счёт 
        text = font2.render("Счёт: " + str(score), 1, (255, 255,255))
        window.blit(text, (10, 20))

        text_lose = font2.render("пропушеные: " + str(lost), 1, (255, 255,255))
        window.blit(text_lose, (10, 50))
        sprites_list = sprite.spritecollide(ship, monsters, False)
        collides = sprite.groupcollide(monsters, bullets, True, False)
        sprite.groupcollide(asreroid, bullets, False, True)
        for c in collides:
            score += 1
            monsters.add(Enemy("ufo.png", 0, randint(0, win_width - 65),0))

        cc = sprite.groupcollide(asreroid, bombas, True, False) 
        for c in cc:
            score -= 10
            asreroid.add(meteor("asteroid.png", 0, randint(0, win_width - 65),0))
              
        
        bombas.update()
        bombas.draw(window)
        asreroid.draw(window)
        asreroid.update()
        ship.reset()
        ship.update()
        bullets.update()
        bullets.draw(window)
        monsters.draw(window)
        monsters.update()
        display.update()
        clock.tick(FPS)

















        
        #следуйшие обнова
        # сюжет НЕТУ просто бей всех и всё но бомбами так не пользуйся часто (если будет больше -100)а то на растрел посадит государство
# как начиналось да просто так и всё
# и уменьшу выйгрышь до 100 а сейчас он до 1000000 и потом -1000000
# обновы будут выходить но пока что она в бета версии и (спасибо за внимание)