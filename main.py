import pygame
from pygame.locals import *

from models.Player import Player

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1366, 768])

player = Player()
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    # screen.fill((255, 255, 255))

    # Draw the player on the screen
    screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()