import pygame
from pygame.locals import *

class Button():
    def __init__(self, screen, color, x, y, w, h):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def color(self, color):
        self.color = color
        return self.Rect()

    def Rect(self):
        return pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.w, self.h))