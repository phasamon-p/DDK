""" Home (Main app) """
import pygame
from pygame.locals import *

import time
import os
import services
import config 
import elements
import views

class admin_data():
    admin_id = ""
    admin_name = ""
    admin_lname = ""
    department = ""
    fingerid = ""
    permission = ""
    locker = ""

class Admin_Finger:
    """Create a single-window app with multiple scenes."""
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        self.admin_information = admin_data()
        self.caption = 'Admin finger scan'
        self.title = 'ADMIN FINGER SCAN'
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

    def exit_fullscreen(self):
        services.getfingerid()
        print("alt+X")
        config.flags = RESIZABLE
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen

    def scan_click(self):
        self.fingerid = services.get_fingerprint()
        if self.fingerid:
            # print("finger id", self.fingerid[1])
            self.admin_data = services.getpersonbyfingerid(self.fingerid[1])
            # print(self.admin_data)
            if self.admin_data[0]:
                if self.admin_data[1][0][5] == 'admin':
                    self.setdata()
                    services.insert_adminlog(views.admin_data.admin_data)
                    views.System_Management().run()
                    pygame.quit()
                else:
                    print("You don't have permission to admin management")
                    views.Home().run()
                    pygame.quit()
            else:
                print("Do not have your finger print")
        else:
            print("Do not have your finger print")
        
    def back_click(self):
        views.Home().run()
        pygame.quit()

    def setdata(self):
        if self.admin_data[0]:
            self.admin_information.admin_id = self.admin_data[1][0][0]
            self.admin_information.admin_name = self.admin_data[1][0][1]
            self.admin_information.admin_lname = self.admin_data[1][0][2]
            self.admin_information.department = services.getdepartmentbyid_bool(self.admin_data[1][0][0])
            self.admin_information.fingerid = str(self.admin_data[1][0][4])
            self.admin_information.permission = self.admin_data[1][0][5]
            self.admin_information.locker = services.getpermission_byid_bool(self.admin_data[1][0][0])
        views.admin_data.admindata_setedit(self.admin_information)
    
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
                        elements.Image('images/touchid.png', (120, 220), app=(self.screen)).draw()
                        elements.Title(self.title, pos=(280, 67), app=(self.screen)).draw()
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