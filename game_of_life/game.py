import pygame

class Game:

    def __init__(self,
                 tile_size: int, 
                 window_width: int, 
                 window_height: int) -> None:
        self._tile_size = tile_size
        self._window_width = window_width
        self._window_height = window_height
        self._objects: list = []
    
    def draw(self,screen: pygame.Surface) -> None:
        for obj in self._objects:
            obj.draw(screen)
    
    def add_object(self,new_object: 'Game') -> None:
        self._objects.append(new_object)   