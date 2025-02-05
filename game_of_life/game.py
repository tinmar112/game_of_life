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
    def tile_size(self) -> int:
        return (self._tile_size)
    
    @property
    def window_width(self) -> int:
        return (self._window_width)

    @property
    def window_height(self) -> int:
        return (self._window_height)

    @property
    def live_cells(self) -> list[tuple[int,int]]:
        live_cells: list[tuple[int,int]] = []
        for cell in self._cells:
            if cell.state == State.LIVE:
                live_cells.append((cell.loc_x,cell.loc_y))
        return live_cells
    
    def draw(self,screen: pygame.Surface) -> None:
        for cell in self._cells:
            cell.draw(screen)
    
    def add(self,new_cell: Cell) -> None:
        self._cells.append(new_cell)
    
    def transition(self) -> None:
        # Finds neighbours and transitions each cell.
        new_objects: list[Cell] = []
        for cell in self._cells:
            cell.find_neighbours(self._cells)
            next_state = cell.transition()           
            new_objects.append(Cell(self._tile_size,
                                    cell.loc_x,
                                    cell.loc_y,
                                    next_state))
        self._cells = new_objects