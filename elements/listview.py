import pygame
from pygame.locals import *
import config 
import numpy

class Search_Listview:
 
    def __init__(self, start_row, start_column, w_column, h_row, app, data, index):
        self.fontname = 'fonts/SEGOEUI.TTF'
        self.fontsize = 24
        self.border = 3
        self.set_font()

        self.app = app
        self.start_row = start_row
        self.start_column = start_column
        self.w_column = w_column  
        self.h_row = h_row
        self.set_size()

        self.color = config.COLOR_INACTIVE

        self.data = data
        self.index = index * 5
        self.number = numpy.empty(len(self.data), dtype=object) 
        self.number_rect = numpy.empty(len(self.data), dtype=object)
        self.product_name = numpy.empty(len(self.data), dtype=object) 
        self.product_rect = numpy.empty(len(self.data), dtype=object)
        self.quantity = numpy.empty(len(self.data), dtype=object)
        self.quantity_rect = numpy.empty(len(self.data), dtype=object) 
        self.locker_number = numpy.empty(len(self.data), dtype=object)
        self.locker_rect = numpy.empty(len(self.data), dtype=object) 
        self.render()

    def set_size(self):
        if self.h_row > 1:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + ((self.w_column -1 ) * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
            else: 
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - (self.border * 2), ((self.h_row * config.bheight) - self.border))
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))
    
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        if len(self.data) - self.index >= 5 :
            self.list_index = 5
        else:
            self.list_index = len(self.data) - self.index
        for x in range(self.list_index):
            self.number[x + self.index] = self.font.render(str((x + self.index) +1), True, self.color)
            self.number_rect[x + self.index] = self.number[x + self.index].get_rect()
            self.number_rect[x + self.index].topleft = ((1 * config.bwidth) + config.margin + 15 ,((x + 5) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.product_name[x + self.index] = self.font.render(self.data[x + self.index]['product_name'][:10], True, self.color)
            self.product_rect[x + self.index] = self.product_name[x + self.index].get_rect()
            self.product_rect[x + self.index].topleft = ((2 * config.bwidth) + config.margin + 15 ,((x + 5) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.quantity[x + self.index] = self.font.render(self.data[x + self.index]['locker_number'], True, self.color)
            self.quantity_rect[x + self.index] = self.quantity[x + self.index].get_rect()
            self.quantity_rect[x + self.index].topleft = ((6 * config.bwidth) + config.margin + 15 ,((x + 5) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.locker_number[x + self.index] = self.font.render(self.data[x + self.index]['locker_number'], True, self.color)
            self.locker_rect[x + self.index] = self.locker_number[x + self.index].get_rect()
            self.locker_rect[x + self.index].topleft = ((7 * config.bwidth) + config.margin + 15 ,((x + 5) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

    def draw(self):
        if len(self.data) - self.index >= 5 :
            self.list_index = 5
        else:
            self.list_index = len(self.data) - self.index
        # Blit the text.
        for x in range(self.list_index):
            self.app.blit(self.number[x + self.index], self.number_rect[x + self.index])
            self.app.blit(self.product_name[x + self.index], self.product_rect[x + self.index])
            self.app.blit(self.quantity[x + self.index], self.quantity_rect[x + self.index])
            self.app.blit(self.locker_number[x + self.index], self.locker_rect[x + self.index])
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)