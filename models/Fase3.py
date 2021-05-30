import pygame

class Fase3:
    def __init__(self):
        self.objetos = []
        self.proximaFase = False

        self.imagemParede = pygame.image.load('./imagens/fase3/parede-do-navio.jpg')
        self.rectParede = self.imagemParede.get_rect()
        self.rectParede.centerx=400
        self.rectParede.centery=50

        self.imagemPorta = pygame.image.load('./imagens/fase3/porta.png')
        self.rectPorta = self.imagemPorta.get_rect()
        self.rectPorta.centerx=400
        self.rectPorta.centery=50

        self.imagemCadeado = pygame.image.load('./imagens/fase3/cadeado-da-porta.png')
        self.rectCadeado = self.imagemCadeado.get_rect()
        self.rectCadeado.centerx=375
        self.rectCadeado.centery=55

        self.imagemDishes1 = pygame.image.load('./imagens/fase3/dishes.png')
        self.rectDishes1 = self.imagemDishes1.get_rect()
        self.rectDishes1.centerx=675
        self.rectDishes1.centery=75

        self.imagemDishes2 = pygame.image.load('./imagens/fase3/dishes.png')
        self.rectDishes2 = self.imagemDishes2.get_rect()
        self.rectDishes2.centerx=725
        self.rectDishes2.centery=75

        self.imagemDishes3 = pygame.image.load('./imagens/fase3/dishes.png')
        self.rectDishes3 = self.imagemDishes3.get_rect()
        self.rectDishes3.centerx=775
        self.rectDishes3.centery=75

        self.imagemArmario1 = pygame.image.load('./imagens/fase3/armarios.png')
        self.rectArmario1 = self.imagemArmario1.get_rect()
        self.rectArmario1.centerx=60
        self.rectArmario1.centery=95
        
        self.imagemArmario2 = pygame.image.load('./imagens/fase3/armarios.png')
        self.rectArmario2 = self.imagemArmario2.get_rect()
        self.rectArmario2.centerx=60
        self.rectArmario2.centery=34

        self.imagemFogao = pygame.image.load('./imagens/fase3/fogao.png')
        self.rectFogao = self.imagemFogao.get_rect()
        self.rectFogao.centerx=142
        self.rectFogao.centery=64

        self.imagemFogao2 = pygame.image.load('./imagens/fase3/fogao2.png')
        self.rectFogao2 = self.imagemFogao2.get_rect()
        self.rectFogao2.centerx=175
        self.rectFogao2.centery=98

        self.imagemArmario3 = pygame.image.load('./imagens/fase3/armarios.png')
        self.rectArmario3 = self.imagemArmario3.get_rect()
        self.rectArmario3.centerx=254
        self.rectArmario3.centery=95
        
        self.imagemArmario4 = pygame.image.load('./imagens/fase3/armarios.png')
        self.rectArmario4 = self.imagemArmario4.get_rect()
        self.rectArmario4.centerx=254
        self.rectArmario4.centery=34

        self.imagemVaso = pygame.image.load('./imagens/fase3/vase.png')
        self.rectVaso = self.imagemVaso.get_rect()
        self.rectVaso.centerx=110
        self.rectVaso.centery=40


        self.imagemMesa = pygame.image.load('./imagens/fase3/table.png')

        self.rectMesa1 = self.imagemMesa.get_rect()
        self.rectMesa1.centerx=90
        self.rectMesa1.centery=250

        self.rectMesa2 = self.imagemMesa.get_rect()
        self.rectMesa2.centerx=300
        self.rectMesa2.centery=250

        self.rectMesa3 = self.imagemMesa.get_rect()
        self.rectMesa3.centerx=520
        self.rectMesa3.centery=250

        self.rectMesa4 = self.imagemMesa.get_rect()
        self.rectMesa4.centerx=720
        self.rectMesa4.centery=250


        self.imagemCadeirasEsq = pygame.image.load('./imagens/fase3/chairs-left.png')
        self.imagemCadeirasDir = pygame.image.load('./imagens/fase3/chairs-right.png')

        self.rectChairsEsq1 = self.imagemCadeirasEsq.get_rect()
        self.rectChairsEsq1.centerx=37
        self.rectChairsEsq1.centery=250

        self.rectChairsEsq2 = self.imagemCadeirasEsq.get_rect()
        self.rectChairsEsq2.centerx=247
        self.rectChairsEsq2.centery=250

        self.rectChairsEsq3 = self.imagemCadeirasEsq.get_rect()
        self.rectChairsEsq3.centerx=466
        self.rectChairsEsq3.centery=250

        self.rectChairsEsq4 = self.imagemCadeirasEsq.get_rect()
        self.rectChairsEsq4.centerx=668
        self.rectChairsEsq4.centery=250


        self.rectChairsDir1 = self.imagemCadeirasDir.get_rect()
        self.rectChairsDir1.centerx=143
        self.rectChairsDir1.centery=250

        self.rectChairsDir2 = self.imagemCadeirasDir.get_rect()
        self.rectChairsDir2.centerx=353
        self.rectChairsDir2.centery=250

        self.rectChairsDir3 = self.imagemCadeirasDir.get_rect()
        self.rectChairsDir3.centerx=571
        self.rectChairsDir3.centery=250

        self.rectChairsDir4 = self.imagemCadeirasDir.get_rect()
        self.rectChairsDir4.centerx=773
        self.rectChairsDir4.centery=250


        self.imagemMesinha = pygame.image.load('./imagens/fase3/mesinha.png')

        self.rectMesinha1 = self.imagemCadeirasEsq.get_rect()
        self.rectMesinha1.centerx=15
        self.rectMesinha1.centery=415

        self.rectMesinha2 = self.imagemCadeirasEsq.get_rect()
        self.rectMesinha2.centerx=157
        self.rectMesinha2.centery=415

        self.rectMesinha3 = self.imagemCadeirasEsq.get_rect()
        self.rectMesinha3.centerx=580
        self.rectMesinha3.centery=415

        self.rectMesinha4 = self.imagemCadeirasEsq.get_rect()
        self.rectMesinha4.centerx=720
        self.rectMesinha4.centery=415


        self.imagemUpHolst = pygame.image.load('./imagens/fase3/upholstery.png')

        self.rectUpHolst1 = self.imagemUpHolst.get_rect()
        self.rectUpHolst1.centerx=115
        self.rectUpHolst1.centery=376

        self.rectUpHolst2 = self.imagemUpHolst.get_rect()
        self.rectUpHolst2.centerx=680
        self.rectUpHolst2.centery=376

        self.imagemBauAberto = pygame.image.load('./imagens/fase3/closed-chest.png')
        self.imagemBauFechado = pygame.image.load('./imagens/fase3/opened-chest.png')

        self.rectBauAberto = self.imagemUpHolst.get_rect()
        self.rectBauAberto.centerx=685
        self.rectBauAberto.centery=363


        self.rects =[
            self.rectParede,
            self.rectPorta,
            self.rectCadeado,
            self.rectDishes1,
            self.rectDishes2,
            self.rectDishes3,
            self.rectArmario1,
            self.rectArmario2,
            self.rectFogao,
            self.rectFogao2,
            self.rectArmario3,
            self.rectArmario4,
            self.rectVaso,
            self.rectMesa1,
            self.rectMesa2,
            self.rectMesa3,
            self.rectMesa4,
            self.rectChairsEsq1,
            self.rectChairsEsq2,
            self.rectChairsEsq3,
            self.rectChairsEsq4,
            self.rectChairsDir1,
            self.rectChairsDir2,
            self.rectChairsDir3,
            self.rectChairsDir4,
            self.rectMesinha1,
            self.rectMesinha2,
            self.rectMesinha3,
            self.rectMesinha4,
            self.rectUpHolst1,
            self.rectUpHolst2,
            self.rectBauAberto,
            
            ]

        self.imagens = [
            self.imagemParede,
            self.imagemPorta,
            self.imagemCadeado,
            self.imagemDishes1,
            self.imagemDishes2,
            self.imagemDishes3,
            self.imagemArmario1,
            self.imagemArmario2,
            self.imagemFogao,
            self.imagemFogao2,
            self.imagemArmario3,
            self.imagemArmario4,
            self.imagemVaso,
            self.imagemMesa,
            self.imagemMesa,
            self.imagemMesa,
            self.imagemMesa,
            self.imagemCadeirasEsq,
            self.imagemCadeirasEsq,
            self.imagemCadeirasEsq,
            self.imagemCadeirasEsq,
            self.imagemCadeirasDir,
            self.imagemCadeirasDir,
            self.imagemCadeirasDir,
            self.imagemCadeirasDir,
            self.imagemMesinha,
            self.imagemMesinha,
            self.imagemMesinha,
            self.imagemMesinha,
            self.imagemUpHolst,
            self.imagemUpHolst,
            self.imagemBauAberto
            
            ]

    def colocar(self, superficie):
        for i in range (0, len(self.rects)):
            superficie.blit(self.imagens[i], self.rects[i])

    def checaColisoes(self, player):
        pass