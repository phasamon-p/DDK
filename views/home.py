""" Home (Main app) """
import pygame
from pygame.locals import *


import time
import os

import config 
import elements
import views



class Home:
    """Create a single-window app with multiple scenes."""

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 

        self.person = Person()

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
            (7, 2): 'views.Search().run(); pygame.quit()',
            (8, 2): 'views.Search().run(); pygame.quit()',
            (9, 2): 'views.Search().run(); pygame.quit()',
            (10, 2): 'views.Search().run(); pygame.quit()',
            (7, 3): 'views.Search().run(); pygame.quit()',
            (8, 3): 'views.Search().run(); pygame.quit()',
            (9, 3): 'views.Search().run(); pygame.quit()',
            (10, 3): 'views.Search().run(); pygame.quit()',
            # Click request button
            (7, 5): 'print("REQUEST")',
            (8, 5): 'print("REQUEST")',
            (9, 5): 'print("REQUEST")',
            (10, 5): 'print("REQUEST")',
            (7, 6): 'print("REQUEST")',
            (8, 6): 'print("REQUEST")',
            (9, 6): 'print("REQUEST")',
            (10, 6): 'print("REQUEST")',
            # Click admin button
            (7, 8): 'print("ADMIN")',
            (8, 8): 'print("ADMIN")',
            (9, 8): 'print("ADMIN")',
            (10, 8): 'print("ADMIN")',
            (7, 9): 'print("ADMIN")',
            (8, 9): 'print("ADMIN")',
            (9, 9): 'print("ADMIN")',
            (10, 9): 'print("ADMIN")',
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

    def run(self):
        self.number = 1

        """Initialize Title and Image."""
        elements.Image('images/qr.png', (200, 200), app=(self.screen)).draw()
        elements.InputBox(100, 100, 140, 32,"Text Input", app=(self.screen))

        """Initialize user interface."""
        for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                row_click = row
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    column_click = column
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) + 5)
                    if row == 2 and column == 7:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 321, config.bheight + 67).Rect()
                        elements.Text_Mainbutton('   SEARCH', position, app=(self.screen)).draw()
                    if row == 5 and column == 7:
                        elements.Button(self.screen, config.blue, x, y, config.bwidth + 321, config.bheight + 67).Rect()  
                        elements.Text_Mainbutton('  REQUEST', position, app=(self.screen)).draw()
                    if row == 8 and column == 7:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 321, config.bheight + 67).Rect()
                        elements.Text_Mainbutton('    ADMIN', position, app=(self.screen)).draw()                   

        """Run the main event loop."""
        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.do_shortcut(event)
                if event.type == QUIT:
                    self.running = False
                if event.type == MOUSEBUTTONDOWN:
                    self.do_click(event)
            
            pygame.display.update()
        pygame.quit()

class Person:
  def __init__(self):
    self.name = "Phasamon Panyee"
    self.age = 27