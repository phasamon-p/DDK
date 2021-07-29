""" Product request (Product request list) """
import pygame
from pygame.locals import *
import time
import os

import config 
import elements
import views
import services

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
            (1, 3): 'self.user_click()',
            (2, 3): 'self.user_click()',
            (3, 3): 'self.user_click()',
            (4, 3): 'self.user_click()',
            (5, 3): 'self.user_click()',
            (6, 3): 'self.user_click()',
            (7, 3): 'self.user_click()',
            (8, 3): 'self.user_click()',
            (9, 3): 'self.user_click()',
            (10, 3): 'self.user_click()',
            (1, 4): 'self.user_click()',
            (2, 4): 'self.user_click()',
            (3, 4): 'self.user_click()',
            (4, 4): 'self.user_click()',
            (5, 4): 'self.user_click()',
            (6, 4): 'self.user_click()',
            (7, 4): 'self.user_click()',
            (8, 4): 'self.user_click()',
            (9, 4): 'self.user_click()',
            (10, 4): 'self.user_click()',
            # Click product managment button
            (1, 5): 'self.product_click()',
            (2, 5): 'self.product_click()',
            (3, 5): 'self.product_click()',
            (4, 5): 'self.product_click()',
            (5, 5): 'self.product_click()',
            (6, 5): 'self.product_click()',
            (7, 5): 'self.product_click()',
            (8, 5): 'self.product_click()',
            (9, 5): 'self.product_click()',
            (10, 5): 'self.product_click()',
            (1, 6): 'self.product_click()',
            (2, 6): 'self.product_click()',
            (3, 6): 'self.product_click()',
            (4, 6): 'self.product_click()',
            (5, 6): 'self.product_click()',
            (6, 6): 'self.product_click()',
            (7, 6): 'self.product_click()',
            (8, 6): 'self.product_click()',
            (9, 6): 'self.product_click()',
            (10, 6): 'self.product_click()',
            # Click locker managment button
            (1, 7): 'self.locker_click()',
            (2, 7): 'self.locker_click()',
            (3, 7): 'self.locker_click()',
            (4, 7): 'self.locker_click()',
            (5, 7): 'self.locker_click()',
            (6, 7): 'self.locker_click()',
            (7, 7): 'self.locker_click()',
            (8, 7): 'self.locker_click()',
            (9, 7): 'self.locker_click()',
            (10, 7): 'self.locker_click()',
            (1, 8): 'self.locker_click()',
            (2, 8): 'self.locker_click()',
            (3, 8): 'self.locker_click()',
            (4, 8): 'self.locker_click()',
            (5, 8): 'self.locker_click()',
            (6, 8): 'self.locker_click()',
            (7, 8): 'self.locker_click()',
            (8, 8): 'self.locker_click()',
            (9, 8): 'self.locker_click()',
            (10, 8): 'self.locker_click()',
            # Click logout button
            (1, 9): 'self.logout_click()',
            (2, 9): 'self.logout_click()',
            (3, 9): 'self.logout_click()',
            (4, 9): 'self.logout_click()',
            (5, 9): 'self.logout_click()',
            (6, 9): 'self.logout_click()',
            (7, 9): 'self.logout_click()',
            (8, 9): 'self.logout_click()',
            (9, 9): 'self.logout_click()',
            (10, 9): 'self.logout_click()',
            (1, 10): 'self.logout_click()',
            (2, 10): 'self.logout_click()',
            (3, 10): 'self.logout_click()',
            (4, 10): 'self.logout_click()',
            (5, 10): 'self.logout_click()',
            (6, 10): 'self.logout_click()',
            (7, 10): 'self.logout_click()',
            (8, 10): 'self.logout_click()',
            (9, 10): 'self.logout_click()',
            (10, 10): 'self.logout_click()',
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

    def user_click(self):
        views.User_Management().run(); 
        pygame.quit()

    def product_click(self):
        views.Product_Management().run(); 
        pygame.quit()

    def locker_click(self):
        views.Locker_Management().run(); 
        pygame.quit()
  
    def logout_click(self):
        views.admin_data.admindata_reset()
        views.Home().run(); 
        pygame.quit()

    def run(self):
        """Initialize Caption and Valiable."""
        self.number = 1
        pygame.display.set_caption('Product request' + config.VERSION)
        while self.running:
            services.lockertimeout() # Check door opening
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