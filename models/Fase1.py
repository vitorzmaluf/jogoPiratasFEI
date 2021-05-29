import pygame

# from pygame import font
from time import sleep


class Fase1:
    def __init__(self):
        txt='Voce passou para a proxima fase'
        pygame.font.init()
        fonte=pygame.font.get_default_font()
        fontesys=pygame.font.SysFont(fonte, 40)
        self.txttela = fontesys.render(txt, 1, (255,255,255)) 

        self.velocidade = 20

        self.encontrouPortao = False
        self.encontrouChave = False
        self.proximaFase = False

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
        self.rectBarra2.centerx=710
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
        self.rectBarra3.centerx=165
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

        self.imagemParede = pygame.image.load('./imagens/fase1/parede-do-navio.jpg')
        self.rectParede = self.imagemParede.get_rect()
        self.rectParede.centerx=400
        self.rectParede.centery=50

        self.imagemPorta = pygame.image.load('./imagens/fase1/porta.png')
        self.rectPorta = self.imagemPorta.get_rect()
        self.rectPorta.centerx=400
        self.rectPorta.centery=50

        self.imagemCadeado = pygame.image.load('./imagens/fase1/cadeado-da-porta.png')
        self.rectCadeado = self.imagemCadeado.get_rect()
        self.rectCadeado.centerx=375
        self.rectCadeado.centery=55

        self.imagemOpaca = pygame.image.load('./imagens/fase1/imagemOpaca.png')
        self.rectOpaca = self.imagemOpaca.get_rect()
        self.rectOpaca.centerx=400
        self.rectOpaca.centery=200

        self.imagemVaso = pygame.image.load('./imagens/fase1/vase.png')
        self.rectVaso = self.imagemVaso.get_rect()
        self.rectVaso.centerx=200
        self.rectVaso.centery=80

        self.imagemChave = pygame.image.load('./imagens/fase1/chave.png')
        self.rectChave = self.imagemChave.get_rect()
        self.rectChave.centerx=200
        self.rectChave.centery=80

        self.objetos = [self.rectBarra1, self.rectBarra2, self.rectBarra3, self.rectCama1, self.rectToilet1]



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
        superficie.blit(self.imagemParede, self.rectParede)
        superficie.blit(self.imagemPorta, self.rectPorta)
        superficie.blit(self.imagemCadeado, self.rectCadeado)
        if self.encontrouChave == False:
            superficie.blit(self.imagemChave, self.rectChave)
        superficie.blit(self.imagemVaso, self.rectVaso)

        if self.proximaFase:
            self.imagemOpaca.set_alpha(180)
            superficie.blit(self.imagemOpaca, self.rectOpaca)
            superficie.blit(self.txttela,(200,200))


    def checaColisoes(self, player):
        # if self.rectBarra1.collidelist([player.rect]) >= 0:

        if self.rectPortao.collidelist([player.rect]) >= 0:
            self.encontrouPortao = True
            self.moverPortao()
            print("encontrou portao")
        if self.rectVaso.collidelist([player.rect]) >= 0 and self.encontrouPortao:
            self.encontrouChave = True
            self.moverVaso()
            print("encontrou chave")
        if self.rectPorta.collidelist([player.rect]) >= 0 and self.encontrouChave:
            self.proximaFase = True
            self.moverCadeado()
            print("proxima fase")
        
        # if self.proximaFase:

    def moverPortao(self):
        for i in range(440, 570):
            self.rectPortao.right = i

    def moverCadeado(self):
        for i in range(55, 100):
            self.rectCadeado.bottom = i
    
    def moverVaso(self):
        for i in range(200, 100, -1):
            self.rectVaso.left = i
