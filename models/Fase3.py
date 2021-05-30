from time import sleep
import pygame

class Fase3:
    def __init__(self):
        self.objetos = []

        self.proximaFase = False
        self.encontrouFogao = False
        self.encontrouLouca = False
        self.puzzleResolvido = False
        self.abriuBau = False
        self.pegouChave = False

        self.mostrarCifra = False
        self.mostrarMapa = False

        self.superficie = None

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

        self.imagemFogaoApagado = pygame.image.load('./imagens/fase3/fogao.png')
        self.imagemFogao = pygame.image.load('./imagens/fase3/fogao-aceso.png')

        self.rectFogao = self.imagemFogao.get_rect()
        self.rectFogao.centerx=142
        self.rectFogao.centery=64

        self.rectFogaoApagado = self.imagemFogaoApagado.get_rect()
        self.rectFogaoApagado.centerx=142
        self.rectFogaoApagado.centery=64

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
        self.rectVaso.centerx=350
        self.rectVaso.centery=90


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


        self.imagemFrascoAmarelo = pygame.image.load('./imagens/fase3/frascos/frasco-amarelo.png')
        self.imagemFrascoAzul = pygame.image.load('./imagens/fase3/frascos/frasco-azul.png')
        self.imagemFrascoPreto = pygame.image.load('./imagens/fase3/frascos/frasco-preto.png')
        self.imagemFrascoRoxo = pygame.image.load('./imagens/fase3/frascos/frasco-roxo.png')
        self.imagemFrascoRoxo2 = pygame.image.load('./imagens/fase3/frascos/frasco-roxo-2.png')
        self.imagemFrascoVerde = pygame.image.load('./imagens/fase3/frascos/frasco-verde.png')
        self.imagemFrascoVermelho = pygame.image.load('./imagens/fase3/frascos/frasco-vermelho.png')
        self.imagemFrascoVermelho2 = pygame.image.load('./imagens/fase3/frascos/frasco-vermelho2.png')

        self.rectFrascoAmarelo = self.imagemFrascoAmarelo.get_rect()
        self.rectFrascoAmarelo.centerx=718
        self.rectFrascoAmarelo.centery=214

        self.rectFrascoAzul = self.imagemFrascoAzul.get_rect()
        self.rectFrascoAzul.centerx=532
        self.rectFrascoAzul.centery=222

        self.rectFrascoPreto = self.imagemFrascoPreto.get_rect()
        self.rectFrascoPreto.centerx=730
        self.rectFrascoPreto.centery=267

        self.rectFrascoRoxo = self.imagemFrascoRoxo.get_rect()
        self.rectFrascoRoxo.centerx=83
        self.rectFrascoRoxo.centery=267

        self.rectFrascoRoxo2 = self.imagemFrascoRoxo2.get_rect()
        self.rectFrascoRoxo2.centerx=529
        self.rectFrascoRoxo2.centery=266

        self.rectFrascoVerde = self.imagemFrascoVerde.get_rect()
        self.rectFrascoVerde.centerx=283
        self.rectFrascoVerde.centery=226

        self.rectFrascoVermelho = self.imagemFrascoVermelho.get_rect()
        self.rectFrascoVermelho.centerx=101
        self.rectFrascoVermelho.centery=219

        self.rectFrascoVermelho2 = self.imagemFrascoVermelho2.get_rect()
        self.rectFrascoVermelho2.centerx=300
        self.rectFrascoVermelho2.centery=260


        self.imagemMapaEnrolado = pygame.image.load('./imagens/fase3/mapa-enrolado.png')
        self.rectMapaEnrolado = self.imagemMapaEnrolado.get_rect()
        self.rectMapaEnrolado.centerx=675
        self.rectMapaEnrolado.centery=80

        self.imagemOpaca = pygame.image.load('./imagens/fase3/imagemOpaca.png')
        self.rectOpaca = self.imagemOpaca.get_rect()
        self.rectOpaca.centerx=400
        self.rectOpaca.centery=200

        self.imagemMapa = pygame.image.load('./imagens/fase3/mapa-final-2.png')
        self.rectMapa = self.imagemMapa.get_rect()
        self.rectMapa.centerx=400
        self.rectMapa.centery=200

        self.imagemCifra = pygame.image.load('./imagens/fase3/cifra.png')
        self.rectCifra = self.imagemCifra.get_rect()
        self.rectCifra.centerx=400
        self.rectCifra.centery=200


        self.rects =[
            self.rectParede,
            self.rectPorta,
            self.rectCadeado,
            self.rectDishes2,
            self.rectDishes3,
            self.rectMapaEnrolado,
            self.rectDishes1,
            self.rectArmario1,
            self.rectArmario2,
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
            self.rectFrascoAmarelo,
            self.rectFrascoAzul,
            self.rectFrascoPreto,
            self.rectFrascoRoxo,
            self.rectFrascoRoxo2,
            self.rectFrascoVerde,
            self.rectFrascoVermelho,
            self.rectFrascoVermelho2,
            
            ]

        self.imagens = [
            self.imagemParede,
            self.imagemPorta,
            self.imagemCadeado,
            self.imagemDishes2,
            self.imagemDishes3,
            self.imagemMapaEnrolado,
            self.imagemDishes1,
            self.imagemArmario1,
            self.imagemArmario2,
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
            self.imagemBauAberto,
            self.imagemFrascoAmarelo,
            self.imagemFrascoAzul,
            self.imagemFrascoPreto,
            self.imagemFrascoRoxo,
            self.imagemFrascoRoxo2,
            self.imagemFrascoVerde,
            self.imagemFrascoVermelho,
            self.imagemFrascoVermelho2,
            
            ]

    def colocar(self, superficie):
        self.superficie = superficie
        for i in range (0, len(self.rects)):
            superficie.blit(self.imagens[i], self.rects[i])
        
        if self.encontrouFogao:
            superficie.blit(self.imagemFogaoApagado, self.rectFogao)
        else:
            superficie.blit(self.imagemFogao, self.rectFogao)

        if self.mostrarMapa:
            superficie.blit(self.imagemOpaca, self.rectOpaca)
            superficie.blit(self.imagemMapa, self.rectMapa)

        if self.mostrarCifra:
            superficie.blit(self.imagemOpaca, self.rectOpaca)
            superficie.blit(self.imagemCifra, self.rectCifra)

    def checaColisoes(self, player):
        if self.rectFogao.collidelist([player.rect]) >= 0:
            self.encontrouFogao = True
            self.mostrarCifra = not self.mostrarCifra
            self.apagarFogao()
        if self.rectDishes1.collidelist([player.rect]) >= 0 and self.encontrouFogao:
            self.encontrouLouca = True
            self.empurrarDishes()
        if self.rectMapaEnrolado.collidelist([player.rect]) >=0 and self.encontrouLouca:
            self.mostrarMapa = not self.mostrarMapa

    def apagarFogao(self):
        self.superficie.blit(self.imagemFogaoApagado, self.rectFogao)
    
    def empurrarDishes(self):
        for i in range(75, 150):
            self.rectDishes1.bottom = i
        sleep(0.2)
        for i in range(675, 750):
            self.rectDishes1.right = i
