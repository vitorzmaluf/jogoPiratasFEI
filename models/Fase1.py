import pygame

class Fase1:
    def __init__(self):
        self.imagemBarra1 = pygame.image.load('./imagens/fase1/barra1.png')
        self.rectBarra1 = self.imagemBarra1.get_rect()
        self.rectBarra1.centerx=400
        self.rectBarra1.centery=300

        self.imagemPortao = pygame.image.load('./imagens/fase1/portao.png')
        self.rectPortao = self.imagemPortao.get_rect()
        self.rectPortao.centerx=440
        self.rectPortao.centery=204

        self.imagemBarra2 = pygame.image.load('./imagens/fase1/barra2.png')
        self.rectBarra2 = self.imagemBarra2.get_rect()
        self.rectBarra2.centerx=690
        self.rectBarra2.centery=204

        self.imagemCama1 = pygame.image.load('./imagens/fase1/cama1.png')
        self.rectCama1 = self.imagemCama1.get_rect()
        self.rectCama1.centerx=746
        self.rectCama1.centery=375

        self.imagemToilet1 = pygame.image.load('./imagens/fase1/toilet.png')
        self.rectToilet1 = self.imagemToilet1.get_rect()
        self.rectToilet1.centerx=420
        self.rectToilet1.centery=375

        self.imagemBarra3 = pygame.image.load('./imagens/fase1/barra2.png')
        self.rectBarra3 = self.imagemBarra3.get_rect()
        self.rectBarra3.centerx=175
        self.rectBarra3.centery=204

        self.imagemCama2 = pygame.image.load('./imagens/fase1/cama1.png')
        self.rectCama2 = self.imagemCama2.get_rect()
        self.rectCama2.centerx=340
        self.rectCama2.centery=375

        self.imagemToilet2 = pygame.image.load('./imagens/fase1/toilet.png')
        self.rectToilet2 = self.imagemToilet2.get_rect()
        self.rectToilet2.centerx=30
        self.rectToilet2.centery=375

        self.imagemEsqueleto = pygame.image.load('./imagens/fase1/esqueleto.png')
        self.rectEsqueleto = self.imagemEsqueleto.get_rect()
        self.rectEsqueleto.centerx=340
        self.rectEsqueleto.centery=375


    def colocar(self, superficie):
        superficie.blit(self.imagemBarra1, self.rectBarra1)
        superficie.blit(self.imagemBarra2, self.rectBarra2)
        superficie.blit(self.imagemPortao, self.rectPortao)
        superficie.blit(self.imagemCama1, self.rectCama1)
        superficie.blit(self.imagemToilet1, self.rectToilet1)
        superficie.blit(self.imagemBarra3, self.rectBarra3)
        superficie.blit(self.imagemCama2, self.rectCama2)
        superficie.blit(self.imagemToilet2, self.rectToilet2)
        superficie.blit(self.imagemEsqueleto, self.rectEsqueleto)