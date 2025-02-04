import pygame

from game_of_life.cell import Cell
from game_of_life.game import Game
from game_of_life.game_object import GameObject
from game_of_life.state import State

class Board(GameObject):

    def __init__(self, game: Game, colour: tuple[int,int,int]) -> None:
        GameObject.__init__(self)
        self._tile_size = game._tile_size
        self._window_height = game._window_height
        self._window_width = game._window_width
        self._colour = colour

    def draw(self,screen: pygame.Surface) -> None:
        rectangle = pygame.Rect(0,0,
                                self._window_width * self._tile_size,
                                self._window_height * self._tile_size)
        pygame.draw.rect(screen, self._colour, rectangle)

    def cell_init(self, game: Game):
        for i in range (self._window_width):
            for j in range(self._window_height):
                cell = Cell(game,i,j, State.DEAD)
                game.add_object(cell)