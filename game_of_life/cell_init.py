from game_of_life.cell import Cell
from game_of_life.game import Game
from game_of_life.state import State

def cell_init(game: Game, live_cells: list[tuple[int,int]]) -> None:
    # Increments start at -5 to give the board a buffer zone,
    # in case patterns evolve outside of the pygame display.
    for i in range (-5, game.window_width):
        for j in range(-5, game.window_height):
            if (i,j) in live_cells:
                game.add(Cell(game.tile_size,i,j, State.LIVE))
            else:
                game.add(Cell(game.tile_size,i,j, State.DEAD))