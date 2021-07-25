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
        self.index = index * self.h_row
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
        if len(self.data) - self.index >= self.h_row:
            self.list_index = self.h_row
        else:
            self.list_index = len(self.data) - self.index
        for x in range(self.list_index):
            self.number[x + self.index] = self.font.render(str((x + self.index) +1), True, self.color)
            self.number_rect[x + self.index] = self.number[x + self.index].get_rect()
            self.number_rect[x + self.index].topleft = ((1 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.product_name[x + self.index] = self.font.render(self.data[x + self.index]['product_name'][:25] + "...", True, self.color)
            self.product_rect[x + self.index] = self.product_name[x + self.index].get_rect()
            self.product_rect[x + self.index].topleft = ((2 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.quantity[x + self.index] = self.font.render(self.data[x + self.index]['quantity'], True, self.color)
            self.quantity_rect[x + self.index] = self.quantity[x + self.index].get_rect()
            self.quantity_rect[x + self.index].topleft = ((6 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.locker_number[x + self.index] = self.font.render(self.data[x + self.index]['locker_number'], True, self.color)
            self.locker_rect[x + self.index] = self.locker_number[x + self.index].get_rect()
            self.locker_rect[x + self.index].topleft = ((7 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

    def draw(self):
        if len(self.data) - self.index >= self.h_row :
            self.list_index = self.h_row
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

class Productedit_Listview:
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
        self.index = index * self.h_row
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
        if len(self.data) - self.index > self.h_row :
            self.list_index = self.h_row
        else:
            self.list_index = len(self.data) - self.index
        for x in range(self.list_index):
            self.number[x + self.index] = self.font.render(str((x + self.index) +1), True, self.color)
            self.number_rect[x + self.index] = self.number[x + self.index].get_rect()
            self.number_rect[x + self.index].topleft = ((1 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.product_name[x + self.index] = self.font.render(self.data[x + self.index].product_name[:25], True, self.color)
            self.product_rect[x + self.index] = self.product_name[x + self.index].get_rect()
            self.product_rect[x + self.index].topleft = ((2 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.quantity[x + self.index] = self.font.render(self.data[x + self.index].quantity, True, self.color)
            self.quantity_rect[x + self.index] = self.quantity[x + self.index].get_rect()
            self.quantity_rect[x + self.index].topleft = ((5 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.locker_number[x + self.index] = self.font.render(self.data[x + self.index].locker_number, True, self.color)
            self.locker_rect[x + self.index] = self.locker_number[x + self.index].get_rect()
            self.locker_rect[x + self.index].topleft = ((6 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

    def draw(self):
        if len(self.data) - self.index > self.h_row :
            self.list_index = self.h_row
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

class Productadd_Listview:
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
        self.index = index * self.h_row
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
        if len(self.data) - self.index > self.h_row :
            self.list_index = self.h_row
        else:
            self.list_index = len(self.data) - self.index
        for x in range(self.list_index):
            self.number[x + self.index] = self.font.render(str((x + self.index) +1), True, self.color)
            self.number_rect[x + self.index] = self.number[x + self.index].get_rect()
            self.number_rect[x + self.index].topleft = ((1 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.product_name[x + self.index] = self.font.render(self.data[x + self.index].product_name[:25], True, self.color)
            self.product_rect[x + self.index] = self.product_name[x + self.index].get_rect()
            self.product_rect[x + self.index].topleft = ((2 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.quantity[x + self.index] = self.font.render(self.data[x + self.index].quantity, True, self.color)
            self.quantity_rect[x + self.index] = self.quantity[x + self.index].get_rect()
            self.quantity_rect[x + self.index].topleft = ((5 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.locker_number[x + self.index] = self.font.render(self.data[x + self.index].locker_number, True, self.color)
            self.locker_rect[x + self.index] = self.locker_number[x + self.index].get_rect()
            self.locker_rect[x + self.index].topleft = ((6 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

    def draw(self):
        if len(self.data) - self.index > self.h_row :
            self.list_index = self.h_row
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

class Useredit_Listview:
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
        self.index = index * self.h_row
        self.user_id = numpy.empty(len(self.data), dtype=object) 
        self.userid_rect = numpy.empty(len(self.data), dtype=object)
        self.user_name = numpy.empty(len(self.data), dtype=object) 
        self.username_rect = numpy.empty(len(self.data), dtype=object)
        self.user_lname = numpy.empty(len(self.data), dtype=object)
        self.userlname_rect = numpy.empty(len(self.data), dtype=object) 
        self.permission = numpy.empty(len(self.data), dtype=object)
        self.permission_rect = numpy.empty(len(self.data), dtype=object) 
        # self.locker_number = numpy.empty(len(self.data), dtype=object)
        # self.locker_rect = numpy.empty(len(self.data), dtype=object)
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
        if len(self.data) - self.index > self.h_row :
            self.list_index = self.h_row
        else:
            self.list_index = len(self.data) - self.index
        for x in range(self.list_index):
            # self.number[x + self.index] = self.font.render(str((x + self.index) +1), True, self.color)
            # self.number_rect[x + self.index] = self.number[x + self.index].get_rect()
            # self.number_rect[x + self.index].topleft = ((1 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.user_id[x + self.index] = self.font.render(self.data[x + self.index].user_id[:25], True, self.color)
            self.userid_rect[x + self.index] = self.user_id[x + self.index].get_rect()
            self.userid_rect[x + self.index].topleft = ((1 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.user_name[x + self.index] = self.font.render(self.data[x + self.index].user_name[:25], True, self.color)
            self.username_rect[x + self.index] = self.user_name[x + self.index].get_rect()
            self.username_rect[x + self.index].topleft = ((3 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.user_lname[x + self.index] = self.font.render(self.data[x + self.index].user_lname, True, self.color)
            self.userlname_rect[x + self.index] = self.user_lname[x + self.index].get_rect()
            self.userlname_rect[x + self.index].topleft = ((5 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.permission[x + self.index] = self.font.render(self.data[x + self.index].permission, True, self.color)
            self.permission_rect[x + self.index] = self.permission[x + self.index].get_rect()
            self.permission_rect[x + self.index].topleft = ((7 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            # self.locker_number[x + self.index] = self.font.render(self.data[x + self.index].locker, True, self.color)
            # self.locker_rect[x + self.index] = self.locker_number[x + self.index].get_rect()
            # self.locker_rect[x + self.index].topleft = ((7 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

    def draw(self):
        if len(self.data) - self.index > self.h_row :
            self.list_index = self.h_row
        else:
            self.list_index = len(self.data) - self.index
        # Blit the text.
        for x in range(self.list_index):
            self.app.blit(self.user_id[x + self.index], self.userid_rect[x + self.index])
            self.app.blit(self.user_name[x + self.index], self.username_rect[x + self.index])
            self.app.blit(self.user_lname[x + self.index], self.userlname_rect[x + self.index])
            self.app.blit(self.permission[x + self.index], self.permission_rect[x + self.index])
            # self.app.blit(self.locker_number[x + self.index], self.locker_rect[x + self.index])
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)
class Request_Listview:
 
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
        self.index = index * self.h_row
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
        if len(self.data) - self.index > self.h_row :
            self.list_index = self.h_row
        else:
            self.list_index = len(self.data) - self.index
        for x in range(self.list_index):
            self.number[x + self.index] = self.font.render(str((x + self.index) +1), True, self.color)
            self.number_rect[x + self.index] = self.number[x + self.index].get_rect()
            self.number_rect[x + self.index].topleft = ((1 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.product_name[x + self.index] = self.font.render(self.data[x + self.index].product_name[:25], True, self.color)
            self.product_rect[x + self.index] = self.product_name[x + self.index].get_rect()
            self.product_rect[x + self.index].topleft = ((2 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.quantity[x + self.index] = self.font.render(self.data[x + self.index].quantity, True, self.color)
            self.quantity_rect[x + self.index] = self.quantity[x + self.index].get_rect()
            self.quantity_rect[x + self.index].topleft = ((5 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.locker_number[x + self.index] = self.font.render(self.data[x + self.index].locker_number, True, self.color)
            self.locker_rect[x + self.index] = self.locker_number[x + self.index].get_rect()
            self.locker_rect[x + self.index].topleft = ((6 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

    def draw(self):
        if len(self.data) - self.index > self.h_row :
            self.list_index = self.h_row
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

class Product_Listview:
 
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
        self.index = index * self.h_row
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
        if len(self.data) - self.index >= self.h_row:
            self.list_index = self.h_row
        else:
            self.list_index = len(self.data) - self.index
        for x in range(self.list_index):
            self.number[x + self.index] = self.font.render(str((x + self.index) +1), True, self.color)
            self.number_rect[x + self.index] = self.number[x + self.index].get_rect()
            self.number_rect[x + self.index].topleft = ((1 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.product_name[x + self.index] = self.font.render(self.data[x + self.index]['product_name'][:25] + "...", True, self.color)
            self.product_rect[x + self.index] = self.product_name[x + self.index].get_rect()
            self.product_rect[x + self.index].topleft = ((2 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.quantity[x + self.index] = self.font.render(self.data[x + self.index]['quantity'], True, self.color)
            self.quantity_rect[x + self.index] = self.quantity[x + self.index].get_rect()
            self.quantity_rect[x + self.index].topleft = ((6 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

            self.locker_number[x + self.index] = self.font.render(self.data[x + self.index]['locker_number'], True, self.color)
            self.locker_rect[x + self.index] = self.locker_number[x + self.index].get_rect()
            self.locker_rect[x + self.index].topleft = ((7 * config.bwidth) + config.margin + 15 ,((x + self.start_column) * config.bheight) + (config.margin * ((x + 5) - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))

    def draw(self):
        if len(self.data) - self.index >= self.h_row :
            self.list_index = self.h_row
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