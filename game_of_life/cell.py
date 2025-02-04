import pygame

from game_of_life.game import Game
from game_of_life.game_object import GameObject
from game_of_life.state import State

class Cell(GameObject):

    def __init__(self, 
                 game: Game,
                 loc_x: int, loc_y: int, 
                 state: State) -> None:
        self._tile_size = game._tile_size
        self._window_width = game._window_width
        self._window_height = game._window_height
        self._loc_x = loc_x
        self._loc_y = loc_y
        self._neighbours: list[Cell] = []
        self._state = state # Initially, a cell is alive.
    
    @property
    def neighbours_count(self) -> int:
        return(len(self._neighbours))
    
    def add_neighbour(self, new_neighbour: 'Cell') -> None:
        self._neighbours.append(new_neighbour)
    
    def rm_neighbour(self, neighbour: 'Cell') -> None:
        self._neighbours.remove(neighbour)
    
    def draw(self, screen: pygame.Surface) -> None:
        if self._state == State.LIVE: # Only live cells get drawn.
            size = self._tile_size
            rectangle = pygame.Rect(self._loc_x * size, self._loc_y * size,
                                    size, size)
            pygame.draw.rect(screen, (0,0,0), rectangle)

    ### Game logic section ###

    def find_neighbours(self, list_of_objects: list[GameObject]) -> None:
        """Finds cells directly adjacent to this cell."""

        # The neighbours list must be re-established every time, because
        # the cells that comprise it may change state.
        self._neighbours = []

        for other_cell in list_of_objects:

            if isinstance(other_cell,Cell): # We are not checking whether
                                            # the board is a neighbour.
                if other_cell._loc_x == self._loc_x - 1:
                    if other_cell._loc_y == self._loc_y - 1:
                        self._neighbours.append(other_cell)
                    elif other_cell._loc_y == self._loc_y:
                        self._neighbours.append(other_cell)
                    elif other_cell._loc_y == self._loc_y + 1:
                        self._neighbours.append(other_cell)
                    
                elif other_cell._loc_x == self._loc_x:
                    if other_cell._loc_y == self._loc_y - 1:
                            self._neighbours.append(other_cell)
                    elif other_cell._loc_y == self._loc_y + 1:
                            self._neighbours.append(other_cell)
                    
                elif other_cell._loc_x == self._loc_x + 1:
                    if other_cell._loc_y == self._loc_y - 1:
                        self._neighbours.append(other_cell)
                    elif other_cell._loc_y == self._loc_y:
                        self._neighbours.append(other_cell)
                    elif other_cell._loc_y == self._loc_y + 1:
                        self._neighbours.append(other_cell)

    def transition(self) -> State:
        """Applies the transition mechanism."""

        # Step 1: counts the number of live neighbouring cells.
        alive = 0
        for cell in self._neighbours:
            if cell._state == State.LIVE:
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