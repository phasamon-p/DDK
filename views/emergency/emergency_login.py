""" Search"""
import pygame
from pygame.locals import *
import time
import os
import config 
import elements
import views
import data_example
import services



class emergency_login :
    """Create a single-window app with multiple scenes."""

    def __init__(self):
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
        self.message = False
        self.message2 = False
        self.caption = 'EMERGENCY LOGIN'
        self.title = 'EMERGENCY LOGIN'
   
        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'home.App().run()',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }

        self.click = {
            # Click next button
            (8, 8): 'self.next_click()',
            (9, 8): 'self.next_click()',
            (10,8): 'self.next_click()',
            (8, 9): 'self.next_click()',
            (9, 9): 'self.next_click()',
            (10,9): 'self.next_click()',
            # Click cancel button
            (8, 10): 'self.cancel_click()',
            (9, 10): 'self.cancel_click()',
            (10, 10): 'self.cancel_click()',
            (8, 11): 'self.cancel_click()',
            (9, 11): 'self.cancel_click()',
            (10, 11): 'self.cancel_click()',
        }
        self.tout = config.time_out
        self.start_time = time.time()

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

    def next_click(self):
        if self.userid_value != '':
            if config.locker_type == 0:
                if  services.checkuserbyid(self.userid_value)[0]:
                    views.emergency_data.emergency_data['user_id'] = self.userid_value
                    views.emergency_mode().run();
                    pygame.quit()
                else:
                    self.message=False
                    self.message2 = True
            else:
                if  services.checkuserbyid(self.userid_value)[0]:
                    views.emergency_data.emergency_data['user_id'] = self.userid_value
                    views.emergency_mode().run();
                    pygame.quit()
                else:
                    self.message=False
                    self.message2 = True      
        else:
            self.message2 = False
            self.message = True
            print("Please enter user name")

    def cancel_click(self):
        views.emergency_data.emergency_data['user_id'] = ''
        views.Home().run()
        pygame.quit()

    def pagetimeout(self):  # function check timeout after touch
        if (time.time() - self.start_time) > self.tout:
            return True 
    def run(self):
        """Initialize Caption and Valiable."""
        pygame.display.set_caption(self.caption + config.VERSION)
        self.username_input = elements.InputBox_Text(1, 3, 10, 1, views.user_data.user_data['user_name'], app = (self.screen), active = True, numpad_active = True)
        """Run the main event loop."""
        while self.running:

            if(self.pagetimeout()):
                views.Home().run()
                pygame.quit() 
                
            self.screen.fill(Color('white'))      
            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position2 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 10, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 10, (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    if row == 0 and column == 0:
                        elements.Title(self.title, pos=(370, 67), app=(self.screen)).draw()
                        elements.Header_Table('MESSAGE', 1, 4, app=(self.screen)).draw()
                        elements.Rectangle(1, 5, 7, 4, app=(self.screen)).draw()
                        elements.Header_Table('OUTPUT', 1, 9, app=(self.screen)).draw()
                        elements.Rectangle(1, 10, 7, 1, app=(self.screen)).draw()
                  
                         
                
                        elements.Header_Table('  1. Enter employee code.', 1, 5, app=(self.screen)).draw()
                        elements.Header_Table("  2. Press LOGIN button.", 1, 6, app=(self.screen)).draw()
                        elements.Header_Table("  3. Press the locker you want to open.", 1, 7, app=(self.screen)).draw()
                        if self.message:
                            elements.Output_Message("  •  Please enter employee code", 1, 10, app=(self.screen)).draw()
                        if self.message2:
                            elements.Output_Message("  •  You don't have permission.", 1, 10, app=(self.screen)).draw()
                        self.username_input.draw()                  
                    """Initialize Button."""
                    if row == 4 and column == 8:
                        elements.Button(self.screen, config.blue, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('BACKSPACE', position3, app=(self.screen)).draw()
                    if row == 6 and column == 8:
                        elements.Button(self.screen, config.dark_gray, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('     CLEAR', position3, app=(self.screen)).draw()
                    if row == 8 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('     LOGIN', position3, app=(self.screen)).draw()
                    if row == 10 and column == 8:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 214, config.bheight).Rect()
                        elements.Text_Button_Medium('    CANCEL', position4, app=(self.screen)).draw()
                   

            for event in pygame.event.get():
                self.userid_value = self.username_input.handle_event(event)
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