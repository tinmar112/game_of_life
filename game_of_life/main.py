import pygame

from game_of_life.board import Board
from game_of_life.cell import Cell
from game_of_life.game import Game

def main() -> None:

    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((20*40,20*20))
    game_init = Game(20,40,20)
    board = Board(20,40,20,(255,255,255))
    cell = Cell(20,40,20,5,5,(0,0,0))

    game_init.add_object(board)
    game_init.add_object(cell)

    running = True

    while running:

        clock.tick()
        game_init.draw(screen)
        pygame.display.update()
    
    pygame.quit()