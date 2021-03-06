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

class locker_control_emegency:
    """Create a single-window app with multiple scenes."""
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        self.caption = 'locker control'
        self.title = 'LOCKER CONTROL'

        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'home.App().run()',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }
        
        if config.locker_type == 0:
            self.locker_type = True # Set true of 12 lockers
        else:
            self.locker_type = False # Set false of 16 lockers

        if self.locker_type :
            # locker impression
            self.locker_one = ["A", "B", "C", "D", "E"]
            self.locker_two = ["F", "G", "H", "I", "J"]
            self.locker_three = ["K", "L"]
            # locker value variables
            self.locker_button = [False, False, False, False, False, False, False, False, False, False, False, False]
            self.productlocker_value = [False, False, False, False, False, False, False, False, False, False, False, False]
            # Position click
            self.click = {
                # Click 1 button
                (1, 3): 'self.toggle_button(1)',
                (2, 3): 'self.toggle_button(1)',
                (1, 4): 'self.toggle_button(1)',
                (2, 4): 'self.toggle_button(1)',
                # Click 2 button
                (3, 3): 'self.toggle_button(2)',
                (4, 3): 'self.toggle_button(2)',
                (3, 4): 'self.toggle_button(2)',
                (4, 4): 'self.toggle_button(2)',
                # Click 3 button
                (5, 3): 'self.toggle_button(3)',
                (6, 3): 'self.toggle_button(3)',
                (5, 4): 'self.toggle_button(3)',
                (6, 4): 'self.toggle_button(3)',
                # Click 4 button
                (7, 3): 'self.toggle_button(4)',
                (8, 3): 'self.toggle_button(4)',
                (7, 4): 'self.toggle_button(4)',
                (8, 4): 'self.toggle_button(4)',
                # Click 5 button
                (9, 3): 'self.toggle_button(5)',
                (10, 3): 'self.toggle_button(5)',
                (9, 4): 'self.toggle_button(5)',
                (10, 4): 'self.toggle_button(5)',
                # Click 6 button
                (1, 5): 'self.toggle_button(6)',
                (2, 5): 'self.toggle_button(6)',
                (1, 6): 'self.toggle_button(6)',
                (2, 6): 'self.toggle_button(6)',
                # Click 7 button
                (3, 5): 'self.toggle_button(7)',
                (4, 5): 'self.toggle_button(7)',
                (3, 6): 'self.toggle_button(7)',
                (4, 6): 'self.toggle_button(7)',
                # Click 8 button
                (5, 5): 'self.toggle_button(8)',
                (6, 5): 'self.toggle_button(8)',
                (5, 6): 'self.toggle_button(8)',
                (6, 6): 'self.toggle_button(8)',
                # Click 9 button
                (7, 5): 'self.toggle_button(9)',
                (8, 5): 'self.toggle_button(9)',
                (7, 6): 'self.toggle_button(9)',
                (8, 6): 'self.toggle_button(9)',
                # Click 10 button
                (9, 5): 'self.toggle_button(10)',
                (10, 5): 'self.toggle_button(10)',
                (9, 6): 'self.toggle_button(10)',
                (10, 6): 'self.toggle_button(10)',
                # Click 11 button
                (1, 7): 'self.toggle_button(11)',
                (2, 7): 'self.toggle_button(11)',
                (1, 8): 'self.toggle_button(11)',
                (2, 8): 'self.toggle_button(11)',
                # Click 12 button
                (3, 7): 'self.toggle_button(12)',
                (4, 7): 'self.toggle_button(12)',
                (3, 8): 'self.toggle_button(12)',
                (4, 8): 'self.toggle_button(12)',
                # Click cencel button
                (9, 9): 'self.cancel_click()',
                (10, 9): 'self.cancel_click()',
                (9, 10): 'self.cancel_click()',
                (10, 10): 'self.cancel_click()',
                }
        else:
                # locker impression
            self.locker_one = ["A", "B", "C", "D", "E"]
            self.locker_two = ["F", "G", "H", "I", "J"]
            self.locker_three = ["K", "L", "M", "N", "O"]
            self.locker_four = ["P"]
            # locker value variables
            self.locker_button = [False, False, False, False, False, False, False, False, False, False, False, False,  False, False, False, False]
            self.productlocker_value = [False, False, False, False, False, False, False, False, False, False, False, False,  False, False, False, False]
            # Position click
            self.click = {
                # Click 1 button
                (1, 3): 'self.toggle_button(1)',
                (2, 3): 'self.toggle_button(1)',
                (1, 4): 'self.toggle_button(1)',
                (2, 4): 'self.toggle_button(1)',
                # Click 2 button
                (3, 3): 'self.toggle_button(2)',
                (4, 3): 'self.toggle_button(2)',
                (3, 4): 'self.toggle_button(2)',
                (4, 4): 'self.toggle_button(2)',
                # Click 3 button
                (5, 3): 'self.toggle_button(3)',
                (6, 3): 'self.toggle_button(3)',
                (5, 4): 'self.toggle_button(3)',
                (6, 4): 'self.toggle_button(3)',
                # Click 4 button
                (7, 3): 'self.toggle_button(4)',
                (8, 3): 'self.toggle_button(4)',
                (7, 4): 'self.toggle_button(4)',
                (8, 4): 'self.toggle_button(4)',
                # Click 5 button
                (9, 3): 'self.toggle_button(5)',
                (10, 3): 'self.toggle_button(5)',
                (9, 4): 'self.toggle_button(5)',
                (10, 4): 'self.toggle_button(5)',
                # Click 6 button
                (1, 5): 'self.toggle_button(6)',
                (2, 5): 'self.toggle_button(6)',
                (1, 6): 'self.toggle_button(6)',
                (2, 6): 'self.toggle_button(6)',
                # Click 7 button
                (3, 5): 'self.toggle_button(7)',
                (4, 5): 'self.toggle_button(7)',
                (3, 6): 'self.toggle_button(7)',
                (4, 6): 'self.toggle_button(7)',
                # Click 8 button
                (5, 5): 'self.toggle_button(8)',
                (6, 5): 'self.toggle_button(8)',
                (5, 6): 'self.toggle_button(8)',
                (6, 6): 'self.toggle_button(8)',
                # Click 9 button
                (7, 5): 'self.toggle_button(9)',
                (8, 5): 'self.toggle_button(9)',
                (7, 6): 'self.toggle_button(9)',
                (8, 6): 'self.toggle_button(9)',
                # Click 10 button
                (9, 5): 'self.toggle_button(10)',
                (10, 5): 'self.toggle_button(10)',
                (9, 6): 'self.toggle_button(10)',
                (10, 6): 'self.toggle_button(10)',
                # Click 11 button
                (1, 7): 'self.toggle_button(11)',
                (2, 7): 'self.toggle_button(11)',
                (1, 8): 'self.toggle_button(11)',
                (2, 8): 'self.toggle_button(11)',
                # Click 12 button
                (3, 7): 'self.toggle_button(12)',
                (4, 7): 'self.toggle_button(12)',
                (3, 8): 'self.toggle_button(12)',
                (4, 8): 'self.toggle_button(12)',
                # Click 13 button
                (5, 7): 'self.toggle_button(13)',
                (6, 7): 'self.toggle_button(13)',
                (5, 8): 'self.toggle_button(13)',
                (6, 8): 'self.toggle_button(13)',
                # Click 14 button
                (7, 7): 'self.toggle_button(14)',
                (8, 7): 'self.toggle_button(14)',
                (7, 8): 'self.toggle_button(14)',
                (8, 8): 'self.toggle_button(14)',
                # Click 15 button
                (9, 7): 'self.toggle_button(15)',
                (10, 7): 'self.toggle_button(15)',
                (9, 8): 'self.toggle_button(15)',
                (10, 8): 'self.toggle_button(15)',
                # Click 16 button
                (1, 9): 'self.toggle_button(16)',
                (2, 9): 'self.toggle_button(16)',
                (1, 10): 'self.toggle_button(16)',
                (2, 10): 'self.toggle_button(16)',
                # Click cencel button
                (9, 9): 'self.cancel_click()',
                (10, 9): 'self.cancel_click()',
                (9, 10): 'self.cancel_click()',
                (10, 10): 'self.cancel_click()',
                }
        self.first_check()
        self.tout = config.time_out
        self.start_time = time.time()

    def first_check(self):
        for x in range(len(views.product_data.product_data['locker_number'])):
            if views.product_data.product_data['locker_number'][x]:
                self.locker_button[x] = True

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

    def cancel_click(self):
        if services.lockertimeout():
                views.emergency_data.emergrncydata_reset()
                views.Home().run()
                pygame.quit()
        else: 
                print("Plese close door")

    def toggle_button(self, event):
        if self.locker_button[event - 1]:
            if config.locker_type == 0:
                self.locker_button[event - 1] = False
                services.locker_close(0, event)
            else:
                """" add 16 locker control """
                self.locker_button[event - 1] = False
                services.locker_close(0, event)
        else:
            if config.locker_type == 0:
                self.locker_button[event - 1] = True
                services.locker_open(0, event)
                services.insert_emegency_log(views.emergency_data.emergency_data,event)
                views.emergency_data.emergrncydata_reset()
                views.Home().run()
                pygame.quit()
        
            else:
                """" add 16 locker control """
                self.locker_button[event - 1] = True
                services.locker_open(0, event)
                services.insert_emegency_log(views.emergency_data.emergency_data,event)
                views.emergency_data.emergrncydata_reset()
                views.Home().run()
                pygame.quit()

    def checklocker_status(self):
        if config.locker_type == 0:
            # Check status locker 8
            if services.getStatus(1):
                    self.locker_button[7] = True 
            else:
                    self.locker_button[7] = False
            # Check status locker 7
            if services.getStatus(2):
                    self.locker_button[6] = True 
            else:
                    self.locker_button[6] = False
            # Check status locker 6
            if services.getStatus(3):
                    self.locker_button[5] = True 
            else:
                    self.locker_button[5] = False
            # Check status locker 5
            if services.getStatus(4):
                    self.locker_button[4] = True 
            else:
                    self.locker_button[4] = False
            # Check status locker 4
            if services.getStatus(5):
                    self.locker_button[3] = True 
            else:
                    self.locker_button[3] = False
            # Check status locker 3
            if services.getStatus(6):
                    self.locker_button[2] = True 
            else:
                    self.locker_button[2] = False
            # Check status locker 2
            if services.getStatus(7):
                    self.locker_button[1] = True 
            else:
                    self.locker_button[1] = False
            # Check status locker 1
            if services.getStatus(8):
                    self.locker_button[0] = True 
            else:
                    self.locker_button[0] = False
            # Check status locker 12
            if services.getStatus(13):
                    self.locker_button[11] = True 
            else:
                    self.locker_button[11] = False
            # Check status locker 11
            if services.getStatus(14):
                    self.locker_button[10] = True 
            else:
                    self.locker_button[10] = False
            # Check status locker 10
            if services.getStatus(15):
                    self.locker_button[9] = True 
            else:
                    self.locker_button[9] = False
            # Check status locker 9
            if services.getStatus(16):
                    self.locker_button[8] = True 
            else:
                    self.locker_button[8] = False
        else:
            # Check status locker 8
            if services.getStatus(1):
                    self.locker_button[7] = True 
            else:
                    self.locker_button[7] = False
            # Check status locker 7
            if services.getStatus(2):
                    self.locker_button[6] = True 
            else:
                    self.locker_button[6] = False
            # Check status locker 6
            if services.getStatus(3):
                    self.locker_button[5] = True 
            else:
                    self.locker_button[5] = False
            # Check status locker 5
            if services.getStatus(4):
                    self.locker_button[4] = True 
            else:
                    self.locker_button[4] = False
            # Check status locker 4
            if services.getStatus(5):
                    self.locker_button[3] = True 
            else:
                    self.locker_button[3] = False
            # Check status locker 3
            if services.getStatus(6):
                    self.locker_button[2] = True 
            else:
                    self.locker_button[2] = False
            # Check status locker 2
            if services.getStatus(7):
                    self.locker_button[1] = True 
            else:
                    self.locker_button[1] = False
            # Check status locker 1
            if services.getStatus(8):
                    self.locker_button[0] = True 
            else:
                    self.locker_button[0] = False
            # Check status locker 16
            if services.getStatus(9):
                    self.locker_button[15] = True 
            else:
                    self.locker_button[15] = False
            # Check status locker 15
            if services.getStatus(10):
                    self.locker_button[14] = True 
            else:
                    self.locker_button[14] = False
            # Check status locker 14
            if services.getStatus(11):
                    self.locker_button[13] = True 
            else:
                    self.locker_button[13] = False
            # Check status locker 13
            if services.getStatus(12):
                    self.locker_button[12] = True 
            else:
                    self.locker_button[12] = False
            # Check status locker 12
            if services.getStatus(13):
                    self.locker_button[11] = True 
            else:
                    self.locker_button[11] = False
            # Check status locker 11
            if services.getStatus(14):
                    self.locker_button[10] = True 
            else:
                    self.locker_button[10] = False
            # Check status locker 10
            if services.getStatus(15):
                    self.locker_button[9] = True 
            else:
                    self.locker_button[9] = False
            # Check status locker 9
            if services.getStatus(16):
                    self.locker_button[8] = True 
            else:
                    self.locker_button[8] = False

    def pagetimeout(self):  # function check timeout after touch
        if (time.time() - self.start_time) > self.tout:
            return True

    def run(self):
        """Initialize Caption and Valiable."""
        print("User_data :", views.emergency_data.emergency_data)
        pygame.display.set_caption(self.caption + config.VERSION)


        """Run the main event loop."""
        while self.running:

            if(self.pagetimeout()) and services.lockertimeout():
                views.Home().run()
                pygame.quit()    

            services.lockertimeout()
            self.screen.fill(Color('white'))  
            self.checklocker_status()    
            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position2 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 50, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 25)
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 50, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 25)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 10, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    if row == 0 and column == 0:
                        elements.Title(self.title, pos=(330, 67), app=(self.screen)).draw() 
                    """Initialize Button."""
                    if self.locker_type :
                        for index in range(5):
                                if row == 3 and column == index + (index + 1):
                                        if self.locker_button[index]:
                                                elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        else:
                                                elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        elements.Text_Button_Medium(self.locker_one[index], position3, app=(self.screen)).draw()
                        for index in range(5):
                                if row == 5 and column == index + (index + 1):
                                        if self.locker_button[index + 5]:
                                                elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        else:
                                                elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        elements.Text_Button_Medium(self.locker_two[index], position3, app=(self.screen)).draw()
                        for index in range(2):
                                if row == 7 and column == index + (index + 1):
                                        if self.locker_button[index + 10]:
                                                elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        else:
                                                elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        elements.Text_Button_Medium(self.locker_three[index], position3, app=(self.screen)).draw()                  
                        if row == 9 and column == 9:
                                elements.Button(self.screen, config.red, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                elements.Text_Button_Medium('CANCEL  ', position4, app=(self.screen)).draw()
                    else :
                        for index in range(5):
                                if row == 3 and column == index + (index + 1):
                                        if self.locker_button[index]:
                                                elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        else:
                                                elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        elements.Text_Button_Medium(self.locker_one[index], position3, app=(self.screen)).draw()
                        for index in range(5):
                                if row == 5 and column == index + (index + 1):
                                        if self.locker_button[index + 5]:
                                                elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        else:
                                                elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        elements.Text_Button_Medium(self.locker_two[index], position3, app=(self.screen)).draw()
                        for index in range(5):
                                if row == 7 and column == index + (index + 1):
                                        if self.locker_button[index + 10]:
                                                elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        else:
                                                elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        elements.Text_Button_Medium(self.locker_three[index], position3, app=(self.screen)).draw()
                        for index in range(1):
                                if row == 9 and column == index + (index + 1):
                                        if self.locker_button[index + 15]:
                                                elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        else:
                                                elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                        elements.Text_Button_Medium(self.locker_four[index], position3, app=(self.screen)).draw()                  
                        if row == 9 and column == 9:
                                elements.Button(self.screen, config.red, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                elements.Text_Button_Medium('CANCEL  ', position4, app=(self.screen)).draw()                 
                   
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