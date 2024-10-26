# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    #Initiate pygame and set the parameters for the screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    #Set clock variable and delta to 0
    clock = pygame.time.Clock()
    

    #Create groups for updatable and drawable objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Set containers of objects
    Player.containers = (updatable,drawable)

    #Instantiate a Player in a player variable
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    dt = 0

    #Initiate Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)
        
        
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()