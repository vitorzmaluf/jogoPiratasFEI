import pygame

class Boss(pygame.sprite.Sprite):

    idleCount = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #ImagemBossArr = [pygame.image.load('./imagens/barba_ruiva_new/idle_0.png'), pygame.image.load('./imagens/barba_ruiva_new/idle_1.png'), pygame.image.load('./imagens/barba_ruiva_new/idle_2.png'), pygame.image.load('./imagens/barba_ruiva_new/idle_3.png'), pygame.image.load('./imagens/barba_ruiva_new/idle_4.png'), pygame.image.load('./imagens/barba_ruiva_new/idle_5.png'), pygame.image.load('./imagens/barba_ruiva_new/idle_6.png')]
        #ImagemBossFlipArr = [pygame.transform.flip(ImagemBossArr[0], True, False), pygame.transform.flip(ImagemBossArr[1], True, False), pygame.transform.flip(ImagemBossArr[2], True, False), pygame.transform.flip(ImagemBossArr[3], True, False), pygame.transform.flip(ImagemBossArr[4], True, False), pygame.transform.flip(ImagemBossArr[5], True, False), pygame.transform.flip(ImagemBossArr[6], True, False)]

        self.ImagemBoss = pygame.image.load('./imagens/barba_ruiva/teste.png')
        self.ImagemBossFlip = pygame.transform.flip(self.ImagemBoss, True, False)
        self.rect = self.ImagemBossFlip.get_rect()
        self.rect.centerx=650
        self.rect.centery=250

    def colocar(self, superficie):
        superficie.blit(self.ImagemBossFlip, self.rect)
