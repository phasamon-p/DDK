""" Search"""
import pygame
from pygame.locals import *
import time
import os
import config 
import elements
import views
import data_example

class User_Lockeraccess:
    """Create a single-window app with multiple scenes."""
    def __init__(self, editstage):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        self.editstage = editstage
        if config.locker_type == 0:
            self.locker_type = True # Set true of 12 lockers
        else:
            self.locker_type = False # Set false of 16 lockers

        if self.editstage:
            self.caption = 'Edit user locker access'
            self.title = 'EDIT USER LOCKER ACCESS'
        else:
            self.caption = 'Add user locker access'
            self.title = 'ADD USER LOCKER ACCESS'

        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'home.App().run()',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }
        if self.locker_type :
            # locker impression
            self.locker_one = ["A", "B", "C", "D", "E"]
            self.locker_two = ["F", "G", "H", "I", "J"]
            self.locker_three = ["K", "L"]
            # locker value variables
            self.locker_button = [False, False, False, False, False, False, False, False, False, False, False, False]
            self.lockeraccess_value = [False, False, False, False, False, False, False, False, False, False, False, False]
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
                (4, 7): 'self.toggle_button(11)',
                (5, 7): 'self.toggle_button(11)',
                (4, 8): 'self.toggle_button(11)',
                (5, 8): 'self.toggle_button(11)',
                # Click 12 button
                (6, 7): 'self.toggle_button(12)',
                (7, 7): 'self.toggle_button(12)',
                (6, 8): 'self.toggle_button(12)',
                (7, 8): 'self.toggle_button(12)',
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
        else :
            # locker impression
            self.locker_one = ["A", "B", "C", "D", "E"]
            self.locker_two = ["F", "G", "H", "I", "J"]
            self.locker_three = ["K", "L", "M", "N", "O"]
            self.locker_four = ["P"]
            # locker value variables
            self.locker_button = [False, False, False, False, False, False, False, False, False, False, False, False,  False, False, False, False]
            self.lockeraccess_value = [False, False, False, False, False, False, False, False, False, False, False, False,  False, False, False, False]
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
                (5, 9): 'self.toggle_button(16)',
                (6, 9): 'self.toggle_button(16)',
                (5, 10): 'self.toggle_button(16)',
                (6, 10): 'self.toggle_button(16)',
                # Click next button
                (7, 9): 'self.next_click()',
                (8, 9): 'self.next_click()',
                (9, 9): 'self.next_click()',
                (10, 9): 'self.next_click()',
                (7, 10): 'self.next_click()',
                (8, 10): 'self.next_click()',
                (9, 10): 'self.next_click()',
                (10, 10): 'self.next_click()',
                # Click cencel button
                (1, 9): 'self.cancel_click()',
                (2, 9): 'self.cancel_click()',
                (3, 9): 'self.cancel_click()',
                (4, 9): 'self.cancel_click()',
                (1, 10): 'self.cancel_click()',
                (2, 10): 'self.cancel_click()',
                (3, 10): 'self.cancel_click()',
                (4, 10): 'self.cancel_click()',
            }
        self.first_check()
        self.check = False

    def first_check(self):
        for x in range(len(views.user_data.user_data['locker_access'])):
            if views.user_data.user_data['locker_access'][x]:
                print("x", self.locker_button)
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

    def next_click(self):
        for x in range(len(self.locker_button)):
            if self.locker_button[x]:
                self.lockeraccess_value[x] = True
                self.check = True
            else:
                self.lockeraccess_value[x] = False

        if self.lockeraccess_value != '':
            if self.editstage:
                if self.check:
                    views.user_data.user_data['locker_access'] = self.lockeraccess_value
                    views.User_Finger(True).run()
                    pygame.quit()
                else:
                    print("Please select user locker access")
            else:
                if self.check:
                    views.user_data.user_data['locker_access'] = self.lockeraccess_value
                    views.User_Finger(False).run()
                    pygame.quit()
                else:
                    print("Please select user locker access")
        else:
            print("Please select user locker access")

    def cancel_click(self):
        if self.editstage:
            views.User_Permission(True).run()
            pygame.quit()
        else:
            views.user_data.lockeraccess_reset()
            views.User_Permission(False).run()
            pygame.quit()

    def toggle_button(self, event):
        if self.locker_button[event - 1]:
            self.locker_button[event - 1] = False
        else:
            self.locker_button[event - 1] = True

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
                    position2 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 50, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 25)
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 40, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 25)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 150, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    position5 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 100, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    if row == 0 and column == 0:
                        elements.Title(self.title, pos=(150, 67), app=(self.screen)).draw()  
                    """Initialize Button."""
                    if self.locker_type:
                        for index in range(5):
                            if row == 3 and column == index + (index + 1):
                                if self.locker_button[index]:
                                    elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                else:
                                    elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                if (index + 1) > 9:
                                    #elements.Text_Button_Medium(str(index + 1), position3, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_one[index], position3, app=(self.screen)).draw()
                                else:
                                    #elements.Text_Button_Medium(str(index + 1), position2, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_one[index], position2, app=(self.screen)).draw()
                        for index in range(5):
                            if row == 5 and column == index + (index + 1):
                                if self.locker_button[index + 5]:
                                    elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                else:
                                    elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                if (index + 6) > 9:
                                    #elements.Text_Button_Medium(str(index + 6), position3, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_two[index], position3, app=(self.screen)).draw()
                                else:
                                    #elements.Text_Button_Medium(str(index + 6), position2, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_two[index], position2, app=(self.screen)).draw()
                        for index in range(2):
                            if row == 7 and column == index + (index + 4):
                                if self.locker_button[index + 10]:
                                    elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                else:
                                    elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                if (index + 11) > 9:
                                    #elements.Text_Button_Medium(str(index + 11), position3, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_three[index], position3, app=(self.screen)).draw()
                                else:
                                    #elements.Text_Button_Medium(str(index + 11), position2, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_three[index], position2, app=(self.screen)).draw()
                        if row == 9 and column == 1:
                            elements.Button(self.screen, config.red, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                            elements.Text_Button_Medium('CANCEL', position4, app=(self.screen)).draw()
                        if row == 9 and column == 6:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                            elements.Text_Button_Medium('   NEXT', position4, app=(self.screen)).draw()
                    else:
                        for index in range(5):
                            if row == 3 and column == index + (index + 1):
                                if self.locker_button[index]:
                                    elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                else:
                                    elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                if (index + 1) > 9:
                                    #elements.Text_Button_Medium(str(index + 1), position3, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_one[index], position3, app=(self.screen)).draw()
                                else:
                                    #elements.Text_Button_Medium(str(index + 1), position2, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_one[index], position2, app=(self.screen)).draw()
                        for index in range(5):
                            if row == 5 and column == index + (index + 1):
                                if self.locker_button[index + 5]:
                                    elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                else:
                                    elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                if (index + 6) > 9:
                                    #elements.Text_Button_Medium(str(index + 6), position3, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_two[index], position3, app=(self.screen)).draw()
                                else:
                                    #elements.Text_Button_Medium(str(index + 6), position2, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_two[index], position2, app=(self.screen)).draw()
                        for index in range(5):
                            if row == 7 and column == index + (index + 1):
                                if self.locker_button[index + 10]:
                                    elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                else:
                                    elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                if (index + 6) > 9:
                                    #elements.Text_Button_Medium(str(index + 6), position3, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_three[index], position3, app=(self.screen)).draw()
                                else:
                                    #elements.Text_Button_Medium(str(index + 6), position2, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_three[index], position2, app=(self.screen)).draw()
                        for index in range(1):
                            if row == 9 and column == index + (index + 5):
                                if self.locker_button[index + 15]:
                                    elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                else:
                                    elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                                if (index + 6) > 9:
                                    #elements.Text_Button_Medium(str(index + 6), position3, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_four[index], position3, app=(self.screen)).draw()
                                else:
                                    #elements.Text_Button_Medium(str(index + 6), position2, app=(self.screen)).draw()
                                    elements.Text_Button_Medium(self.locker_four[index], position2, app=(self.screen)).draw()
                        # for index in range(2):
                        #     if row == 7 and column == index + (index + 4):
                        #         if self.locker_button[index + 10]:
                        #             elements.Button(self.screen, config.green, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                        #         else:
                        #             elements.Button(self.screen, config.blue, x, y, config.bwidth + 107, config.bheight + 67).Rect()
                        #         if (index + 11) > 9:
                        #             #elements.Text_Button_Medium(str(index + 11), position3, app=(self.screen)).draw()
                        #             elements.Text_Button_Medium(self.locker_three[index], position3, app=(self.screen)).draw()
                        #         else:
                        #             #elements.Text_Button_Medium(str(index + 11), position2, app=(self.screen)).draw()
                        #             elements.Text_Button_Medium(self.locker_three[index], position2, app=(self.screen)).draw()
                        if row == 9 and column == 1:
                            elements.Button(self.screen, config.red, x, y, config.bwidth + 321, config.bheight + 67).Rect()
                            elements.Text_Button_Medium(' CANCEL', position5, app=(self.screen)).draw()
                        if row == 9 and column == 7:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 321, config.bheight + 67).Rect()
                            elements.Text_Button_Medium('   NEXT', position5, app=(self.screen)).draw()
                   
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