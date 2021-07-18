import pygame
from pygame.locals import *
import config 

class Rectangle:
    def __init__(self, start_row, start_column, w_column, h_row, app):
        self.app = app
        self.border = 3
        self.color = config.COLOR_INACTIVE
        self.start_row = start_row
        self.start_column = start_column
        self.w_column = w_column  
        self.h_row = h_row
        self.set_size()

    def set_size(self):
        if self.h_row > 1:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + ((self.w_column -1 ) * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + (self.start_row * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - (self.border * 2), ((self.h_row * config.bheight) - self.border))
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + (self.start_row * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))

    def draw(self):
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)