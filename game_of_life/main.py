import logging
import pygame
import sys

from game_of_life.arguments import arguments
from game_of_life.cell_init import cell_init
from game_of_life.game import Game
from game_of_life.logging import set_logger
from game_of_life.read_write import read_pattern, write_pattern

def main() -> None:
    """Main function of the Game of Life"""

    args = arguments() # Parsing command line arguments.
    logger = logging.getLogger("game_of_life")
    set_logger(logger,args) # Setting up logging messages.

    # Game initialisation using arguments.
    game = Game(20,args.width,args.height)
    cell_init(game,read_pattern(args.initial_file))
    logger.info(f'Game initialised from file {args.initial_file} .')
    
    if args.display: # A display flag prompts Pygame.
        
        pygame.init()
        logger.warning('Pygame has been launched.')
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((20*args.width,20*args.height))
        
        # This game will run until a specified number of transitions is hit.
        # Hence, it will be using a for loop.
        for i in range(args.max):

            # Display comes first so that the initial figure gets displayed.
            game.draw(screen)
            pygame.display.set_caption(f"Game of Life : step {i}")
            pygame.event.pump() # I am using pump() to force a window title update.
            pygame.display.update()

            clock.tick(args.fps)
            game.transition()
            logger.info('Game transition occurred.')

        write_pattern(args.output_file,game.live_cells)
        logger.info(f'Final pattern has been encoded into {args.output_file} .')

        pygame.quit()
        logger.warning('Pygame has been closed.')
        sys.exit()
    
    
    else: # If Pygame has not been asked for.

        for i in range (args.max):

            game.transition()
            logger.info('Game transition occurred.')

        write_pattern(args.output_file,game.live_cells)
        logger.info(f'Final pattern has been encoded into {args.output_file} .')

        sys.exit()