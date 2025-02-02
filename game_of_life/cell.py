import pygame

from game_of_life.game import Game

class Cell(Game):

    def __init__(self, 
                 tile_size: int, 
                 window_width: int, 
                 window_height: int, 
                 loc_x: int, loc_y: int, 
                 colour: tuple[int,int,int]) -> None:
        Game.__init__(self, tile_size, window_width, window_height)
        self._loc_x = loc_x
        self._loc_y = loc_y
        self._colour = colour
        self._neighbours: list[Cell] = []
    
    @property
    def neighbours_count(self) -> int:
        return(len(self._neighbours))
    
    def add_neighbour(self, new_neighbour: 'Cell') -> None:
        self._neighbours.append(new_neighbour)
    
    def rm_neighbour(self, neighbour: 'Cell') -> None:
        self._neighbours.remove(neighbour)
    
    def transition(self):
        pass

    def draw(self,screen: pygame.Surface) -> None:
        size = self._tile_size
        rectangle = pygame.Rect(self._loc_x * size, self._loc_y * size,
                                size, size)
        pygame.draw.rect(screen, self._colour, rectangle)