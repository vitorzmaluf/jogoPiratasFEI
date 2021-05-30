import pygame, sys
from pygame.locals import *
from time import sleep
import random


from models.Player import Player
from models.FaseFinal import FaseFinal
from models.Boss import Boss
from models.Fase1 import Fase1
from models.Fase2 import Fase2
from models.Fase3 import Fase3

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

pos_player = [400, 300]



def pirata():
    pygame.init()
    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("ARG!")

    player = Player()
    boss = Boss()
    fase1 = Fase1()
    fase2= Fase2()
    fase3 = Fase3()
    fasefinal = FaseFinal()

    bossCount = 0

    imagemFundo = pygame.image.load('./imagens/cenario/bkgrnd.png')
    # Run until the user asks to quit
    running = True

    fases = [fase1, fase2, fase3, fasefinal]
    faseAtual = fases[0]
    while running:
        if faseAtual.proximaFase:
            sleep(2);##TODO verificar se é a ultima fase
            faseAtual = None
            fases.pop(0)
            faseAtual = fases[0]
        
        player.movimento(faseAtual.objetos)#TODO nao deixar jogador atravessar objetos

        # Did the user click the window close button?
        keys = pygame.key.get_pressed()
        if(player.livre):
            if keys[K_LEFT]:
                player.rect.left -= player.velocidade
            elif keys[K_RIGHT]:
                player.rect.right += player.velocidade
            if keys[K_UP]:
                player.rect.top -= player.velocidade
            elif keys[K_DOWN]:
                player.rect.bottom += player.velocidade
            # if keys[K_SPACE]:
            #     # sleep(1)
            #     # faseAtual.checaColisoes(player) 

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_LEFT:
                #     player.rect.left -= player.velocidade
                # if event.key == pygame.K_RIGHT:
                #     player.rect.right += player.velocidade
                # if event.key == pygame.K_UP:
                #     player.rect.top -= player.velocidade
                # if event.key == pygame.K_DOWN:
                #     player.rect.bottom += player.velocidade
                
                #Evento de ação: checa colisões com os objetos chave
                if event.key == pygame.K_SPACE:
                    if(faseAtual != fases[3]):
                        faseAtual.checaColisoes(player)
                        print('test')
                    else:
                        print('atirou')

                    # while pygame.key.get_pressed()[pygame.K_SPACE]:
                    #     print("espaco apertado")

                screen.fill((0,0,0))
                    
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(imagemFundo, [0, 0])
        faseAtual.colocar(screen)
        player.colocar(screen)

        if(faseAtual == fases[3]):
            if(boss.life > 0):
                boss.colocar(screen, bossCount//24)
                boss.movimento()
                if(boss.bossState == 0):
                    #retornar para posicao original
                    if(boss.rect.left < 650):
                        boss.rect.right += 2
                    else:
                        ran = random.randint( 0, 4000 )
                        if(ran < 100):
                            boss.velocidade = -boss.velocidade
                            ran_atk = random.randint( 0, 200 )
                            if(ran_atk < 30):
                                boss.bossState = 1

                boss.rect.top += boss.velocidade

                if(boss.bossState == 1):
                    boss.rect.left -= 2

                    if(boss.rect.left < 40):
                        boss.bossState = 0
                bossCount += 1
                if(bossCount > 144):
                    bossCount = 0
            
            #Morreu
            else:
                boss.bossState = 2




            

        pygame.display.update()

        # Fill the background with white
        # screen.fill((255, 255, 255))

        # Draw the player on the screen
        # screen.blit(player.surf, (pos_player[0], pos_player[1]))

        # Draw a solid blue circle in the center
        # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        # pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()

pirata()