# import pygame, sys
# from pygame.locals import *
# import random, time

# pygame.init()

# FPS = 60
# FramePerSec = pygame.time.Clock()

# BLUE  = (0, 0, 255)
# RED   = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)

# width = 400
# height = 600
# SPEED = 5
# SCORE = 0 

# font = pygame.font.SysFont("Verdana", 60)
# font_small = pygame.font.SysFont("Verdana", 20)
# game_over = font.render("Game Over", True, BLACK)
 
# background = pygame.image.load("AnimatedStreet.png")

# display_surf = pygame.display.set_mode((width, height))
# display_surf.fill(WHITE)
# pygame.display.set_caption('Racer')


# class Enemy(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load('Enemy.png')
#         self.rect = self.image.get_rect()
#         self.rect.center = (random.randint(40, width-40), 0)

#         def move(self):
#             global SCORE
#             self.rect.move_ip(0, SPEED)
#             if (self.rect.top > 600):
#                 self.rect.top = 0
#             self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load('Player.png')
#         self.rect = self.image.get_rect()
#         self.rect.center = (160, 520)

#     def update(self):
#         pressed_keys = pygame.key.get_pressed()

#         if self.rect.left > 0:
#             if pressed_keys[K_LEFT]:
#                 self.rect.move_ip(-5, 0)
#         if self.rect.right < width:
#             if pressed_keys[K_RIGHT]:
#                 self.rect.move_ip(5, 0)


# P1 = Player()
# E1 = Enemy()

# enemies = pygame.sprite.Group()
# enemies.add(E1)
# all_sprites = pygame.sprite.Group()
# all_sprites.add(P1)
# all_sprites.add(E1)

# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

# while True:
#     for event in pygame.event.get():
#         if event.type == INC_SPEED:
#             SPEED += 0.5
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     display_surf.blit(background, (0,0))
#     scores = font_small.render(str(SCORE), True, BLACK)
#     display_surf.blit(scores, (10,10))
    
#     for entity in all_sprites:
#         display_surf.blit(entity.image, entity.rect)
#         entity.move()

#     if pygame.sprite.spritecollideany(P1, enemies):
#         pygame.mixer.Sound('crash.wav').play()
#         time.sleep(0.5)
                    
#         display_surf.fill(RED)
#         display_surf.blit(game_over, (30,250))
           
#         pygame.display.update()
#         for entity in all_sprites:
#             entity.kill() 
#         time.sleep(2)
#         pygame.quit()
#         sys.exit()     
    
#     pygame.display.update()
#     FramePerSec.tick(FPS)


# import pygame, sys
# from pygame.locals import *
# import random, time

# pygame.init()

# FPS = 60
# FramePerSec = pygame.time.Clock()

# BLUE  = (0, 0, 255)
# RED   = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)

# width = 400
# height = 600
# SPEED = 5
# SCORE = 0 

# font = pygame.font.SysFont("Verdana", 60)
# font_small = pygame.font.SysFont("Verdana", 20)
# game_over = font.render("Game Over", True, BLACK)
 
# background = pygame.image.load("AnimatedStreet.png")

# display_surf = pygame.display.set_mode((width, height))
# display_surf.fill(WHITE)
# pygame.display.set_caption('Racer')


# class Enemy(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load('Enemy.png')
#         self.rect = self.image.get_rect()
#         self.rect.center = (random.randint(40, width-40), 0)

#     def move(self):
#         global SCORE
#         self.rect.move_ip(0, SPEED)
#         if (self.rect.top > 600):
#             self.rect.top = 0
#         self.rect.center = (random.randint(40, width - 40), 0)
        
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load('Player.png')
#         self.rect = self.image.get_rect()
#         self.rect.center = (160, 520)

#     def move(self):
#         pressed_keys = pygame.key.get_pressed()

#         if self.rect.left > 0:
#             if pressed_keys[K_LEFT]:
#                 self.rect.move_ip(-5, 0)
#         if self.rect.right < width:
#             if pressed_keys[K_RIGHT]:
#                 self.rect.move_ip(5, 0)


# P1 = Player()
# E1 = Enemy()

# enemies = pygame.sprite.Group()
# enemies.add(E1)
# all_sprites = pygame.sprite.Group()
# all_sprites.add(P1)
# all_sprites.add(E1)

# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

# while True:
#     for event in pygame.event.get():
#         if event.type == INC_SPEED:
#             SPEED += 0.5
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     display_surf.blit(background, (0,0))
#     scores = font_small.render(str(SCORE), True, BLACK)
#     display_surf.blit(scores, (10,10))
    
#     for entity in all_sprites:
#         display_surf.blit(entity.image, entity.rect)
#         entity.move()

#     if pygame.sprite.spritecollideany(P1, enemies):
#         pygame.mixer.Sound('crash.wav').play()
#         time.sleep(0.5)
                    
#         display_surf.fill(RED)
#         display_surf.blit(game_over, (30,250))
           
#         pygame.display.update()
#         for entity in all_sprites:
#             entity.kill() 
#         time.sleep(2)
#         pygame.quit()
#         sys.exit()     
    
#     pygame.display.update()
#     FramePerSec.tick(FPS)


import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin_1.png")
        # self.image = pygame.transfrom.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

COIN_APPEAR = pygame.USEREVENT + 2
pygame.time.set_timer(COIN_APPEAR, 3000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     
        if event.type == COIN_APPEAR:
            new_coin = Coin()
            coins.add(new_coin)
            all_sprites.add(new_coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    # scores = font_small.render(str(SCORE), True, BLACK)
    # DISPLAYSURF.blit(scores, (10,10))
    score_display = font_small.render("Coins: " + str(COINS_COLLECTED), True, BLACK)
    DISPLAYSURF.blit(score_display, (300, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()    

    #Check if player collects the coin
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        COINS_COLLECTED += 10
         
    pygame.display.update()
    FramePerSec.tick(FPS)
