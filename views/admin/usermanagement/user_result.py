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



class User_Result:
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
            self.caption = 'Update user information'
            self.title = 'Update USER INFORMATION'
        else:
            self.caption = 'Confirm user information'
            self.title = 'CONFIRM USER INFORMATION'

        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'home.App().run()',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }

        self.click = {
            # Click confirm button
            (8, 4): 'self.confirm_click()',
            (9, 4): 'self.confirm_click()',
            (10, 4): 'self.confirm_click()',
            (8, 5): 'self.confirm_click()',
            (9, 5): 'self.confirm_click()',
            (10, 5): 'self.confirm_click()',
            (8, 6): 'self.confirm_click()',
            (9, 6): 'self.confirm_click()',
            (10, 6): 'self.confirm_click()',
            # Click back button
            (8, 8): 'self.back_click()',
            (9, 8): 'self.back_click()',
            (10, 8): 'self.back_click()',
            (8, 9): 'self.back_click()',
            (9, 9): 'self.back_click()',
            (10, 9): 'self.back_click()',
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
        if (column_click, row_click) in self.click:
            exec(self.click[column_click, row_click])

    def confirm_click(self):
        self.set_data()
        services.insertperson(self.user_data)
        services.insertpermission(self.user_data[0], self.user_data[6])
        views.user_data.userdata_reset()
        print(views.user_data.user_data)
        views.User_Management().run()
        pygame.quit()

    def back_click(self):
        views.user_data.user_data['fingerid'] = ''
        views.User_Finger(False).run()
        pygame.quit()
    
    def set_data(self):
        self.user_data = []
        self.user_data.append(views.user_data.user_data['user_id'])
        self.user_data.append(views.user_data.user_data['user_name'])
        self.user_data.append(views.user_data.user_data['user_lname'])
        self.user_data.append(views.user_data.department())
        self.user_data.append(views.user_data.user_data['fingerid'])
        self.user_data.append(views.user_data.user_data['permission'])
        self.user_data.append(views.user_data.user_data['locker_access'])
        return self.user_data 

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
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 10, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 60)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 10, (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    if row == 0 and column == 0:
                        elements.Title(self.title, pos=(110, 67), app=(self.screen)).draw()
                        elements.Header_Table('USER INFORMATION', 1, 3, app=(self.screen)).draw()
                        elements.Header_Result('  User id : ', 1, 4, app=(self.screen)).draw()
                        elements.Header_Result('  User name : ', 1, 5, app=(self.screen)).draw()
                        elements.Header_Result('  User lastname : ', 1, 6, app=(self.screen)).draw()
                        elements.Header_Result('  User department : ', 1, 7, app=(self.screen)).draw()
                        elements.Header_Result('  User permission : ', 1, 8, app=(self.screen)).draw()
                        elements.Header_Result('  User locker access : ', 1, 9, app=(self.screen)).draw()
                        elements.Header_Result('  User finger id : ', 1, 10, app=(self.screen)).draw()
                        # User information
                        elements.Header_Table(views.user_data.user_data['user_id'], 4, 4, app=(self.screen)).draw()
                        elements.Header_Table(views.user_data.user_data['user_name'], 4, 5, app=(self.screen)).draw()
                        elements.Header_Table(views.user_data.user_data['user_lname'], 4, 6, app=(self.screen)).draw()
                        elements.Header_Table(views.user_data.department(), 4, 7, app=(self.screen)).draw()
                        elements.Header_Table(views.user_data.user_data['permission'], 4, 8, app=(self.screen)).draw()
                        elements.Header_Table(views.user_data.lengh_lockeraccess(), 4, 9, app=(self.screen)).draw()
                        elements.Header_Table(views.user_data.user_data['fingerid'], 4, 10, app=(self.screen)).draw()
                        elements.Rectangle(1, 4, 7, 7, app=(self.screen)).draw()
                    """Initialize Button."""
                    if row == 4 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 214, config.bheight + 134).Rect()
                        elements.Text_Button_Medium('  CONFIRM', position3, app=(self.screen)).draw()
                    if row == 8 and column == 8:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 214, config.bheight + 134).Rect()
                        elements.Text_Button_Medium('      BACK', position3, app=(self.screen)).draw()
                   
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