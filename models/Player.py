<<<<<<< HEAD
import pygame
from pygame.event import post
=======
import pygame, glob
>>>>>>> cb1efa19cae74bf3998da580cc6cf082be08fcd6
from pygame.locals import *

class Shoot(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.Shoot = pygame.image.load('./imagens/shot.png')
        self.rect = self.Shoot.get_rect()
        self.rect.centerx=pos_x
        self.rect.centery=pos_y
        self.vel = 1

        self.x = pos_x
        self.y = pos_y

    def atualizar(self):
        self.rect.x += self.vel
        self.x = self.rect.x
        self.y = self.rect.y


    def colocar(self, superficie):
        superficie.blit(self.Shoot, self.rect)
    
class Player(pygame.sprite.Sprite):

    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemPlayer = pygame.image.load('./imagens/player.png')
        self.livre = True

        self.vida = True
        self.velocidade = 3

<<<<<<< HEAD
        self.x = self.rect.centerx
        self.y = self.rect.centery
    
    def movimento(self, objetosFase):
        xAnt = self.rect.x - self.velocidade
        yAnt = self.rect.y - self.velocidade
=======
        self._turn_right = False
        self._turn_left = False
        self._attack_flag = False
        self.walk_right = []
        self.walk_left = []
        self.attack = []
        self.carrega_sprites_andar()
        self.carrega_sprites_atacar()
        self.step_index = 0
        self.attack_index = 0


        self.rect = self.ImagemPlayer.get_rect()
        self.rect.centerx = 150
        self.rect.centery = 300

    def set_turn_right(self, bool):
        self._turn_right = bool

    def set_turn_left(self, bool):
        self._turn_left = bool

    def set_attack_flag(self, bool):
        self._attack_flag = bool

    def carrega_sprites_atacar(self):
        sprites = glob.glob('./todasImagens/PNG/2/attack/*.png')

        for sprite in sprites:
            sprite = sprite.replace('\\', '/')
            self.attack.append(pygame.image.load(sprite))

    def carrega_sprites_andar(self):
        sprites = glob.glob('./todasImagens/PNG/2/walk/*.png')

        for sprite in sprites:
            sprite = sprite.replace('\\', '/')
            print(sprite)
            if 'walk_left' in sprite:
                self.walk_left.append(pygame.image.load(sprite))
            else:
                self.walk_right.append(pygame.image.load(sprite))
        #print(self.walk_left))
        #print((self.walk_right))


    def movimento(self, objetosFase):
        xAnt = self.rect.x - self.velocidade
        yAnt = self.rect.y - self.velocidade
 

        '''if self.rect.collidelist(objetosFase) >= 0:
             print("Colidiu")
             self.livre = False
        else:
            self.livre = True
        
        keys = pygame.key.get_pressed()
        if(self.livre):
            if not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_UP] and not keys[K_DOWN]:
                self.livre = True'''

>>>>>>> cb1efa19cae74bf3998da580cc6cf082be08fcd6

        if self.vida:
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rect.right > 800:
                self.rect.right = 800
            if self.rect.bottom > 400:
                self.rect.bottom = 400
            if self.rect.top < 60:
                self.rect.top = 60


    def colocar(self, superficie):
<<<<<<< HEAD
        superficie.blit(self.ImagemPlayer, self.rect)

    def setPos(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
=======
        if self.step_index > 18:
            self.step_index = 0

        if self.attack_index > 144:
            self.attack_index = 0

        if self._turn_left:
            print('chamou')
            superficie.blit(self.walk_left[self.step_index//3], self.rect)
            self.step_index += 1

        elif self._turn_right:
            superficie.blit(self.walk_right[self.step_index//3], self.rect)
            self.step_index += 1
        elif self._attack_flag:
            superficie.blit(self.attack[self.step_index // 24], self.rect)
            self.attack_index += 1

        else:
            superficie.blit(self.ImagemPlayer, self.rect)
>>>>>>> cb1efa19cae74bf3998da580cc6cf082be08fcd6
