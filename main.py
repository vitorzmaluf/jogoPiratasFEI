import pygame, sys
from pygame.locals import *
from time import sleep


from models.Player import Player
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
    fase1 = Fase1()
    fase2= Fase2()
    fase3 = Fase3()

    imagemFundo = pygame.image.load('./imagens/cenario/bkgrnd.png')
    # Run until the user asks to quit
    running = True

    fases = [fase1, fase2, fase3]
    faseAtual = fases[0]
    while running:
        i = 0
        if faseAtual.proximaFase:
            sleep(2);##TODO verificar se é a ultima fase
            i += 1
            faseAtual.__del__()
            faseAtual = fases[i]
        
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
                    faseAtual.checaColisoes(player)
                    # while pygame.key.get_pressed()[pygame.K_SPACE]:
                    #     print("espaco apertado")

                screen.fill((0,0,0))
                    
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(imagemFundo, [0, 0])
        faseAtual.colocar(screen)
        player.colocar(screen)

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