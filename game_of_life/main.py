import pygame

from game_of_life.arguments import arguments
from game_of_life.cell import Cell
from game_of_life.cell_init import cell_init
from game_of_life.game import Game
from game_of_life.read_write import read_pattern

def main() -> None:

    args = arguments()

    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((20*args.width,20*args.height))
    game = Game(20,args.width,args.height)
    initial_live_cells = read_pattern(args.initial_file)
    cell_init(game,initial_live_cells)

    running = True

    while running:

        clock.tick(args.fps)

        game.draw(screen)
        pygame.display.update()

        # Finding neighbours and transitioning for cells.
        new_objects: list[Cell] = []
        for cell in game.cells:
            cell.find_neighbours(game.cells)
            next_state = cell.transition()           
            new_objects.append(Cell(game._tile_size,cell._loc_x,cell._loc_y,next_state))
        game.cells = new_objects
    
    pygame.quit()