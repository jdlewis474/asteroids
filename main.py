import pygame
from constants import *
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    i=0
    player_one = player.Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    while i < 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player_one.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60)

if __name__ == "__main__":
    main()