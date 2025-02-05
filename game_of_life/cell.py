import pygame

from game_of_life.state import State

class Cell:

    def __init__(self,
                 tile_size: int,
                 loc_x: int, loc_y: int, 
                 state: State) -> None:
        self._tile_size = tile_size
        self._loc_x = loc_x
        self._loc_y = loc_y
        self._state = state
        self._neighbours: list[Cell] = []
    
    @property
    def loc_x(self) -> int:
        return(self._loc_x)
    
    @property
    def loc_y(self) -> int:
        return(self._loc_y)
    
    @property
    def state(self) -> State:
        return(self._state)

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the cell, dead of alive."""
        size = self._tile_size
        rectangle = pygame.Rect(self._loc_x * size, self._loc_y * size,
                                size, size)
        if self._state == State.LIVE:
            pygame.draw.rect(screen, (0,0,0), rectangle)
        else:
            pygame.draw.rect(screen, (255,255,255), rectangle)

    ### Game logic section ###

    def find_neighbours(self, list_of_cells: list['Cell']) -> None:
        """Finds cells directly adjacent to this cell."""

        # The neighbours list must be re-established every time, because
        # the cells that comprise it may change state.
        self._neighbours = []

        for other_cell in list_of_cells:

            if other_cell.loc_x == self._loc_x - 1:
                if other_cell.loc_y == self._loc_y - 1:
                    self._neighbours.append(other_cell)
                elif other_cell.loc_y == self._loc_y:                        
                    self._neighbours.append(other_cell)
                elif other_cell.loc_y == self._loc_y + 1:
                    self._neighbours.append(other_cell)
                    
            elif other_cell.loc_x == self._loc_x:
                if other_cell.loc_y == self._loc_y - 1:
                    self._neighbours.append(other_cell)
                elif other_cell.loc_y == self._loc_y + 1:
                    self._neighbours.append(other_cell)
                    
            elif other_cell.loc_x == self._loc_x + 1:
                if other_cell.loc_y == self._loc_y - 1:
                    self._neighbours.append(other_cell)
                elif other_cell.loc_y == self._loc_y:
                    self._neighbours.append(other_cell)
                elif other_cell.loc_y == self._loc_y + 1:
                    self._neighbours.append(other_cell)

    def transition(self) -> State:
        """Applies the transition mechanism."""

        # Step 1: counts the number of live neighbouring cells.
        alive = 0
        for cell in self._neighbours:
            if cell.state == State.LIVE:
                alive = alive + 1

        # Applies the transition mechanism, given a cell's current state.
        if self._state == State.LIVE:
            if (alive <= 1) or (alive >= 4):
                return State.DEAD
            else:
                return State.LIVE
        elif self._state == State.DEAD:
            if alive == 3:
                return State.LIVE
            else:
                return State.DEAD