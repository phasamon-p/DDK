""" Product request (Product request list) """
import pygame
from pygame.locals import *
import time
import os

import config 
import elements
import views

class User_Management:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 

        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'home.App().run()',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }
        
        self.click = {
            # Click add button
            (1, 3): 'self.add_click()',
            (5, 3): 'self.add_click()',
            (6, 3): 'self.add_click()',
            (7, 3): 'self.add_click()',
            (8, 3): 'self.add_click()',
            (9, 3): 'self.add_click()',
            (10, 3): 'self.add_click()',
            (1, 4): 'self.add_click()',
            (2, 4): 'self.add_click()',
            (3, 4): 'self.add_click()',
            (4, 4): 'self.add_click()',
            (5, 4): 'self.add_click()',
            (6, 4): 'self.add_click()',
            (7, 4): 'self.add_click()',
            (8, 4): 'self.add_click()',
            (9, 4): 'self.add_click()',
            (10, 4): 'self.add_click()',

            # Click edit or delete button
            (1, 6): 'print("EDIT OR DELETE")',
            (2, 6): 'print("EDIT OR DELETE")',
            (3, 6): 'print("EDIT OR DELETE")',
            (4, 6): 'print("EDIT OR DELETE")',
            (5, 6): 'print("EDIT OR DELETE")',
            (6, 6): 'print("EDIT OR DELETE")',
            (7, 6): 'print("EDIT OR DELETE")',
            (8, 6): 'print("EDIT OR DELETE")',
            (9, 6): 'print("EDIT OR DELETE")',
            (10, 6): 'print("EDIT OR DELETE")',
            (1, 7): 'print("EDIT OR DELETE")',
            (2, 7): 'print("EDIT OR DELETE")',
            (3, 7): 'print("EDIT OR DELETE")',
            (4, 7): 'print("EDIT OR DELETE")',
            (5, 7): 'print("EDIT OR DELETE")',
            (6, 7): 'print("EDIT OR DELETE")',
            (7, 7): 'print("EDIT OR DELETE")',
            (8, 7): 'print("EDIT OR DELETE")',
            (9, 7): 'print("EDIT OR DELETE")',
            (10, 7): 'print("EDIT OR DELETE")',
            
            # Click back button
            (1, 9): 'views.System_Management().run(); pygame.quit()',
            (2, 9): 'views.System_Management().run(); pygame.quit()',
            (3, 9): 'views.System_Management().run(); pygame.quit()',
            (4, 9): 'views.System_Management().run(); pygame.quit()',
            (5, 9): 'views.System_Management().run(); pygame.quit()',
            (6, 9): 'views.System_Management().run(); pygame.quit()',
            (7, 9): 'views.System_Management().run(); pygame.quit()',
            (8, 9): 'views.System_Management().run(); pygame.quit()',
            (9, 9): 'views.System_Management().run(); pygame.quit()',
            (10, 9): 'views.System_Management().run(); pygame.quit()',
            (1, 10): 'views.System_Management().run(); pygame.quit()',
            (2, 10): 'views.System_Management().run(); pygame.quit()',
            (3, 10): 'views.System_Management().run(); pygame.quit()',
            (4, 10): 'views.System_Management().run(); pygame.quit()',
            (5, 10): 'views.System_Management().run(); pygame.quit()',
            (6, 10): 'views.System_Management().run(); pygame.quit()',
            (7, 10): 'views.System_Management().run(); pygame.quit()',
            (8, 10): 'views.System_Management().run(); pygame.quit()',
            (9, 10): 'views.System_Management().run(); pygame.quit()',
            (10, 10): 'views.System_Management().run(); pygame.quit()',
           
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

    def add_click(self):
        views.User_Id(False).run()
        pygame.quit()

    def run(self):
        """Initialize Caption and Valiable."""
        self.number = 1
        pygame.display.set_caption('User management' + config.VERSION)
       
        while self.running:
            """Refresh surface."""
            self.screen.fill(Color('white')) 

            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 350, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)

                    if row == 0 and column == 0:
                        elements.Title('USER MANAGEMENT', pos=(290, 67), app=(self.screen)).draw()
                    if row == 3 and column == 1:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 958, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('         ADD', position, app=(self.screen)).draw()
                    if row == 6 and column == 1:
                        elements.Button(self.screen, config.blue, x, y, config.bwidth + 958, config.bheight + 67).Rect()  
                        elements.Text_Button_Medium('EDIT OR DELETE', position, app=(self.screen)).draw()
                    if row == 9 and column == 1:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 958, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('        BACK', position, app=(self.screen)).draw()   
            
            """Run the main event loop."""
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