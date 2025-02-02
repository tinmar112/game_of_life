import pygame

from game_of_life.game import Game

class Board(Game):

    def __init__(self, 
                 tile_size: int, 
                 window_width: int, 
                 window_height: int, 
                 colour : tuple[int,int,int]) -> None:
        Game.__init__(self, tile_size, window_width, window_height)
        self._colour = colour

    def draw(self,screen: pygame.Surface) -> None:
        rectangle = pygame.Rect(0,0,
                                self._window_width * self._tile_size,
                                self._window_height * self._tile_size)
        pygame.draw.rect(screen, self._colour, rectangle)
