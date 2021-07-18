import pygame
from pygame.locals import *
import config 
import os 

class Image():
    """Create a image object."""
    
    def __init__(self, path, pos, app):
        self.path = path
        self.pos = pos
        self.app = app
        self._image_library = {}
        
        self.get_image()

    def get_image(self):
        self.image = self._image_library.get(self.path)
        if self.image == None:
                self.canonicalized_path = self.path.replace('/', os.sep).replace('\\', os.sep)
                self.image = pygame.image.load(self.canonicalized_path)
                self._image_library[self.path] = self.image

    def draw(self):
        self.app.blit(self.image, self.pos)