import pygame
import sys

from game_of_life.arguments import arguments
from game_of_life.cell_init import cell_init
from game_of_life.game import Game
from game_of_life.read_write import read_pattern, write_pattern

def main() -> None:

    args = arguments()

    game = Game(20,args.width,args.height)
    cell_init(game,read_pattern(args.initial_file))

    running = True
    counter, max = 0, args.max
    
    if args.display: # Display flag prompts Pygame.

        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((20*args.width,20*args.height))
        
        while running and (counter <= max):

            # Display comes first so that initial figure gets displayed.
            game.draw(screen)
            pygame.display.set_caption(f"Game of Life : step {counter}")
            pygame.event.pump()
            pygame.display.update()

            clock.tick(args.fps)
            game.transition()
            counter = counter + 1

        write_pattern(args.output_file,game.live_cells)

        pygame.quit()
        sys.exit()
    
    
    else:

        while running and (counter <= max):

            game.transition()
            counter = counter + 1

        write_pattern(args.output_file,game.live_cells)

        sys.exit()