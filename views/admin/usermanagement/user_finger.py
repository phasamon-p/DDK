""" Home (Main app) """
import pygame
from pygame.locals import *

import time
import os
import services
import config 
import elements
import views



class User_Finger:
    """Create a single-window app with multiple scenes."""

    def __init__(self, editstage):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        self.editstage = editstage

        if self.editstage:
            self.caption = 'Edit user finger scan'
            self.title = 'EDIT USER FINGER SCAN'
        else:
            self.caption = 'Add user finger scan'
            self.title = 'ADD USER FINGER SCAN'

        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'self.exit_fullscreen()',
            (K_x, KMOD_LCTRL): 'print("ctrl + X")',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }
    
        self.click = {
            # Click scan button
            (7, 4): 'self.scan_click()',
            (8, 4): 'self.scan_click()',
            (9, 4): 'self.scan_click()',
            (10, 4): 'self.scan_click()',
            (7, 5): 'self.scan_click()',
            (8, 5): 'self.scan_click()',
            (9, 5): 'self.scan_click()',
            (10, 5): 'self.scan_click()',
            # Click back button
            (7, 8): 'self.back_click()',
            (8, 8): 'self.back_click()',
            (9, 8): 'self.back_click()',
            (10, 8): 'self.back_click()',
            (7, 9): 'self.back_click()',
            (8, 9): 'self.back_click()',
            (9, 9): 'self.back_click()',
            (10, 9): 'self.back_click()',
        }

        self.click_edit = {
            # Click update button
            (7, 3): 'self.update_click()',
            (8, 3): 'self.update_click()',
            (9, 3): 'self.update_click()',
            (10, 3): 'self.update_click()',
            (7, 4): 'self.update_click()',
            (8, 4): 'self.update_click()',
            (9, 4): 'self.update_click()',
            (10, 4): 'self.update_click()',
            # Click next button
            (7, 6): 'self.next_click()',
            (8, 6): 'self.next_click()',
            (9, 6): 'self.next_click()',
            (10, 6): 'self.next_click()',
            (7, 7): 'self.next_click()',
            (8, 7): 'self.next_click()',
            (9, 7): 'self.next_click()',
            (10, 7): 'self.next_click()',
            # Click back button
            (7, 9): 'self.back_click()',
            (8, 9): 'self.back_click()',
            (9, 9): 'self.back_click()',
            (10, 9): 'self.back_click()',
            (7, 10): 'self.back_click()',
            (8, 10): 'self.back_click()',
            (9, 10): 'self.back_click()',
            (10, 10): 'self.back_click()',
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
        if self.editstage:
            if (column_click, row_click) in self.click_edit:
                exec(self.click_edit[column_click, row_click])
        else:
            if (column_click, row_click) in self.click:
                exec(self.click[column_click, row_click])

    def exit_fullscreen(self):
        services.getfingerid()
        print("alt+X")
        config.flags = RESIZABLE
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen

    def scan_click(self):
        self.index = services.getfingerid()
        if services.enroll_finger(self.index):
            views.user_data.user_data['fingerid'] = str(self.index)
            views.User_Result(False).run()
            pygame.quit()
        else:
            print("Can't created finger print")
    
    def update_click(self):
        services.enroll_finger(int(views.user_data.user_data['fingerid']))
        views.User_Result(True).run()
        pygame.quit()

    def next_click(self):
        views.User_Result(True).run()
        pygame.quit()    
        
    def back_click(self):
        if self.editstage:
            views.User_Lockeraccess(True).run()
            pygame.quit()
        else:
            views.user_data.user_data['fingerid'] = ''
            views.User_Lockeraccess(False).run()
            pygame.quit()
    
    def run(self):
        """Initialize Caption and Valiable."""
        pygame.display.set_caption(self.caption + config.VERSION)
        while self.running:
            """Refresh surface."""
            self.screen.fill(Color('white'))
            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                row_click = row
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    column_click = column
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 15, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 5)
                    if row == 0 and column == 0:
                        if self.editstage:
                            elements.Image('images/touchid.png', (120, 200), app=(self.screen)).draw()
                        else:
                            elements.Image('images/touchid.png', (120, 220), app=(self.screen)).draw()
                        elements.Title(self.title, pos=(210, 67), app=(self.screen)).draw()
                    if self.editstage:
                        if row == 3 and column == 7:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 321, config.bheight + 67).Rect()
                            elements.Text_Mainbutton('  UPDATE', position, app=(self.screen)).draw()
                        if row == 6 and column == 7:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 321, config.bheight + 67).Rect()  
                            elements.Text_Mainbutton('    NEXT', position, app=(self.screen)).draw()
                        if row == 9 and column == 7:
                            elements.Button(self.screen, config.red, x, y, config.bwidth + 321, config.bheight + 67).Rect()
                            elements.Text_Mainbutton('    BACK', position, app=(self.screen)).draw()
                    else:
                        if row == 4 and column == 7:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 321, config.bheight + 67).Rect()  
                            elements.Text_Mainbutton('    SCAN', position, app=(self.screen)).draw()
                        if row == 8 and column == 7:
                            elements.Button(self.screen, config.red, x, y, config.bwidth + 321, config.bheight + 67).Rect()
                            elements.Text_Mainbutton('    BACK', position, app=(self.screen)).draw()
            """Run the main event loop."""
            for event in pygame.event.get():
                if event.type == FINGERDOWN:
                    print(event)
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

class Person:
  def __init__(self):
    self.name = "Phasamon Panyee"
    self.age = 27