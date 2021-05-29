from models.Player import Player
import pygame

posicoes_x =[140, 320, 580]
posicoes_y =[155, 285, 195]
caixas = []

class Box:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def setarPos(x,y):
        Box.x = x
        Box.y = y

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

        self.imagemCaixa = pygame.image.load('./imagens/fase_final/box.png')
        for n in range(len(posicoes_x)):
            self.rectCaixa = self.imagemCaixa.get_rect()
            self.rectCaixa.centerx = posicoes_x[n]
            self.rectCaixa.centery = posicoes_y[n]
            caixas.append(self.rectCaixa)

        Player.po

    def colocar(self, superficie):
        superficie.blit(self.imagemCeu, self.rectCeu)
        superficie.blit(self.imagemBorda, self.rectBorda)

        for n in caixas:
            superficie.blit(self.imagemCaixa, n)

