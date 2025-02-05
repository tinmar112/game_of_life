from game_of_life.cell import Cell
from game_of_life.game import Game
from game_of_life.state import State

def cell_init(game: Game, live_cells: list[tuple[int,int]]) -> None:
    for i in range (game.window_width):
        for j in range(game.window_height):
            if (i,j) in live_cells:
                cell = Cell(game.tile_size,i,j, State.LIVE)
                game.add(cell)
            else:
                cell = Cell(game.tile_size,i,j, State.DEAD)
                game.add(cell)