""" Search"""
import pygame
from pygame.locals import *
import time
import os
import config 
import elements
import views
import data_example



class Search:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        flags = RESIZABLE
        self.screen = pygame.display.set_mode(config.screensize, flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        self.next_button = False # Set default avtivation status of next button
        self.previous_button = False # Set default avtivation status of previous button
        self.index = 0 # Set default index value of listview page
        self.product_data = ""

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
            (8, 3): 'self.product_data = self.search_click()',
            (9, 3): 'self.product_data = self.search_click()',
            (10, 3): 'self.product_data = self.search_click()',
            (8, 4): 'self.product_data = self.search_click()',
            (9, 4): 'self.product_data = self.search_click()',
            (10, 4): 'self.product_data = self.search_click()',
            # Click cancel button
            (8, 9): 'views.Home().run(); pygame.quit()',
            (9, 9): 'views.Home().run(); pygame.quit()',
            (10, 9): 'views.Home().run(); pygame.quit()',
            (8, 10): 'views.Home().run(); pygame.quit()',
            (9, 10): 'views.Home().run(); pygame.quit()',
            (10, 10): 'views.Home().run(); pygame.quit()',
            # Click previous button
            (1, 10): 'self.previousbutton_click()',
            (2, 10): 'self.previousbutton_click()',
            # Click next button
            (6, 10): 'self.nextbutton_click()',
            (7, 10): 'self.nextbutton_click()',
        }

    def do_shortcut(self, event):
        """Find the the key/mod combination in the dictionary and execute the cmd."""
        k = event.key
        m = event.mod
        if (k, m) in self.shortcuts:
            exec(self.shortcuts[k, m])

    def do_click(self, event):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = event.pos[0] // (config.bwidth + config.margin)
        row_click = event.pos[1] // (config.bheight + config.margin)
        if (column_click, row_click) in self.click:
            exec(self.click[column_click, row_click])

    def search_click(self):
        x = data_example.product['product']
        return x

    def active_button(self):
        """Check activation next button."""
        if len(self.product_data) - (self.index * 5) > 5 :
            self.next_button = True
        else:
            self.next_button = False
        """Check activation previous button."""
        if self.index > 0:
            self.previous_button = True
        else:
            self.previous_button = False
    def nextbutton_click(self):
        if self.next_button:
            self.index += 1

    def previousbutton_click(self):
        if self.previous_button:
            self.index -= 1

    def run(self):
        """Initialize Caption and Valiable."""
        pygame.display.set_caption('Product search' + config.VERSION)
        self.search_input = elements.InputBox(1, 3, 7, 1, app = (self.screen), active = True, numpad_active = True)

        """Run the main event loop."""
        while self.running:
            self.number = 1
            self.screen.fill(Color('white'))
            self.product_listview = elements.Search_Listview(1, 5, 7, 5, app=(self.screen),data = self.product_data, index = self.index)
            self.active_button()
            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position2 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) - 30, (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) - 35, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 20)
                    if row == 0 and column == 0:
                        elements.Title('PRODUCT SEARCH', pos=(320, 67), app=(self.screen)).draw()
                        elements.Header_Table('No.', 1, 4, app=(self.screen)).draw()
                        elements.Header_Table('Product name', 2, 4, app=(self.screen)).draw()
                        elements.Header_Table('QTY.', 6, 4, app=(self.screen)).draw()
                        elements.Header_Table('Locker', 7, 4, app=(self.screen)).draw()
                        # elements.Rectangle(1, 5, 7, 5, app=(self.screen)).draw()
                        self.search_input.draw() 
                        self.product_listview.draw()                     
                    if row == 3 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button('     SEARCH', position4, app=(self.screen)).draw()
                    """Initialize Numpad."""
                    if row >= 5 and row <= 8 and column >= 8 and column <= 10:
                        if row == 8 and column == 8:
                            elements.Button(self.screen, config.light_blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number('*', position, app=(self.screen)).draw()
                        elif row == 8 and column == 9:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number(str(0), position, app=(self.screen)).draw()
                        elif row == 8 and column == 10:
                            elements.Button(self.screen, config.light_blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number('#', position, app=(self.screen)).draw()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number(str(self.number), position, app=(self.screen)).draw()
                        self.number += 1
                    if row == 9 and column == 8:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button('     CANCEL', position4, app=(self.screen)).draw()
                    if row == 10 and column == 1:
                        if self.previous_button:
                            elements.Button(self.screen, config.dark_gray, x, y, config.bwidth + 107, config.bheight).Rect()
                        else:
                            elements.Button(self.screen, config.gray, x, y, config.bwidth + 107, config.bheight).Rect()
                        elements.Text_Button_Medium(' PREVIOUS', position3, app=(self.screen)).draw() 
                    if row == 10 and column == 6:
                        if self.next_button:
                            elements.Button(self.screen, config.dark_gray, x, y, config.bwidth + 107, config.bheight).Rect()
                        else:
                            elements.Button(self.screen, config.gray, x, y, config.bwidth + 107, config.bheight).Rect()
                        elements.Text_Button_Medium('  NEXT', position2, app=(self.screen)).draw()                

            for event in pygame.event.get():
                self.search_value = self.search_input.handle_event(event)
                if event.type == KEYDOWN:
                    self.do_shortcut(event)
                if event.type == QUIT:
                    self.running = False
                if event.type == MOUSEBUTTONDOWN:
                    self.do_click(event)
            
            pygame.display.update()
            pygame.display.flip()
        pygame.quit()