import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemPlayer = pygame.image.load('./imagens/player.png')

        self.rect = self.ImagemPlayer.get_rect()
        self.rect.centerx=600
        self.rect.centery=300

        self.vida = True
        self.velocidade = 20
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
    
    def movimento(self):
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
