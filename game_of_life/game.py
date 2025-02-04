import pygame

from game_of_life.game_object import GameObject

class Game:

    def __init__(self,
                 tile_size: int, 
                 window_width: int, 
                 window_height: int) -> None:
        self._tile_size = tile_size
        self._window_width = window_width
        self._window_height = window_height
        self._objects: list[GameObject] = []
    
    @property
    def objects(self) -> list[GameObject]:
        return(self._objects)
    
    @objects.setter
    def objects(self, new_objects_list: list[GameObject]) -> None:
        self._objects = new_objects_list
    
    def draw(self,screen: pygame.Surface) -> None:
        for obj in self._objects:
            obj.draw(screen)
    
    def add_object(self,new_object: GameObject) -> None:
        self._objects.append(new_object)   