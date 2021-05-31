from models.Player import Player
from models.Boss import Boss
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

        self.objetos = [self.rectBorda, self.rectCeu]

        self.proximaFase = False
        self.disparos = []



    def colocar(self, superficie):
        superficie.blit(self.imagemCeu, self.rectCeu)
        superficie.blit(self.imagemBorda, self.rectBorda)

    def tocar(self):
        pygame.mixer.music.load('./sons/music-pirata.wav')
        pygame.mixer.music.play(0)

    def parar(self):
        pygame.mixer.music.stop()

    def Lose(self, superficie):
        txt='Você morreu!'
        pygame.font.init()
        fonte=pygame.font.get_default_font()
        fontesys=pygame.font.SysFont(fonte, 40)
        self.txttela = fontesys.render(txt, 1, (255,255,255)) 

        self.imagemOpaca = pygame.image.load('./imagens/fase1/imagemOpaca.png')
        self.rectOpaca = self.imagemOpaca.get_rect()
        self.rectOpaca.centerx=400
        self.rectOpaca.centery=200

        self.imagemOpaca.set_alpha(180)
        superficie.blit(self.imagemOpaca, self.rectOpaca)
        superficie.blit(self.txttela,(200,200))

    def Win(self, superficie):
        txt='Você venceu!'
        pygame.font.init()
        fonte=pygame.font.get_default_font()
        fontesys=pygame.font.SysFont(fonte, 40)
        self.txttela = fontesys.render(txt, 1, (255,255,255)) 

        self.imagemOpaca = pygame.image.load('./imagens/fase1/imagemOpaca.png')
        self.rectOpaca = self.imagemOpaca.get_rect()
        self.rectOpaca.centerx=400
        self.rectOpaca.centery=200

        self.imagemOpaca.set_alpha(180)
        superficie.blit(self.imagemOpaca, self.rectOpaca)
        superficie.blit(self.txttela,(200,200))


