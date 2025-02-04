import pygame

from game_of_life.cell import Cell

class Game:

    def __init__(self,
                 tile_size: int, 
                 window_width: int, 
                 window_height: int) -> None:
        self._tile_size = tile_size
        self._window_width = window_width
        self._window_height = window_height
        self._cells: list[Cell] = []
    
    @property
    def cells(self) -> list[Cell]:
        return(self._cells)
    
    @cells.setter
    def cells(self, new_cells_list: list[Cell]) -> None:
        self._cells = new_cells_list
    
    def draw(self,screen: pygame.Surface) -> None:
        for cell in self._cells:
            cell.draw(screen)
    
    def add_cell(self,new_cell: Cell) -> None:
        self._cells.append(new_cell)   