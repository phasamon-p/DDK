""" Search"""
import pygame
from pygame.locals import *
import time
import os
import config 
import elements
import views
import data_example



class User_Department:
    """Create a single-window app with multiple scenes."""

    def __init__(self, editstage):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        self.next_button = False # Set default avtivation status of next button
        self.previous_button = False # Set default avtivation status of previous button
        self.index = 0 # Set default index value of listview page
        self.product_data = ""
        self.editstage = editstage

        self.as1_button = False
        self.as2_button = False
        self.mt1_button = False
        self.mt2_button = False
        self.pr_button = False
        self.department_value = ''
        if self.editstage:
            self.caption = 'Edit user department'
            self.title = 'EDIT USER DEPARTMENT'
        else:
            self.caption = 'Add user department'
            self.title = 'ADD USER DEPARTMENT'

        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'home.App().run()',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }

        self.click = {
            # Click AS1 button
            (1, 3): 'self.as1_click()',
            (2, 3): 'self.as1_click()',
            (3, 3): 'self.as1_click()',
            (4, 3): 'self.as1_click()',
            (5, 3): 'self.as1_click()',
            (1, 4): 'self.as1_click()',
            (2, 4): 'self.as1_click()',
            (3, 4): 'self.as1_click()',
            (4, 4): 'self.as1_click()',
            (5, 4): 'self.as1_click()',
            # Click AS2 button
            (6, 3): 'self.as2_click()',
            (7, 3): 'self.as2_click()',
            (8, 3): 'self.as2_click()',
            (9, 3): 'self.as2_click()',
            (10, 3): 'self.as2_click()',
            (6, 4): 'self.as2_click()',
            (7, 4): 'self.as2_click()',
            (8, 4): 'self.as2_click()',
            (9, 4): 'self.as2_click()',
            (10, 4): 'self.as2_click()',
            # Click MT1 button
            (1, 5): 'self.mt1_click()',
            (2, 5): 'self.mt1_click()',
            (3, 5): 'self.mt1_click()',
            (4, 5): 'self.mt1_click()',
            (5, 5): 'self.mt1_click()',
            (1, 6): 'self.mt1_click()',
            (2, 6): 'self.mt1_click()',
            (3, 6): 'self.mt1_click()',
            (4, 6): 'self.mt1_click()',
            (5, 6): 'self.mt1_click()',
            # Click MT2 button
            (6, 5): 'self.mt2_click()',
            (7, 5): 'self.mt2_click()',
            (8, 5): 'self.mt2_click()',
            (9, 5): 'self.mt2_click()',
            (10, 5): 'self.mt2_click()',
            (6, 6): 'self.mt2_click()',
            (7, 6): 'self.mt2_click()',
            (8, 6): 'self.mt2_click()',
            (9, 6): 'self.mt2_click()',
            (10, 6): 'self.mt2_click()',
            # Click PR button
            (4, 7): 'self.pr_click()',
            (5, 7): 'self.pr_click()',
            (6, 7): 'self.pr_click()',
            (7, 7): 'self.pr_click()',
            (8, 7): 'self.pr_click()',
            (4, 8): 'self.pr_click()',
            (5, 8): 'self.pr_click()',
            (6, 8): 'self.pr_click()',
            (7, 8): 'self.pr_click()',
            (8, 8): 'self.pr_click()',
            # Click next button
            (6, 9): 'self.next_click()',
            (7, 9): 'self.next_click()',
            (8, 9): 'self.next_click()',
            (9, 9): 'self.next_click()',
            (10, 9): 'self.next_click()',
            (6, 10): 'self.next_click()',
            (7, 10): 'self.next_click()',
            (8, 10): 'self.next_click()',
            (9, 10): 'self.next_click()',
            (10, 10): 'self.next_click()',
            # Click cencel button
            (1, 9): 'self.cancel_click()',
            (2, 9): 'self.cancel_click()',
            (3, 9): 'self.cancel_click()',
            (4, 9): 'self.cancel_click()',
            (5, 9): 'self.cancel_click()',
            (1, 10): 'self.cancel_click()',
            (2, 10): 'self.cancel_click()',
            (3, 10): 'self.cancel_click()',
            (4, 10): 'self.cancel_click()',
            (5, 10): 'self.cancel_click()',
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

    def as1_click(self):
        self.toggle_button("AS1")
    
    def as2_click(self):
        self.toggle_button("AS2")

    def mt1_click(self):
        self.toggle_button("MT1")

    def mt2_click(self):
        self.toggle_button("MT2")

    def pr_click(self):
        self.toggle_button("PR")

    def next_click(self):
        if self.as1_button:
            self.department_value += 'AS1'
        if self.as2_button:
            self.department_value += 'AS2'
        if self.mt1_button:
            self.department_value += 'MT1'
        if self.mt2_button:
            self.department_value += 'MT2'
        if self.pr_button:
            self.department_value += 'PR'

        if self.department_value != '':
            views.user_data.user_data['department'] = self.department_value
        else:
            print("Please select user deparment")

    def cancel_click(self):
        views.user_data.user_data['department'] = ''
        views.User_Lname(False).run()
        pygame.quit()

    def toggle_button(self, event):
        if event == "AS1":
            if self.as1_button:
                self.as1_button = False
            else:
                self.as1_button = True
        if event == "AS2":
            if self.as2_button:
                self.as2_button = False
            else:
                self.as2_button = True
        if event == "MT1":
            if self.mt1_button:
                self.mt1_button = False
            else:
                self.mt1_button = True
        if event == "MT2":
            if self.mt2_button:
                self.mt2_button = False
            else:
                self.mt2_button = True
        if event == "PR":
            if self.pr_button:
                self.pr_button = False
            else:
                self.pr_button = True           

    def run(self):
        """Initialize Caption and Valiable."""
        pygame.display.set_caption(self.caption + config.VERSION)
        print("User_data :", views.user_data.user_data)
        """Run the main event loop."""
        while self.running:
            self.screen.fill(Color('white'))      
            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position2 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 150, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 40, (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    if row == 0 and column == 0:
                        elements.Title(self.title, pos=(200, 67), app=(self.screen)).draw()  
                    """Initialize Button."""
                    if row == 3 and column == 1:
                        if self.as1_button:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   AS1', position3, app=(self.screen)).draw()
                    if row == 3 and column == 6:
                        if self.as2_button:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   AS2', position3, app=(self.screen)).draw()
                    if row == 5 and column == 1:
                        if self.mt1_button:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   MT1', position3, app=(self.screen)).draw()
                    if row == 5 and column == 6:
                        if self.mt2_button:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   MT2', position3, app=(self.screen)).draw()
                    if row == 7 and column == 4:
                        if self.pr_button:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 321, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 321, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('PR', position3, app=(self.screen)).draw()

                    if row == 9 and column == 1:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('CANCEL', position3, app=(self.screen)).draw()
                    if row == 9 and column == 6:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   NEXT', position3, app=(self.screen)).draw()
                   
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