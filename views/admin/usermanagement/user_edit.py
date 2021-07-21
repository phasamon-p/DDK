""" Search"""
import pygame
from pygame.locals import *
import time
import os
import config 
import elements
import services
import views
import data_example

class user_list():
    user_id = ""
    user_name = ""
    user_lname = ""
    department = ""
    fingerid = ""
    permission = ""
    locker = ""

class userdata_edit():
    user_id = ""
    user_name = ""
    user_lname = ""
    department = ""
    fingerid = ""
    permission = ""
    locker = ""

class User_Edit:
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
        self.user_data = views.user_data.request_list
        self.user_list = user_list() 
        self.user_edit = userdata_edit()

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
            (8, 3): 'self.search_click()',
            (9, 3): 'self.search_click()',
            (10, 3): 'self.search_click()',
            # Click search button
            (8, 4): 'self.edit_click()',
            (9, 4): 'self.edit_click()',
            (10, 4): 'self.edit_click()',
            # Click delete button
            (8, 5): 'self.delete_click()',
            (9, 5): 'self.delete_click()',
            (10, 5): 'self.delete_click()',
            # Click cancel button
            (8, 10): 'self.cancel_click()',
            (9, 10): 'self.cancel_click()',
            (10, 10): 'self.cancel_click()',
            # # Click edit information button
            # (1, 9): 'self.editinformation_click()',
            # (2, 9): 'self.editinformation_click()',
            # (3, 9): 'self.editinformation_click()',
            # (1, 10): 'self.editinformation_click()',
            # (2, 10): 'self.editinformation_click()',
            # (3, 10): 'self.editinformation_click()',
            # # Click next button
            # (5, 9): 'self.editinventory_click()',
            # (6, 9): 'self.editinventory_click()',
            # (7, 9): 'self.editinventory_click()',
            # (5, 10): 'self.editinventory_click()',
            # (6, 10): 'self.editinventory_click()',
            # (7, 10): 'self.editinventory_click()',
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

    def search_click(self):
        self.data = services.selectpersonbyid(self.search_value.replace("\r", ""))
        
        if self.data[0]:
            print(self.data)
            self.user_list.user_id = self.data[1][0][0]
            self.user_list.user_name = self.data[1][0][1]
            self.user_list.user_lname = self.data[1][0][2]
            self.user_list.department = self.data[1][0][3]
            self.user_list.fingerid = self.data[1][0][4]
            self.user_list.permission = self.data[1][0][5]
            self.user_list.locker = services.getpermission_byid_string(self.data[1][0][0])
            views.user_data.list_reset()
            views.user_data.list_add(self.user_list)
        else:
            views.user_data.userdata_reset()
            views.user_data.list_reset()
            print("don't have product")

    def delete_click(self):
        if len(views.user_data.request_list) > 0:
            print("delete")
            services.deletepersonbyid(self.data[1][0][0])
            services.deletepermissionbyid(self.data[1][0][0])
            self.search_input.update("*")
            views.user_data.userdata_reset()
            views.user_data.list_reset()
        else:
            print("Please searching product")

    def cancel_click(self):
        views.user_data.userdata_reset()
        views.user_data.list_reset()
        views.User_Management().run() 
        pygame.quit()

    def edit_click(self):
        if len(views.user_data.request_list) > 0:
            self.setdata()
            views.User_Id(True).run() 
            pygame.quit()
        else:
            print("Please searching product")
    
    def setdata(self):
        if self.data[0]:
            self.user_edit.user_id = self.data[1][0][0]
            self.user_edit.user_name = self.data[1][0][1]
            self.user_edit.user_lname = self.data[1][0][2]
            self.user_edit.department = services.getdepartmentbyid_bool(self.data[1][0][0])
            self.user_edit.fingerid = str(self.data[1][0][4])
            self.user_edit.permission = self.data[1][0][5]
            self.user_edit.locker = services.getpermission_byid_bool(self.data[1][0][0])
        views.user_data.userdata_setedit(self.user_edit)

    def run(self):
        """Initialize Caption and Valiable."""
        pygame.display.set_caption('Product search' + config.VERSION)
        self.search_input = elements.User_Search(1, 3, 7, 1, app = (self.screen), active = True, numpad_active = True)

        """Run the main event loop."""
        while self.running:
            self.number = 1
            self.screen.fill(Color('white'))
            self.user_listview = elements.Useredit_Listview(1, 5, 7, 4, app=(self.screen),data = self.user_data, index = self.index)
            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position2 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) , (config.margin + config.bheight) * row + (config.bheight / 3.5) + 10)
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) , (config.margin + config.bheight) * row + (config.bheight / 3.5) + 50)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 20, (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position5 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) - 15, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    if row == 0 and column == 0:
                        elements.Title('PRODUCT SEARCH', pos=(320, 67), app=(self.screen)).draw()
                        elements.Header_Table('ID', 1, 4, app=(self.screen)).draw()
                        elements.Header_Table('Name', 3, 4, app=(self.screen)).draw()
                        elements.Header_Table('Lastname', 5, 4, app=(self.screen)).draw()
                        elements.Header_Table('Permis..', 7, 4, app=(self.screen)).draw()
                        # elements.Header_Table('Locker', 7, 4, app=(self.screen)).draw()
                        elements.Header_Table('Output', 1, 9, app=(self.screen)).draw()
                        elements.Rectangle(1, 10, 7, 1, app=(self.screen)).draw()
                        self.search_input.draw() 
                        self.user_listview.draw()                     
                    if row == 3 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 214, config.bheight).Rect()
                        elements.Text_Button_Medium('   SEARCH', position4, app=(self.screen)).draw()
                    if row == 4 and column == 8:
                        elements.Button(self.screen, config.blue, x, y, config.bwidth + 214, config.bheight).Rect()
                        elements.Text_Button_Medium('     EDIT', position4, app=(self.screen)).draw()
                    if row == 5 and column == 8:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 214, config.bheight).Rect()
                        elements.Text_Button_Medium('   DELETE', position4, app=(self.screen)).draw() 
                    """Initialize Numpad."""
                    if row >= 6 and row <= 9 and column >= 8 and column <= 10:
                        if row == 9 and column == 8:
                            elements.Button(self.screen, config.light_blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number('*', position, app=(self.screen)).draw()
                        elif row == 9 and column == 9:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number(str(0), position, app=(self.screen)).draw()
                        elif row == 9 and column == 10:
                            elements.Button(self.screen, config.light_blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number('#', position, app=(self.screen)).draw()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number(str(self.number), position, app=(self.screen)).draw()
                        self.number += 1
                    if row == 10 and column == 8:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 214, config.bheight).Rect()
                        elements.Text_Button_Medium('     BACK', position4, app=(self.screen)).draw()
                                

            for event in pygame.event.get():
                self.search_value = self.search_input.handle_event(event)
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