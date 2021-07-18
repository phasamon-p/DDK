""" Product request (Product request list) """
import pygame
from pygame.locals import *
import time
import os

import config 
import elements
import views

class System_Management:
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
            # Click user managment button
            (1, 3): 'views.User_Management().run(); pygame.quit()',
            (2, 3): 'views.User_Management().run(); pygame.quit()',
            (3, 3): 'views.User_Management().run(); pygame.quit()',
            (4, 3): 'views.User_Management().run(); pygame.quit()',
            (5, 3): 'views.User_Management().run(); pygame.quit()',
            (6, 3): 'views.User_Management().run(); pygame.quit()',
            (7, 3): 'views.User_Management().run(); pygame.quit()',
            (8, 3): 'views.User_Management().run(); pygame.quit()',
            (9, 3): 'views.User_Management().run(); pygame.quit()',
            (10, 3): 'views.User_Management().run(); pygame.quit()',
            (1, 4): 'views.User_Management().run(); pygame.quit()',
            (2, 4): 'views.User_Management().run(); pygame.quit()',
            (3, 4): 'views.User_Management().run(); pygame.quit()',
            (4, 4): 'views.User_Management().run(); pygame.quit()',
            (5, 4): 'views.User_Management().run(); pygame.quit()',
            (6, 4): 'views.User_Management().run(); pygame.quit()',
            (7, 4): 'views.User_Management().run(); pygame.quit()',
            (8, 4): 'views.User_Management().run(); pygame.quit()',
            (9, 4): 'views.User_Management().run(); pygame.quit()',
            (10, 4): 'views.User_Management().run(); pygame.quit()',

            # Click product managment button
            (1, 5): 'views.Product_Management().run(); pygame.quit()',
            (2, 5): 'views.Product_Management().run(); pygame.quit()',
            (3, 5): 'views.Product_Management().run(); pygame.quit()',
            (4, 5): 'views.Product_Management().run(); pygame.quit()',
            (5, 5): 'views.Product_Management().run(); pygame.quit()',
            (6, 5): 'views.Product_Management().run(); pygame.quit()',
            (7, 5): 'views.Product_Management().run(); pygame.quit()',
            (8, 5): 'views.Product_Management().run(); pygame.quit()',
            (9, 5): 'views.Product_Management().run(); pygame.quit()',
            (10, 5): 'views.Product_Management().run(); pygame.quit()',
            (1, 6): 'views.Product_Management().run(); pygame.quit()',
            (2, 6): 'views.Product_Management().run(); pygame.quit()',
            (3, 6): 'views.Product_Management().run(); pygame.quit()',
            (4, 6): 'views.Product_Management().run(); pygame.quit()',
            (5, 6): 'views.Product_Management().run(); pygame.quit()',
            (6, 6): 'views.Product_Management().run(); pygame.quit()',
            (7, 6): 'views.Product_Management().run(); pygame.quit()',
            (8, 6): 'views.Product_Management().run(); pygame.quit()',
            (9, 6): 'views.Product_Management().run(); pygame.quit()',
            (10, 6): 'views.Product_Management().run(); pygame.quit()',

            # Click locker managment button
            (1, 7): 'print("LOCKER MANAGEMENT")',
            (2, 7): 'print("LOCKER MANAGEMENT")',
            (3, 7): 'print("LOCKER MANAGEMENT")',
            (4, 7): 'print("LOCKER MANAGEMENT")',
            (5, 7): 'print("LOCKER MANAGEMENT")',
            (6, 7): 'print("LOCKER MANAGEMENT")',
            (7, 7): 'print("LOCKER MANAGEMENT")',
            (8, 7): 'print("LOCKER MANAGEMENT")',
            (9, 7): 'print("LOCKER MANAGEMENT")',
            (10, 7): 'print("LOCKER MANAGEMENT")',
            (1, 8): 'print("LOCKER MANAGEMENT")',
            (2, 8): 'print("LOCKER MANAGEMENT")',
            (3, 8): 'print("LOCKER MANAGEMENT")',
            (4, 8): 'print("LOCKER MANAGEMENT")',
            (5, 8): 'print("LOCKER MANAGEMENT")',
            (6, 8): 'print("LOCKER MANAGEMENT")',
            (7, 8): 'print("LOCKER MANAGEMENT")',
            (8, 8): 'print("LOCKER MANAGEMENT")',
            (9, 8): 'print("LOCKER MANAGEMENT")',
            (10, 8): 'print("LOCKER MANAGEMENT")',

            # Click logout button
            (1, 9): 'views.Home().run(); pygame.quit()',
            (2, 9): 'views.Home().run(); pygame.quit()',
            (3, 9): 'views.Home().run(); pygame.quit()',
            (4, 9): 'views.Home().run(); pygame.quit()',
            (5, 9): 'views.Home().run(); pygame.quit()',
            (6, 9): 'views.Home().run(); pygame.quit()',
            (7, 9): 'views.Home().run(); pygame.quit()',
            (8, 9): 'views.Home().run(); pygame.quit()',
            (9, 9): 'views.Home().run(); pygame.quit()',
            (10, 9): 'views.Home().run(); pygame.quit()',
            (1, 10): 'views.Home().run(); pygame.quit()',
            (2, 10): 'views.Home().run(); pygame.quit()',
            (3, 10): 'views.Home().run(); pygame.quit()',
            (4, 10): 'views.Home().run(); pygame.quit()',
            (5, 10): 'views.Home().run(); pygame.quit()',
            (6, 10): 'views.Home().run(); pygame.quit()',
            (7, 10): 'views.Home().run(); pygame.quit()',
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

    def do_click(self, x, y):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = x // (config.bwidth + config.margin)
        row_click = y // (config.bheight + config.margin)
        if (column_click, row_click) in self.click:
            exec(self.click[column_click, row_click])

    def run(self):
        """Initialize Caption and Valiable."""
        self.number = 1
        pygame.display.set_caption('Product request' + config.VERSION)
       
        while self.running:
            """Refresh surface."""
            self.screen.fill(Color('white')) 

            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 300, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)

                    if row == 0 and column == 0:
                        elements.Title('SYSTEM MANAGEMENT', pos=(240, 67), app=(self.screen)).draw()
                    if row == 3 and column == 1:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 958, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   USER MANAGMENT', position, app=(self.screen)).draw()
                    if row == 5 and column == 1:
                        elements.Button(self.screen, config.blue, x, y, config.bwidth + 958, config.bheight + 67).Rect()  
                        elements.Text_Button_Medium('PRODUCT MANAGMENT', position, app=(self.screen)).draw()
                    if row == 7 and column == 1:
                        elements.Button(self.screen, config.dark_yellow, x, y, config.bwidth + 958, config.bheight + 67).Rect()
                        elements.Text_Button_Medium(' LOCKER MANAGMENT', position, app=(self.screen)).draw()  
                    if row == 9 and column == 1:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 958, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('            LOGOUT', position, app=(self.screen)).draw()  
            
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