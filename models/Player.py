import pygame
from pygame.locals import *

class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        self.Shoot = pygame.image.load('./imagens/shot.png')

    
class Player(pygame.sprite.Sprite):
    

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemPlayer = pygame.image.load('./imagens/player.png')
        self.livre = True

        shoots = []

        self.rect = self.ImagemPlayer.get_rect()
        self.rect.centerx=150
        self.rect.centery=300

        self.vida = True
        self.velocidade = 3
    
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

    def disparou(self):
        self.rect = self.Shoot.get_rect()
        self.rect.centerx= self.rect.left
        self.rect.centery= self.rect.top


    def colocar(self, superficie):
        superficie.blit(self.ImagemPlayer, self.rect)
