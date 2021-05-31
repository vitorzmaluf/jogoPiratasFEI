import pygame
from pygame.event import post
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

        self.rect = self.ImagemPlayer.get_rect()
        self.rect.centerx=150
        self.rect.centery=300

        self.vida = True
        self.velocidade = 3

        self.x = self.rect.centerx
        self.y = self.rect.centery
    
    def movimento(self, objetosFase):
        xAnt = self.rect.x - self.velocidade
        yAnt = self.rect.y - self.velocidade

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
        superficie.blit(self.ImagemPlayer, self.rect)

    def setPos(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y
