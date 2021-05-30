import pygame

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
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((255, 255, 255))
    
    def movimento(self, objetosFase):
        xAnt = self.rect.x - self.velocidade
        yAnt = self.rect.y - self.velocidade
        self.livre = True

        #if self.rect.collidelist(objetosFase) >= 0:
            #print("Colidiu")
            #self.livre = False
            # self.rect.x = yAnt
            # self.rect.y = xAnt

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
