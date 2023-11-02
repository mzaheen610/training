import sys
import pygame

def run_game():
    #inititalize game screen
    #create a screen object
    pygame.init()

    screen = pygame.display.set_mode((1200, 800))

    bg_color = (2,30,0)
    pygame.display.set_caption("Alien Invasion")

    #starting main lop

    while True:

        #watch for keyboard/mouse events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.fill(bg_color)
        pygame.display.flip()

run_game()



