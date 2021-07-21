""" Search"""
import pygame
from pygame.locals import *
import time
import os
import config 
import elements
import views
import services
import data_example

class Locker_Control:
    """Create a single-window app with multiple scenes."""
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        self.locker_button = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.productlocker_value = [False, False, False, False, False, False, False, False, False, False, False, False]
        self.first_check()

      
        self.caption = 'locker control'
        self.title = 'LOCKER CONTROL'

        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'home.App().run()',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }

        self.click = {
            # Click 1 button
            (1, 3): 'self.toggle_button(1)',
            (2, 3): 'self.toggle_button(1)',
            (1, 4): 'self.toggle_button(1)',
            (2, 4): 'self.toggle_button(1)',
            # Click 2 button
            (3, 3): 'self.toggle_button(2)',
            (4, 3): 'self.toggle_button(2)',
            (3, 4): 'self.toggle_button(2)',
            (4, 4): 'self.toggle_button(2)',
            # Click 3 button
            (5, 3): 'self.toggle_button(3)',
            (6, 3): 'self.toggle_button(3)',
            (5, 4): 'self.toggle_button(3)',
            (6, 4): 'self.toggle_button(3)',
            # Click 4 button
            (7, 3): 'self.toggle_button(4)',
            (8, 3): 'self.toggle_button(4)',
            (7, 4): 'self.toggle_button(4)',
            (8, 4): 'self.toggle_button(4)',
            # Click 5 button
            (9, 3): 'self.toggle_button(5)',
            (10, 3): 'self.toggle_button(5)',
            (9, 4): 'self.toggle_button(5)',
            (10, 4): 'self.toggle_button(5)',
            # Click 6 button
            (1, 5): 'self.toggle_button(6)',
            (2, 5): 'self.toggle_button(6)',
            (1, 6): 'self.toggle_button(6)',
            (2, 6): 'self.toggle_button(6)',
            # Click 7 button
            (3, 5): 'self.toggle_button(7)',
            (4, 5): 'self.toggle_button(7)',
            (3, 6): 'self.toggle_button(7)',
            (4, 6): 'self.toggle_button(7)',
            # Click 8 button
            (5, 5): 'self.toggle_button(8)',
            (6, 5): 'self.toggle_button(8)',
            (5, 6): 'self.toggle_button(8)',
            (6, 6): 'self.toggle_button(8)',
            # Click 9 button
            (7, 5): 'self.toggle_button(9)',
            (8, 5): 'self.toggle_button(9)',
            (7, 6): 'self.toggle_button(9)',
            (8, 6): 'self.toggle_button(9)',
            # Click 10 button
            (9, 5): 'self.toggle_button(10)',
            (10, 5): 'self.toggle_button(10)',
            (9, 6): 'self.toggle_button(10)',
            (10, 6): 'self.toggle_button(10)',
            # Click 11 button
            (1, 7): 'self.toggle_button(11)',
            (2, 7): 'self.toggle_button(11)',
            (1, 8): 'self.toggle_button(11)',
            (2, 8): 'self.toggle_button(11)',
            # Click 12 button
            (3, 7): 'self.toggle_button(12)',
            (4, 7): 'self.toggle_button(12)',
            (3, 8): 'self.toggle_button(12)',
            (4, 8): 'self.toggle_button(12)',
            # Click cencel button
            (9, 9): 'self.cancel_click()',
            (10, 9): 'self.cancel_click()',
            (9, 10): 'self.cancel_click()',
            (10, 10): 'self.cancel_click()',
        }

    def first_check(self):
        for x in range(len(views.product_data.product_data['locker_number'])):
            if views.product_data.product_data['locker_number'][x]:
                self.locker_button[x] = True

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

    def cancel_click(self):
        views.Locker_Management().run()
        pygame.quit()

    def toggle_button(self, event):
        if self.locker_button[event - 1]:
            if config.locker_type == 0:
                self.locker_button[event - 1] = False
                services.locker_close(0, event)
            else:
                self.locker_button[event - 1] = False
                services.locker_close(0, event)
        else:
            if config.locker_type == 0:
                self.locker_button[event - 1] = True
                services.locker_open(0, event)
            else:
                self.locker_button[event - 1] = True
                services.locker_open(0, event)

    def run(self):
        """Initialize Caption and Valiable."""
        pygame.display.set_caption(self.caption + config.VERSION)
        """Run the main event loop."""
        while self.running:
            self.screen.fill(Color('white'))      
            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position2 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 50, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 25)
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 40, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 25)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 10, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    if row == 0 and column == 0:
                        elements.Title(self.title, pos=(330, 67), app=(self.screen)).draw() 
                    """Initialize Button."""
                    for index in range(5):
                        if row == 3 and column == index + (index + 1):
                            if self.locker_button[index]:
                                elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                            else:
                                elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                            if (index + 1) > 9:
                                elements.Text_Button_Medium(str(index + 1), position3, app=(self.screen)).draw()
                            else:
                                elements.Text_Button_Medium(str(index + 1), position2, app=(self.screen)).draw()
                    for index in range(5):
                        if row == 5 and column == index + (index + 1):
                            if self.locker_button[index + 5]:
                                elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                            else:
                                elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                            if (index + 6) > 9:
                                elements.Text_Button_Medium(str(index + 6), position3, app=(self.screen)).draw()
                            else:
                                elements.Text_Button_Medium(str(index + 6), position2, app=(self.screen)).draw()
                    for index in range(2):
                        if row == 7 and column == index + (index + 1):
                            if self.locker_button[index + 10]:
                                elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                            else:
                                elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                            if (index + 11) > 9:
                                elements.Text_Button_Medium(str(index + 11), position3, app=(self.screen)).draw()
                            else:
                                elements.Text_Button_Medium(str(index + 11), position2, app=(self.screen)).draw()
                    if row == 9 and column == 9:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                        elements.Text_Button_Medium(' BACK', position4, app=(self.screen)).draw()
                   
            for event in pygame.event.get():
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