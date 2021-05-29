from models.Fase1 import Fase1
from models.Fase2 import Fase2
import pygame, sys
from pygame.locals import *


from models.Player import Player
from models.FaseFinal import FaseFinal
#from models.Fase1 import Fase1

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

pos_player = [400, 300]



def pirata():
    pygame.init()
    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Pirata")

    player = Player()
    fase1 = Fase1()
    fase2= Fase2()
    fasefinal = FaseFinal()

    imagemFundo = pygame.image.load('./imagens/cenario/bkgrnd.png')
    # Run until the user asks to quit
    running = True

    while running:
        player.movimento()
        # Did the user click the window close button?

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.rect.left -= player.velocidade
                if event.key == pygame.K_RIGHT:
                    player.rect.right += player.velocidade
                if event.key == pygame.K_UP:
                    player.rect.top -= player.velocidade
                if event.key == pygame.K_DOWN:
                    player.rect.bottom += player.velocidade

                screen.fill((0,0,0))
                    
            if event.type == pygame.QUIT:
                running = False
        
        screen.blit(imagemFundo, [0, 0])
        #fase2.colocar(screen)
        fasefinal.colocar(screen)
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