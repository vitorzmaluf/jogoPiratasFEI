import pygame
import random

idleCount = 0

class Boss(pygame.sprite.Sprite):
    ImagemBossWalkArr = []
    ImagemBossWalkFlipArr = []

    ImagemBossAtkArr = []
    ImagemBossAtkFlipArr = []

    ImagemBossDeadArr = []
    ImagemBossDeadFlipArr = []

    ''' State = 0 -> Await, 
        State = 1 -> Attack,
        State = 2 -> Dead '''

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBossAtkArr = [
          pygame.image.load('./imagens/barba_ruiva_new/ATTACK_000.png')
        , pygame.image.load('./imagens/barba_ruiva_new/ATTACK_001.png')
        , pygame.image.load('./imagens/barba_ruiva_new/ATTACK_002.png')
        , pygame.image.load('./imagens/barba_ruiva_new/ATTACK_003.png')
        , pygame.image.load('./imagens/barba_ruiva_new/ATTACK_004.png')
        , pygame.image.load('./imagens/barba_ruiva_new/ATTACK_005.png')
        , pygame.image.load('./imagens/barba_ruiva_new/ATTACK_006.png')]

        self.ImagemBossWalkArr = [
          pygame.image.load('./imagens/barba_ruiva_new/WALK_000.png')
        , pygame.image.load('./imagens/barba_ruiva_new/WALK_001.png')
        , pygame.image.load('./imagens/barba_ruiva_new/WALK_002.png')
        , pygame.image.load('./imagens/barba_ruiva_new/WALK_003.png')
        , pygame.image.load('./imagens/barba_ruiva_new/WALK_004.png')
        , pygame.image.load('./imagens/barba_ruiva_new/WALK_005.png')
        , pygame.image.load('./imagens/barba_ruiva_new/WALK_006.png')]

        self.ImagemBossDeadArr = [
          pygame.image.load('./imagens/barba_ruiva_new/DIE_000.png')
        , pygame.image.load('./imagens/barba_ruiva_new/DIE_001.png')
        , pygame.image.load('./imagens/barba_ruiva_new/DIE_002.png')
        , pygame.image.load('./imagens/barba_ruiva_new/DIE_003.png')
        , pygame.image.load('./imagens/barba_ruiva_new/DIE_004.png')
        , pygame.image.load('./imagens/barba_ruiva_new/DIE_005.png')
        , pygame.image.load('./imagens/barba_ruiva_new/DIE_006.png')]




        self.ImagemBossFlipWalkArr = [pygame.transform.flip(self.ImagemBossWalkArr[0], True, False),
                                      pygame.transform.flip(self.ImagemBossWalkArr[1], True, False), 
                                      pygame.transform.flip(self.ImagemBossWalkArr[2], True, False), 
                                      pygame.transform.flip(self.ImagemBossWalkArr[3], True, False), 
                                      pygame.transform.flip(self.ImagemBossWalkArr[4], True, False), 
                                      pygame.transform.flip(self.ImagemBossWalkArr[5], True, False), 
                                      pygame.transform.flip(self.ImagemBossWalkArr[6], True, False)]

        self.ImagemBossAtkFlipArr = [ pygame.transform.flip(self.ImagemBossAtkArr[0], True, False),
                                      pygame.transform.flip(self.ImagemBossAtkArr[1], True, False), 
                                      pygame.transform.flip(self.ImagemBossAtkArr[2], True, False), 
                                      pygame.transform.flip(self.ImagemBossAtkArr[3], True, False), 
                                      pygame.transform.flip(self.ImagemBossAtkArr[4], True, False), 
                                      pygame.transform.flip(self.ImagemBossAtkArr[5], True, False), 
                                      pygame.transform.flip(self.ImagemBossAtkArr[6], True, False)]

        self.ImagemBossDeadFlipArr = [ pygame.transform.flip(self.ImagemBossDeadArr[0], True, False),
                                      pygame.transform.flip(self.ImagemBossDeadArr[1], True, False), 
                                      pygame.transform.flip(self.ImagemBossDeadArr[2], True, False), 
                                      pygame.transform.flip(self.ImagemBossDeadArr[3], True, False), 
                                      pygame.transform.flip(self.ImagemBossDeadArr[4], True, False), 
                                      pygame.transform.flip(self.ImagemBossDeadArr[5], True, False), 
                                      pygame.transform.flip(self.ImagemBossDeadArr[6], True, False)]

        self.ImagemBossFlip = self.ImagemBossWalkArr[0]
        
        self.rect = self.ImagemBossFlip.get_rect()
        self.rect.centerx=650
        self.rect.centery=250

        self.life = random.randint(10,20)
        
        self.velocidade = 1
        self.bossState = 0
        self.flip = 0


    def colocar(self, superficie, n):
        if(self.bossState == 0):
            if(self.flip == 1):
                superficie.blit(self.ImagemBossWalkArr[n], self.rect)
            else:
                superficie.blit(self.ImagemBossFlipWalkArr[n], self.rect)
        elif(self.bossState == 1):
            superficie.blit(self.ImagemBossAtkFlipArr[n], self.rect)
        else:
            superficie.blit(self.ImagemBossDeadFlipArr[n], self.rect)


    def movimento(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.bottom > 400:
            self.rect.bottom = 400
        if self.rect.top < 60:
            self.rect.top = 60
