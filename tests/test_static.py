from game_of_life.cell_init import cell_init
from game_of_life.game import Game

def test_block():

    game = Game(20,40,30)
    cell_init(game,[(0, 0), (1, 0), (0, 1), (1, 1)])
    game.transition()
    # Checking if elements are the same, regardless of order. 
    # (There are not repetitions.)
    assert set(game.live_cells) == set([(0, 0), (1, 0), (0, 1), (1, 1)])

def test_beehive():

    game = Game(20,40,30)
    cell_init(game,[(1, 0), (2, 0), (0, 1), (3, 1), (1, 2), (2, 2)])
    game.transition()
    # Checking if elements are the same, regardless of order. 
    # (There are not repetitions.)
    assert set(game.live_cells) == set([(1, 0), (2, 0), (0, 1), (3, 1), (1, 2), (2, 2)])