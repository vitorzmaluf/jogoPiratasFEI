import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemPlayer = pygame.image.load('./imagens/player.png')

        self.livre = True

        self.rect = self.ImagemPlayer.get_rect()
        self.rect.centerx=600
        self.rect.centery=300

        self.vida = True
        self.velocidade = 3
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
    
    def movimento(self, objetosFase):
        xAnt = self.rect.x - self.velocidade
        yAnt = self.rect.y - self.velocidade
 

        # if self.rect.collidelist(objetosFase) >= 0:
        #     print("Colidiu")
        #     self.livre = False
        # else:
        #     self.livre = True
        
        # keys = pygame.key.get_pressed()
        # if(self.livre):
        #     if not keys[K_LEFT] and not keys[K_RIGHT] and not keys[K_UP] and not keys[K_DOWN]:
        #         self.livre = True


        if self.vida:
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rect.right > 800:
                self.rect.right = 800
            if self.rect.bottom > 400:
                self.rect.bottom = 400
            if self.rect.top <= 0:
                self.rect.top = 0

    def colocar(self, superficie):
        superficie.blit(self.ImagemPlayer, self.rect)
