import enum

class State(enum.Enum):
    """State of cells: dead or alive"""
    DEAD = 0
    LIVE = 1