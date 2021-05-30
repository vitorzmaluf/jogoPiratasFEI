from models.Player import Player
import pygame

class FaseFinal:
    def __init__(self):
        self.imagemCeu = pygame.image.load('./imagens/fase_final/sky.png')
        self.rectCeu = self.imagemCeu.get_rect()
        self.rectCeu.centerx=400
        self.rectCeu.centery=50

        self.imagemBorda = pygame.image.load('./imagens/fase_final/borda-navio.png')
        self.rectBorda = self.imagemBorda.get_rect()
        self.rectBorda.centerx=400
        self.rectBorda.centery=50


    def colocar(self, superficie):
        superficie.blit(self.imagemCeu, self.rectCeu)
        superficie.blit(self.imagemBorda, self.rectBorda)

