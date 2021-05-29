import pygame
from time import sleep
from models.Player import Player

class Fase2:
    def __init__(self):
        txt='Voce passou para a proxima fase'
        pygame.font.init()
        fonte=pygame.font.get_default_font()
        fontesys=pygame.font.SysFont(fonte, 40)
        self.txttela = fontesys.render(txt, 1, (255,255,255)) 


        self.encontrouCofre = False #Fica atras do quadro da direita
        self.encontrouCodigo = False #codigo para abrir o cofre - fica em baixo da cama inferior direita
        self.encontrouFenda = False # fica dentro do cofre
        self.encontrouChave = False # fica atras do quadro da esquerda, que tem que ser removido com a chave de fenda
        self.abriuCadeado = False
        self.proximaFase = False


        self.imagemPrateleira1 = pygame.image.load('./imagens/fase2/cj-prateleiras-1.png')
        self.rectPrateleira1 = self.imagemPrateleira1.get_rect()
        self.rectPrateleira1.centerx=400
        self.rectPrateleira1.centery=200

        self.imagemBeliches = pygame.image.load('./imagens/fase2/beliches.png')
        self.rectBeliches = self.imagemBeliches.get_rect()
        self.rectBeliches.centerx=400
        self.rectBeliches.centery=200
        

        self.imagemTesouros = pygame.image.load('./imagens/fase2/tesouros.png')
        self.rectTesouros = self.imagemTesouros.get_rect()
        self.rectTesouros.centerx=400
        self.rectTesouros.centery=200

        self.imagemPrateleira2 = pygame.image.load('./imagens/fase2/cjPrateleiras2.png')
        self.rectPrateleira2 = self.imagemPrateleira2.get_rect()
        self.rectPrateleira2.centerx=400
        self.rectPrateleira2.centery=200

        self.imagemsacosDeMoedas = pygame.image.load('./imagens/fase2/sacosDeMoedas.png')
        self.rectsacosDeMoedas = self.imagemsacosDeMoedas.get_rect()
        self.rectsacosDeMoedas.centerx=400
        self.rectsacosDeMoedas.centery=200

        self.imagemQuadroEsquerda = pygame.image.load('./imagens/fase2/quadro-esquerda.png')
        self.rectQuadroEsquerda = self.imagemQuadroEsquerda.get_rect()
        self.rectQuadroEsquerda.centerx=325
        self.rectQuadroEsquerda.centery=50

        self.imagemQuadroDireita = pygame.image.load('./imagens/fase2/quadro-direita.png')
        self.rectQuadroDireita = self.imagemQuadroDireita.get_rect()
        self.rectQuadroDireita.centerx=480
        self.rectQuadroDireita.centery=50

        self.imagemBeliche = pygame.image.load('./imagens/fase2/beliche.png')
        self.rectBeliche = self.imagemBeliche.get_rect()
        self.rectBeliche.centerx=200
        self.rectBeliche.centery=325

        self.imagemPrateleiraEspecial = pygame.image.load('./imagens/fase2/prateleiraEspecial.jpg')
        self.rectPrateleiraEspecial = self.imagemPrateleiraEspecial.get_rect()
        self.rectPrateleiraEspecial.centerx=756
        self.rectPrateleiraEspecial.centery=93

        self.imagemParede = pygame.image.load('./imagens/fase2/parede-do-navio.jpg')
        self.rectParede = self.imagemParede.get_rect()
        self.rectParede.centerx=400
        self.rectParede.centery=50

        self.imagemPorta = pygame.image.load('./imagens/fase2/porta.png')
        self.rectPorta = self.imagemPorta.get_rect()
        self.rectPorta.centerx=400
        self.rectPorta.centery=50

        self.imagemCadeado = pygame.image.load('./imagens/fase2/cadeado-da-porta.png')
        self.rectCadeado = self.imagemCadeado.get_rect()
        self.rectCadeado.centerx=375
        self.rectCadeado.centery=55

        self.imagemCofre = pygame.image.load('./imagens/fase2/safe-box.png')
        self.rectCofre = self.imagemCofre.get_rect()
        self.rectCofre.centerx=480
        self.rectCofre.centery=55

        self.imagemChave = pygame.image.load('./imagens/fase2/chave.png')
        self.rectChave = self.imagemChave.get_rect()
        self.rectChave.centerx=325
        self.rectChave.centery=55

        self.imagemOpaca = pygame.image.load('./imagens/fase1/imagemOpaca.png')
        self.rectOpaca = self.imagemOpaca.get_rect()
        self.rectOpaca.centerx=400
        self.rectOpaca.centery=200

        self.objetos = [self.rectPrateleira1, self.rectPrateleira2, self.rectBeliches, self.rectTesouros, self.rectsacosDeMoedas]

    

    def colocar(self, superficie):
        superficie.blit(self.imagemParede, self.rectParede)
        superficie.blit(self.imagemPorta, self.rectPorta)
        superficie.blit(self.imagemCadeado, self.rectCadeado)
        superficie.blit(self.imagemPrateleira1, self.rectPrateleira1)
        superficie.blit(self.imagemPrateleira2, self.rectPrateleira2)
        superficie.blit(self.imagemBeliches, self.rectBeliches)
        superficie.blit(self.imagemTesouros, self.rectTesouros)
        superficie.blit(self.imagemsacosDeMoedas, self.rectsacosDeMoedas)
        if self.encontrouChave == False:
            superficie.blit(self.imagemChave, self.rectChave)
        superficie.blit(self.imagemQuadroEsquerda, self.rectQuadroEsquerda)
        superficie.blit(self.imagemCofre, self.rectCofre)
        superficie.blit(self.imagemQuadroDireita, self.rectQuadroDireita)
        superficie.blit(self.imagemBeliche, self.rectBeliche)
        superficie.blit(self.imagemPrateleiraEspecial, self.rectPrateleiraEspecial)

        
        if self.proximaFase:
            self.imagemOpaca.set_alpha(180)
            superficie.blit(self.imagemOpaca, self.rectOpaca)
            superficie.blit(self.txttela,(200,200))
        

    def checaColisoes(self, player):
        #Verifica se encontrou o cofre (Fica atras do quadro da direita)
        if self.rectQuadroDireita.collidelist([player.rect]) >= 0:
            self.encontrouCofre = True
            self.moverQuadroDireita()
            print("encontrou cofre")
        #Verifica se encontrou o codigo (Fica em baixo da cama inferior direita)
        if self.rectBeliche.collidelist([player.rect]) >= 0 and self.encontrouCofre:
            self.encontrouCodigo = True
            print("encontrou codigo")
        
        #Verifica se encontrou a chave de fenda (Fica dentro do cofre)
        if self.rectCofre.collidelist([player.rect]) >= 0 and self.encontrouCodigo:
            self.encontrouFenda = True
            print("encontrou fenda")
        
        #Verifica se encontrou a chave da porta (Fica tras do quadro da esquerda)
        if self.rectQuadroEsquerda.collidelist([player.rect]) >= 0 and self.encontrouFenda:
            self.encontrouChave = True
            self.moverQuadroEsquerda()
            print("encontrou chave")
        #Abre a porta se encontrou chave
        if self.rectPorta.collidelist([player.rect]) >= 0 and self.encontrouChave:
            self.abriuCadeado = True
            self.moverCadeado()
            print("abriu cadeado")
        if self.rectPorta.collidelist([player.rect]) >= 0 and self.abriuCadeado:
            self.proximaFase = True
            print("proxima fase")

    def moverQuadroEsquerda(self):
        for i in range(50, 180):
            self.rectQuadroEsquerda.bottom = i

    def moverQuadroDireita(self):
        for i in range(50, 150):
            self.rectQuadroDireita.bottom = i

    def moverCadeado(self):
        for i in range(55, 100):
            self.rectCadeado.bottom = i
        
