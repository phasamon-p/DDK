""" Search (Searching Product) """
import pygame
from pygame.locals import *
import time
import os

import config 
import elements
import views



class Search:
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
            # Click search button
            (8, 3): 'print("ADD")',
            (9, 3): 'print("ADD")',
            (10, 3): 'print("ADD")',
            (8, 4): 'print("ADD")',
            (9, 4): 'print("ADD")',
            (10, 4): 'print("ADD")',
            # Click request button
            (8, 5): 'print("DELETE")',
            (9, 5): 'print("DELETE")',
            (10, 5): 'print("DELETE")',
            (8, 6): 'print("DELETE")',
            (9, 6): 'print("DELETE")',
            (10, 6): 'print("DELETE")',
            # Click admin button
            (8, 7): 'print("CONFIRM")',
            (9, 7): 'print("CONFIRM")',
            (10, 7): 'print("CONFIRM")',
            (8, 8): 'print("CONFIRM")',
            (9, 8): 'print("CONFIRM")',
            (10, 8): 'print("CONFIRM")',
            # Click admin button
            (8, 9): 'views.Home().run(); pygame.quit()',
            (9, 9): 'views.Home().run(); pygame.quit()',
            (10, 9): 'views.Home().run(); pygame.quit()',
            (8, 10): 'views.Home().run(); pygame.quit()',
            (9, 10): 'views.Home().run(); pygame.quit()',
            (10, 10): 'views.Home().run(); pygame.quit()',
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
        elements.Title('PRODUCT REQUEST LIST', pos=(200, 67), app=(self.screen)).draw()

        """Initialize user interface."""
        for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                row_click = row
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    column_click = column
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) + 20)
                    position2 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) - 30, (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    if row == 3 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 204, config.bheight + 67).Rect()
                        elements.Text_Button('    ADD', position, app=(self.screen)).draw()
                    if row == 5 and column == 8:
                        elements.Button(self.screen, config.dark_gray, x, y, config.bwidth + 204, config.bheight + 67).Rect()  
                        elements.Text_Button('  DELETE', position, app=(self.screen)).draw()
                    if row == 7 and column == 8:
                        elements.Button(self.screen, config.blue, x, y, config.bwidth + 204, config.bheight + 67).Rect()
                        elements.Text_Button(' CONFIRM', position, app=(self.screen)).draw()  
                    if row == 9 and column == 8:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 204, config.bheight + 67).Rect()
                        elements.Text_Button('  CANCEL', position, app=(self.screen)).draw()
                    if row == 10 and column == 1:
                        elements.Button(self.screen, config.gray, x, y, config.bwidth + 107, config.bheight).Rect()
                        elements.Text_Button_Medium(' PREVIOUS', position3, app=(self.screen)).draw() 
                    if row == 10 and column == 6:
                        elements.Button(self.screen, config.gray, x, y, config.bwidth + 107, config.bheight).Rect()
                        elements.Text_Button_Medium('  NEXT', position2, app=(self.screen)).draw() 

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