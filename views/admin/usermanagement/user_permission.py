""" Search"""
import pygame
from pygame.locals import *
import time
import os
import config 
import elements
import views
import data_example

class User_Permission:
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
        self.permission_value = ''
        self.general_button = False
        self.admin_button = False
        self.emergency_button = False
        
        if views.user_data.user_data['permission'] == "general":
            self.general_button = True
        elif views.user_data.user_data['permission'] == "admin":
            self.admin_button = True
        elif views.user_data.user_data['permission'] == "emergency":
            self.emergency_button = True
        else:
            self.general_button = False
            self.admin_button = False
            self.emergency_button = False

        if self.editstage:
            self.caption = 'Edit user permission'
            self.title = 'EDIT USER PERMISSION'
        else:
            self.caption = 'Add user permission'
            self.title = 'ADD USER PERMISSION'

        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'home.App().run()',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }

        self.click = {
            # Click general button
            (1, 3): 'self.general_click()',
            (2, 3): 'self.general_click()',
            (3, 3): 'self.general_click()',
            (4, 3): 'self.general_click()',
            (5, 3): 'self.general_click()',
            (6, 3): 'self.general_click()',
            (7, 3): 'self.general_click()',
            (8, 3): 'self.general_click()',
            (9, 3): 'self.general_click()',
            (1, 4): 'self.general_click()',
            (2, 4): 'self.general_click()',
            (3, 4): 'self.general_click()',
            (4, 4): 'self.general_click()',
            (5, 4): 'self.general_click()',
            (6, 4): 'self.general_click()',
            (7, 4): 'self.general_click()',
            (8, 4): 'self.general_click()',
            (9, 4): 'self.general_click()',
            # Click admin button
            (1, 5): 'self.admin_click()',
            (2, 5): 'self.admin_click()',
            (3, 5): 'self.admin_click()',
            (4, 5): 'self.admin_click()',
            (5, 5): 'self.admin_click()',
            (6, 5): 'self.admin_click()',
            (7, 5): 'self.admin_click()',
            (8, 5): 'self.admin_click()',
            (9, 5): 'self.admin_click()',
            (1, 6): 'self.admin_click()',
            (2, 6): 'self.admin_click()',
            (3, 6): 'self.admin_click()',
            (4, 6): 'self.admin_click()',
            (5, 6): 'self.admin_click()',
            (6, 6): 'self.admin_click()',
            (7, 6): 'self.admin_click()',
            (8, 6): 'self.admin_click()',
            (9, 6): 'self.admin_click()',
            # Click admin button
            (1, 7): 'self.emergency_click()',
            (2, 7): 'self.emergency_click()',
            (3, 7): 'self.emergency_click()',
            (4, 7): 'self.emergency_click()',
            (5, 7): 'self.emergency_click()',
            (6, 7): 'self.emergency_click()',
            (7, 7): 'self.emergency_click()',
            (8, 7): 'self.emergency_click()',
            (9, 7): 'self.emergency_click()',
            (1, 8): 'self.emergency_click()',
            (2, 8): 'self.emergency_click()',
            (3, 8): 'self.emergency_click()',
            (4, 8): 'self.emergency_click()',
            (5, 8): 'self.emergency_click()',
            (6, 8): 'self.emergency_click()',
            (7, 8): 'self.emergency_click()',
            (8, 8): 'self.emergency_click()',
            (9, 8): 'self.emergency_click()',
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

    def general_click(self):
        if self.editstage:
            if views.user_data.user_data['permission'] !='emergency':
                self.toggle_button("GENERAL")
        else:
            self.toggle_button("GENERAL")
    
    def admin_click(self):
        if self.editstage:
            if views.user_data.user_data['permission'] !='emergency':
                self.toggle_button("ADMIN")
        else:
            self.toggle_button("ADMIN")

    def emergency_click(self):
        if self.editstage:
            if views.user_data.user_data['permission'] =='emergency' or views.user_data.user_data['permission'] =='':
                self.toggle_button("EMERGENCY")
        else:
            self.toggle_button("EMERGENCY")



    def next_click(self):
        if self.general_button:
            self.permission_value = 'general'
        if self.admin_button:
            self.permission_value += 'admin'
        if self.emergency_button:
            self.permission_value += 'emergency'

        if self.permission_value != '':
            if self.editstage:
                views.user_data.user_data['permission'] = self.permission_value
                if self.permission_value == 'emergency':
                    if config.locker_type == 0:
                        views.user_data.user_data['locker_access'] = [True, True, True, True, True, True, True, True, True, True, True, True]
                    else:
                        views.user_data.user_data['locker_access'] = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
                    views.User_Result(True).run()
                    pygame.quit()
                else:
                    views.User_Lockeraccess(True).run()
                    pygame.quit()
            else:
                views.user_data.user_data['permission'] = self.permission_value
                if self.permission_value == 'emergency':
                    if config.locker_type == 0:
                        views.user_data.user_data['locker_access'] = [True, True, True, True, True, True, True, True, True, True, True, True]
                    else:
                        views.user_data.user_data['locker_access'] = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
                    views.user_data.user_data['fingerid'] = str(0)
                    views.User_Result(False).run()
                    pygame.quit()
                else:
                    views.User_Lockeraccess(False).run()
                    pygame.quit()   
                
        else:
            print("Please select user permission")

    def cancel_click(self):
        if self.editstage:
            views.User_Department(True).run()
            pygame.quit()
        else:
            views.user_data.user_data['permission'] = ''
            views.User_Department(False).run()
            pygame.quit()
    def toggle_button(self, event):
        if event == "GENERAL":
            if self.general_button:
                self.general_button = False
            else:
                self.general_button = True
                self.admin_button = False
                self.emergency_button = False
        if event == "ADMIN":
            if self.admin_button:
                self.admin_button = False
            else:
                self.admin_button = True
                self.general_button = False
                self.emergency_button = False           
        if event == "EMERGENCY":
            if self.emergency_button:
                self.emergency_button = False
            else:
                self.emergency_button= True
                self.general_button = False
                self.admin_button = False       

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
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 400, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 150, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    if row == 0 and column == 0:
                        elements.Title(self.title, pos=(250, 67), app=(self.screen)).draw()  
                    """Initialize Button."""
                    if row == 3 and column == 1:
                        if self.general_button:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 963, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 963, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('  GENERAL', position3, app=(self.screen)).draw()
                    if row == 5 and column == 1:
                        if self.admin_button:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 963, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 963, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   ADMIN', position3, app=(self.screen)).draw()

                    if row == 7 and column == 1:
                        if self.emergency_button:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 963, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 963, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('EMERGENCY', position3, app=(self.screen)).draw()  

                    if row == 9 and column == 1:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('CANCEL', position4, app=(self.screen)).draw()
                    if row == 9 and column == 6:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   NEXT', position4, app=(self.screen)).draw()
                   
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