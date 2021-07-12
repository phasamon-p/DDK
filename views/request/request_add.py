""" Product request (Add))"""
import pygame
from pygame.locals import *
import time
import os
import config 
import elements
import views

class product_list():
    section = ""
    qrcode = ""
    item_number = ""
    product_name = ""
    part_numbe = ""
    part_name = ""
    drawing_number = ""
    locker_number = ""
    quantity = ""
    other = ""

class Request_Add:
    """Create a single-window app with multiple scenes."""
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        flags = RESIZABLE
        self.screen = pygame.display.set_mode(config.screensize, flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        views.request_data.inbox_active[0] = True # Set default input box activation
        views.request_data.inbox_active[1] = False # Set default input box activation
        self.product_list = product_list()
        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'home.App().run()',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }
        self.click = {
            # Click search button
            (8, 3): 'print("SEARCH");',
            (9, 3): 'print("SEARCH");',
            (10, 3): 'print("SEARCH");',
            # Click add button
            (8, 8): 'self.add()',
            (9, 8): 'self.add()',
            (10, 8): 'self.add()',
            (8, 9): 'self.add()',
            (9, 9): 'self.add()',
            (10, 9): 'self.add()',
            # Click cancel button
            (8, 10): 'self.cancel()',
            (9, 10): 'self.cancel()',
            (10, 10): 'self.cancel()',
        }

    def do_shortcut(self, event):
        """Find the the key/mod combination in the dictionary and execute the cmd."""
        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])

    def do_click(self, x, y):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = x // (config.bwidth + config.margin)
        row_click = y // (config.bheight + config.margin)
        if (column_click, row_click) in self.click:
            exec(self.click[column_click, row_click])

    def add(self):
        if self.search_value != "":
            self.product_list.product_name = self.search_value
            if self.quantity_value != "":
                self.product_list.quantity = self.quantity_value
                views.request_data.add(self.product_list)
                views.Request().run(); pygame.quit()
            else:
                self.product_list.quantity = ""
                print("Quantity is invalid")
        else:
            self.product_list.product_name = self.search_value
            print("Product request is invalid")

    def cancel(self):
        views.Request().run()
        pygame.quit()
       

    def run(self):
        """Initialize Caption and Valiable."""
        pygame.display.set_caption('Add product requestion' + config.VERSION)
        self.search_input = elements.InputBox_2(1, 3, 7, 1, app = (self.screen), active = views.request_data.inbox_active[0], numpad_active = True)
        self.quantity_input = elements.InputBox_2(1, 10, 7, 1, app = (self.screen), active = views.request_data.inbox_active[1], numpad_active = True)
        
        """Run the main event loop."""
        while self.running:
            self.number = 1
            self.screen.fill(Color('white'))
            self.search_input.active = views.request_data.inbox_active[0]
            self.quantity_input.active = views.request_data.inbox_active[1]

            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                row_click = row
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    column_click = column
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position2 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    if row == 0 and column == 0:
                        elements.Title('ADD PRODUCT REQUEST', pos=(230, 67), app=(self.screen)).draw()
                        elements.Header_Table('No.', 1, 4, app=(self.screen)).draw()
                        elements.Header_Table('Product name', 2, 4, app=(self.screen)).draw()
                        elements.Header_Table('QTY.', 6, 4, app=(self.screen)).draw()
                        elements.Header_Table('Locker', 7, 4, app=(self.screen)).draw()
                        elements.Header_Table('Quantity Requesition', 1, 9, app=(self.screen)).draw()
                        elements.Rectangle(1, 5, 7, 4, app=(self.screen)).draw()
                        self.search_input.draw()
                        self.quantity_input.draw()                       
                    if row == 3 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 214, config.bheight).Rect()
                        elements.Text_Button_Medium('     SEARCH', position, app=(self.screen)).draw()
                    """Initialize Numpad."""
                    if row >= 4 and row <= 7 and column >= 8 and column <= 10:
                        if row == 7 and column == 8:
                            elements.Button(self.screen, config.light_blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number('*', position, app=(self.screen)).draw()
                        elif row == 7 and column == 9:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number(str(0), position, app=(self.screen)).draw()
                        elif row == 7 and column == 10:
                            elements.Button(self.screen, config.light_blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number('#', position, app=(self.screen)).draw()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number(str(self.number), position, app=(self.screen)).draw()
                        self.number += 1
                    if row == 8 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 214, config.bheight + 67).Rect()  
                        elements.Text_Button_Medium('        ADD', position2, app=(self.screen)).draw()
                    if row == 10 and column == 8:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 214, config.bheight).Rect()
                        elements.Text_Button_Medium('     CANCEL', position, app=(self.screen)).draw()                 

            for event in pygame.event.get():
                self.search_value = self.search_input.handle_event(event, 1)
                self.quantity_value = self.quantity_input.handle_event(event, 2)
                if event.type == KEYDOWN:
                    self.do_shortcut(event)
                if event.type == QUIT:
                    self.running = False
                if event.type == MOUSEBUTTONDOWN or event.type == FINGERDOWN:
                    # self.do_click(event)
                    if event.type == FINGERDOWN:
                        x = event.x * config.width
                        y = event.y * config.height
                        self.do_click(x, y)
                    else:
                        x, y = event.pos
                        self.do_click(x, y)
            
            pygame.display.update()
            pygame.display.flip()
        pygame.quit()