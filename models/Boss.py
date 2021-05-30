import pygame
import random

idleCount = 0

class Boss(pygame.sprite.Sprite):
    ImagemBossArr = []
    ImagemBossFlipArr = []

    ''' State = 0 -> Await, 
        State = 1 -> Attack,
        State = 2 -> Dead '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBossArr = [
          pygame.image.load('./imagens/barba_ruiva_new/idle_0.png')
        , pygame.image.load('./imagens/barba_ruiva_new/idle_1.png')
        , pygame.image.load('./imagens/barba_ruiva_new/idle_2.png')
        , pygame.image.load('./imagens/barba_ruiva_new/idle_3.png')
        , pygame.image.load('./imagens/barba_ruiva_new/idle_4.png')
        , pygame.image.load('./imagens/barba_ruiva_new/idle_5.png')
        , pygame.image.load('./imagens/barba_ruiva_new/idle_6.png')]

        self.ImagemBossFlipArr = [pygame.transform.flip(self.ImagemBossArr[0], True, False) , pygame.transform.flip(self.ImagemBossArr[1], True, False), pygame.transform.flip(self.ImagemBossArr[2], True, False), pygame.transform.flip(self.ImagemBossArr[3], True, False), pygame.transform.flip(self.ImagemBossArr[4], True, False), pygame.transform.flip(self.ImagemBossArr[5], True, False), pygame.transform.flip(self.ImagemBossArr[6], True, False)]

        self.ImagemBoss = pygame.image.load('./imagens/barba_ruiva_new/idle_0.png')
        self.ImagemBossFlip = pygame.transform.flip(self.ImagemBoss, True, False)
        
        self.rect = self.ImagemBossFlip.get_rect()
        self.rect.centerx=650
        self.rect.centery=250

        self.life = 100
        
        self.velocidade = 1
        self.bossState = 0


    def colocar(self, superficie):
        superficie.blit(self.ImagemBossFlipArr[0], self.rect)

    def movimento(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.bottom > 400:
            self.rect.bottom = 400
        if self.rect.top < 60:
            self.rect.top = 60
