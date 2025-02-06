from game_of_life.cell_init import cell_init
from game_of_life.game import Game


# Oscillators with period 2
def test_blinker():

    game = Game(20,40,30)
    cell_init(game,[(0, 0), (1, 0), (2, 0)])
    for i in range(2):
        game.transition()
    # Checking if elements are the same, regardless of order. 
    # (There are not repetitions.)
    assert set(game.live_cells) == set([(0, 0), (1, 0), (2, 0)])

def test_toad():

    game = Game(20,40,30)
    cell_init(game,[(1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1)])
    for i in range(2):
        game.transition()
    # Checking if elements are the same, regardless of order. 
    # (There are not repetitions.)
    assert set(game.live_cells) == set([(1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1)])

# Oscillator with period of 3
def test_pulsar():

    game = Game(20,40,30)
    cell_init(game,[(3, 0),
 (6, 0),
 (3, 1),
 (6, 1),
 (2, 2),
 (3, 2),
 (6, 2),
 (7, 2),
 (0, 3),
 (1, 3),
 (2, 3),
 (7, 3),
 (8, 3),
 (9, 3),
 (0, 6),
 (1, 6),
 (2, 6),
 (7, 6),
 (8, 6),
 (9, 6),
 (2, 7),
 (3, 7),
 (6, 7),
 (7, 7),
 (3, 8),
 (6, 8),
 (3, 9),
 (6, 9)])
    for i in range(3):
        game.transition()
    # Checking if elements are the same, regardless of order. 
    # (There are not repetitions.)
    assert set(game.live_cells) == set([(3, 0),
 (6, 0),
 (3, 1),
 (6, 1),
 (2, 2),
 (3, 2),
 (6, 2),
 (7, 2),
 (0, 3),
 (1, 3),
 (2, 3),
 (7, 3),
 (8, 3),
 (9, 3),
 (0, 6),
 (1, 6),
 (2, 6),
 (7, 6),
 (8, 6),
 (9, 6),
 (2, 7),
 (3, 7),
 (6, 7),
 (7, 7),
 (3, 8),
 (6, 8),
 (3, 9),
 (6, 9)])
    
# Oscillator with period of 15
def test_pentadecathlon():

    game = Game(20,40,30)
    cell_init(game,[(2, 0),
 (7, 0),
 (0, 1),
 (1, 1),
 (3, 1),
 (4, 1),
 (5, 1),
 (6, 1),
 (8, 1),
 (9, 1),
 (2, 2),
 (7, 2)]
)
    for i in range(15):
        game.transition()
    # Checking if elements are the same, regardless of order. 
    # (There are not repetitions.)
    assert set(game.live_cells) == set([(2, 0),
 (7, 0),
 (0, 1),
 (1, 1),
 (3, 1),
 (4, 1),
 (5, 1),
 (6, 1),
 (8, 1),
 (9, 1),
 (2, 2),
 (7, 2)]
)