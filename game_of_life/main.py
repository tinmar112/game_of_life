import copy
import pygame

from game_of_life.board import Board
from game_of_life.cell import Cell
from game_of_life.game import Game
from game_of_life.game import GameObject
from game_of_life.state import State

def main() -> None:

    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((20*40,20*20))
    game = Game(20,40,20)
    board = Board(game,(255,255,255))
    game.add_object(board)
    board.cell_init(game)

    for elt in game.objects:
        if isinstance(elt,Cell):
            if (elt._loc_x == 3 and elt._loc_y == 3):
                elt._state = State.LIVE
            elif (elt._loc_x == 4 and elt._loc_y == 3):
                elt._state = State.LIVE
            elif (elt._loc_x == 5 and elt._loc_y == 3):
                elt._state = State.LIVE
            elif (elt._loc_x == 5 and elt._loc_y == 2):
                elt._state = State.LIVE
            elif (elt._loc_x == 4 and elt._loc_y == 1):
                elt._state = State.LIVE

    game.draw(screen)

    running = True

    while running:

        clock.tick(5)

        # Finding neighbours and transitioning for cells.
        new_objects: list[GameObject] = [board]
        for cell in game.objects:
            if isinstance(cell,Cell):
                cell.find_neighbours(game.objects)
                next_state = cell.transition()           
                new_objects.append(Cell(game,cell._loc_x,cell._loc_y,next_state))
        game.objects = new_objects

        game.draw(screen)
        pygame.display.update()
    
    pygame.quit()