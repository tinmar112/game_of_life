import pygame

from game_of_life.cell import Cell
from game_of_life.state import State

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
    
    @property
    def live_cells(self) -> list[tuple[int,int]]:
        live_cells: list[tuple[int,int]] = []
        for cell in self._cells:
            if cell._state == State.LIVE:
                live_cells.append((cell._loc_x,cell._loc_y))
        return live_cells
    
    def draw(self,screen: pygame.Surface) -> None:
        for cell in self._cells:
            cell.draw(screen)
    
    def add_cell(self,new_cell: Cell) -> None:
        self._cells.append(new_cell)   