""" Product request (Add))"""
import pygame
from pygame.locals import *
import time
import os
import config 
import elements
import views
import services

class product_list():
    section = ""
    qrcode = ""
    item_number = ""
    product_name = ""
    part_number = ""
    part_name = ""
    drawing_number = ""
    locker_number = ""
    quantity = ""
    other = ""
class Request_Check:
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
        self.product_data = views.request_data.request_list2
        self.data = ''
        if config.locker_type == 0:
            self.check = [False, False, False, False, False, False, False, False, False, False, False, False]
        else:
            self.check = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
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
            (8, 3): 'self.check_click()',
            (9, 3): 'self.check_click()',
            (10, 3): 'self.check_click()',
            # Click confirm button
            (8, 8): 'self.confirm_click()',
            (9, 8): 'self.confirm_click()',
            (10, 8): 'self.confirm_click()',
            (8, 9): 'self.confirm_click()',
            (9, 9): 'self.confirm_click()',
            (10, 9): 'self.confirm_click()',
            (8, 10): 'self.confirm_click()',
            (9, 10): 'self.confirm_click()',
            (10, 10): 'self.confirm_click()',
            # Click previous button
            (1, 10): 'self.previousbutton_click()',
            (2, 10): 'self.previousbutton_click()',
            # Click next button
            (6, 10): 'self.nextbutton_click()',
            (7, 10): 'self.nextbutton_click()',
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
    
    def active_button(self):
        """Check activation next button."""
        if len(self.product_data) - (self.index * 6) > 6 :
            self.next_button = True
        else:
            self.next_button = False
        """Check activation previous button."""
        if self.index > 0:
            self.previous_button = True
        else:
            self.previous_button = False

    def nextbutton_click(self):
        if self.next_button:
            self.index += 1

    def previousbutton_click(self):
        if self.previous_button:
            self.index -= 1

    def confirm_click(self):
        views.request_data.list_check_reset()
        views.request_data.list_reset()
        views.request_data.reset()
        views.request_data.requester_reset()
        views.Request().run()
        pygame.quit()

    def check_click(self):
        for x in range(len(views.request_data.request_list2)):
            if views.request_data.request_list2[x].qrcode == self.search_value.replace("\r", ""):
                views.request_data.request_list2_check[x] = True
                self.search_input.update('*')

    def run(self):
        """Initialize Caption and Valiable."""
        pygame.display.set_caption('Requestion check' + config.VERSION)
        self.search_input = elements.InputBox_Request_Check(1, 3, 7, 1, "", app = (self.screen), active = True, numpad_active = True)
        print(views.request_data.request_list2_check)
        """Run the main event loop."""
        while self.running:
            self.number = 1
            self.screen.fill(Color('white'))
            self.requestcheck_listview = elements.Request_Check_Listview(1, 5, 7, 5, check = views.request_data.request_list2_check, app = (self.screen),data = self.product_data, index = self.index)
            self.active_button()
            """Initialize user interface."""
            for row in range(12):
                y = (config.margin + config.bheight) * row + config.margin
                row_click = row
                for column in range(12):
                    x = (config.margin + config.bwidth) * column + config.margin
                    column_click = column
                    position = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position2 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1), (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) - 30, (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 15, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 60)
                    if row == 0 and column == 0:
                        elements.Title('REQUESTION CHECK', pos=(280, 67), app=(self.screen)).draw()
                        elements.Header_Table('No.', 1, 4, app=(self.screen)).draw()
                        elements.Header_Table('Product name', 2, 4, app=(self.screen)).draw()
                        elements.Header_Table('QTY.', 5, 4, app=(self.screen)).draw()
                        elements.Header_Table('Locker', 6, 4, app=(self.screen)).draw()
                        self.search_input.draw()
                        self.requestcheck_listview.draw()                     
                    if row == 3 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 214, config.bheight).Rect()
                        elements.Text_Button_Medium('      CHECK', position, app=(self.screen)).draw()
                    """Initialize Numpad."""
                    if row >= 4 and row <= 7 and column >= 8 and column <= 10:
                        if row == 7 and column == 8:
                            elements.Button(self.screen, config.light_blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number('*', position, app=(self.screen)).draw()
                        elif row == 7 and column == 9:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number(str(0), position, app=(self.screen)).draw()
                        elif row == 7 and column == 10:
                            elements.Button(self.screen, config.light_blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number('#', position, app=(self.screen)).draw()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth, config.bheight).Rect()
                            elements.Number(str(self.number), position, app=(self.screen)).draw()
                        self.number += 1
                    if row == 8 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 214, config.bheight + 134).Rect()  
                        elements.Text_Button_Medium('  CONFIRM', position4, app=(self.screen)).draw()
                    
                    if row == 10 and column == 1:
                        if self.previous_button:
                            elements.Button(self.screen, config.dark_gray, x, y, config.bwidth + 107, config.bheight).Rect()
                        else:
                            elements.Button(self.screen, config.gray, x, y, config.bwidth + 107, config.bheight).Rect()
                        elements.Text_Button_Medium(' PREVIOUS', position3, app=(self.screen)).draw() 
                    if row == 10 and column == 6:
                        if self.next_button:
                            elements.Button(self.screen, config.dark_gray, x, y, config.bwidth + 107, config.bheight).Rect()
                        else:
                            elements.Button(self.screen, config.gray, x, y, config.bwidth + 107, config.bheight).Rect()
                        elements.Text_Button_Medium('  NEXT', position2, app=(self.screen)).draw()                

            for event in pygame.event.get():
                self.search_value = self.search_input.handle_event(event)
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.check_click()
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