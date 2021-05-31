import pygame
from pygame.event import post
import pygame, glob
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
        self.rect = self.ImagemPlayer.get_rect()
        self.livre = True

        self.vida = True
        self.velocidade = 3

        '''self.x = self.rect.centerx
        self.y = self.rect.centery'''
    
        xAnt = self.rect.x - self.velocidade
        yAnt = self.rect.y - self.velocidade
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

        self.rect.x = 620
        self.rect.y = 296

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


    def verifica_colisao_fase1(self, objetosFase):
        if self.rect.colliderect(objetosFase['Barra1']):

            print('#############################################################################################')
            # Barra 1
            if abs(objetosFase['Barra1'].bottom - self.rect.top) < 5:
                self.rect.top = objetosFase['Barra1'].bottom
            if abs(objetosFase['Barra1'].top - self.rect.bottom) < 5:
                self.rect.bottom = objetosFase['Barra1'].top

            if abs(objetosFase['Barra1'].left - self.rect.right) < 5:
                self.rect.right = objetosFase['Barra1'].left
            if abs(objetosFase['Barra1'].right - self.rect.left) < 5:
                self.rect.left = objetosFase['Barra1'].right

        if self.rect.colliderect(objetosFase['Barra2']):
            # Barra 3
            if abs(objetosFase['Barra2'].bottom - self.rect.top) < 4:
                self.rect.top = objetosFase['Barra2'].bottom
            if abs(objetosFase['Barra2'].top - self.rect.bottom) < 4:
                self.rect.bottom = objetosFase['Barra2'].top

            if abs(objetosFase['Barra2'].left - self.rect.right) < 4:
                self.rect.right = objetosFase['Barra2'].left
            if abs(objetosFase['Barra2'].right - self.rect.left) < 4:
                self.rect.left = objetosFase['Barra2'].right

        if self.rect.colliderect(objetosFase['Barra3']):
            # Barra 3
            if abs(objetosFase['Barra3'].bottom - self.rect.top) < 3:
                self.rect.top = objetosFase['Barra3'].bottom
            if abs(objetosFase['Barra3'].top - self.rect.bottom) < 3:
                self.rect.bottom = objetosFase['Barra3'].top

            if abs(objetosFase['Barra3'].left - self.rect.right) < 3:
                self.rect.right = objetosFase['Barra3'].left
            if abs(objetosFase['Barra3'].right - self.rect.left) < 3:
                self.rect.left = objetosFase['Barra3'].right

        if self.rect.colliderect(objetosFase['Portao']):
            # Barra 3
            if abs(objetosFase['Portao'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Portao'].bottom
            if abs(objetosFase['Portao'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Portao'].top

            if abs(objetosFase['Portao'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Portao'].left
            if abs(objetosFase['Portao'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Portao'].right


    def verifica_colisao_fase2(self, objetosFase):
        print('#############################################')
        print(objetosFase)
        if self.rect.colliderect(objetosFase['Prateleira2']):
            # Barra 3
            if abs(objetosFase['Prateleira2'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Prateleira2'].bottom
            if abs(objetosFase['Prateleira2'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Prateleira2'].top

            if abs(objetosFase['Prateleira2'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Prateleira2'].left
            if abs(objetosFase['Prateleira2'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Prateleira2'].right

        if self.rect.colliderect(objetosFase['Camas']):
            # Barra 3
            if abs(objetosFase['Camas'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Camas'].bottom
            if abs(objetosFase['Camas'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Camas'].top

            if abs(objetosFase['Camas'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Camas'].left
            if abs(objetosFase['Camas'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Camas'].right

        if self.rect.colliderect(objetosFase['Prateleira1']):
            # Barra 3
            if abs(objetosFase['Prateleira1'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Prateleira1'].bottom
            if abs(objetosFase['Prateleira1'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Prateleira1'].top

            if abs(objetosFase['Prateleira1'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Prateleira1'].left
            if abs(objetosFase['Prateleira1'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Prateleira1'].right

    def verifica_colisao_fase3(self, objetosFase):
        if self.rect.colliderect(objetosFase['Mesa1']):

            if abs(objetosFase['Mesa1'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Mesa1'].bottom
            if abs(objetosFase['Mesa1'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Mesa1'].top

            if abs(objetosFase['Mesa1'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Mesa1'].left
            if abs(objetosFase['Mesa1'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Mesa1'].right

        if self.rect.colliderect(objetosFase['Mesa2']):
            print('#############################################')
            if abs(objetosFase['Mesa2'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Mesa2'].bottom
            if abs(objetosFase['Mesa2'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Mesa2'].top

            if abs(objetosFase['Mesa2'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Mesa2'].left
            if abs(objetosFase['Mesa2'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Mesa2'].right


        if self.rect.colliderect(objetosFase['Mesa3']):
            # Barra 3
            if abs(objetosFase['Mesa3'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Mesa3'].bottom
            if abs(objetosFase['Mesa3'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Mesa3'].top

            if abs(objetosFase['Mesa3'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Mesa3'].left
            if abs(objetosFase['Mesa3'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Mesa3'].right


        if self.rect.colliderect(objetosFase['Mesa4']):
            # Barra 3
            if abs(objetosFase['Mesa4'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Mesa4'].bottom
            if abs(objetosFase['Mesa4'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Mesa4'].top

            if abs(objetosFase['Mesa4'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Mesa4'].left
            if abs(objetosFase['Mesa4'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Mesa4'].right

        if self.rect.colliderect(objetosFase['Mesinha1']):

            if abs(objetosFase['Mesinha1'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Mesinha1'].bottom
            if abs(objetosFase['Mesinha1'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Mesinha1'].top

            if abs(objetosFase['Mesinha1'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Mesinha1'].left
            if abs(objetosFase['Mesinha1'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Mesinha1'].right

        if self.rect.colliderect(objetosFase['Mesinha2']):
            print('#############################################')
            if abs(objetosFase['Mesinha2'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Mesinha2'].bottom
            if abs(objetosFase['Mesinha2'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Mesinha2'].top

            if abs(objetosFase['Mesinha2'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Mesinha2'].left
            if abs(objetosFase['Mesinha2'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Mesinha2'].right


        if self.rect.colliderect(objetosFase['Mesinha3']):
            # Barra 3
            if abs(objetosFase['Mesinha3'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Mesinha3'].bottom
            if abs(objetosFase['Mesinha3'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Mesinha3'].top

            if abs(objetosFase['Mesinha3'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Mesinha3'].left
            if abs(objetosFase['Mesinha3'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Mesinha3'].right


        '''if self.rect.colliderect(objetosFase['Mesinha4']):
            # Barra 3
            if abs(objetosFase['Mesinha4'].bottom - self.rect.top) < 3.1:
                self.rect.top = objetosFase['Mesinha4'].bottom
            if abs(objetosFase['Mesinha4'].top - self.rect.bottom) < 3.1:
                self.rect.bottom = objetosFase['Mesinha4'].top

            if abs(objetosFase['Mesinha4'].left - self.rect.right) < 3.1:
                self.rect.right = objetosFase['Mesinha4'].left
            if abs(objetosFase['Mesinha4'].right - self.rect.left) < 3.1:
                self.rect.left = objetosFase['Mesinha4'].right'''

    def movimento(self, objetosFase):
        xAnt = self.rect.x - self.velocidade
        yAnt = self.rect.y - self.velocidade
 
        if (objetosFase['FASE'] == 1):
            self.verifica_colisao_fase1(objetosFase)

        if (objetosFase['FASE'] == 2):
            self.verifica_colisao_fase2(objetosFase)

        if (objetosFase['FASE'] == 3):
            self.verifica_colisao_fase3(objetosFase)

        if (objetosFase['FASE'] == 4):
            pass

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

        if self.step_index > 18:
            self.step_index = 0

        if self.attack_index > 144:
            self.attack_index = 0

        if self._turn_left:
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

    def setPos(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

