""" Search"""
import pygame
from pygame.locals import *
import time
import os
import config 
import elements
import views
import data_example



class Product_Section:
    """Create a single-window app with multiple scenes."""

    def __init__(self, editstage):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        self.editstage = editstage

        self.section_button = [False, False, False, False, False]
        self.section_value = [False, False, False, False, False]
        self.first_check()

        if self.editstage:
            self.caption = 'Edit product section'
            self.title = 'EDIT PRODUCT SECTION'
        else:
            self.caption = 'Add product section'
            self.title = 'ADD PRODUCT SECTION'

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
            (1, 3): 'self.toggle_button(1)',
            (2, 3): 'self.toggle_button(1)',
            (3, 3): 'self.toggle_button(1)',
            (4, 3): 'self.toggle_button(1)',
            (5, 3): 'self.toggle_button(1)',
            (1, 4): 'self.toggle_button(1)',
            (2, 4): 'self.toggle_button(1)',
            (3, 4): 'self.toggle_button(1)',
            (4, 4): 'self.toggle_button(1)',
            (5, 4): 'self.toggle_button(1)',
            # Click AS2 button
            (6, 3): 'self.toggle_button(2)',
            (7, 3): 'self.toggle_button(2)',
            (8, 3): 'self.toggle_button(2)',
            (9, 3): 'self.toggle_button(2)',
            (10, 3): 'self.toggle_button(2)',
            (6, 4): 'self.toggle_button(2)',
            (7, 4): 'self.toggle_button(2)',
            (8, 4): 'self.toggle_button(2)',
            (9, 4): 'self.toggle_button(2)',
            (10, 4): 'self.toggle_button(2)',
            # Click MT1 button
            (1, 5): 'self.toggle_button(3)',
            (2, 5): 'self.toggle_button(3)',
            (3, 5): 'self.toggle_button(3)',
            (4, 5): 'self.toggle_button(3)',
            (5, 5): 'self.toggle_button(3)',
            (1, 6): 'self.toggle_button(3)',
            (2, 6): 'self.toggle_button(3)',
            (3, 6): 'self.toggle_button(3)',
            (4, 6): 'self.toggle_button(3)',
            (5, 6): 'self.toggle_button(3)',
            # Click MT2 button
            (6, 5): 'self.toggle_button(4)',
            (7, 5): 'self.toggle_button(4)',
            (8, 5): 'self.toggle_button(4)',
            (9, 5): 'self.toggle_button(4)',
            (10, 5): 'self.toggle_button(4)',
            (6, 6): 'self.toggle_button(4)',
            (7, 6): 'self.toggle_button(4)',
            (8, 6): 'self.toggle_button(4)',
            (9, 6): 'self.toggle_button(4)',
            (10, 6): 'self.toggle_button(4)',
            # Click PR button
            (4, 7): 'self.toggle_button(5)',
            (5, 7): 'self.toggle_button(5)',
            (6, 7): 'self.toggle_button(5)',
            (7, 7): 'self.toggle_button(5)',
            (8, 7): 'self.toggle_button(5)',
            (4, 8): 'self.toggle_button(5)',
            (5, 8): 'self.toggle_button(5)',
            (6, 8): 'self.toggle_button(5)',
            (7, 8): 'self.toggle_button(5)',
            (8, 8): 'self.toggle_button(5)',
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

    def first_check(self):
        for x in range(len(self.section_button)):
            if views.product_data.product_data['section'][x]:
                self.section_button[x] = True
            else:
                 self.section_button[x] = False
 
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
        if self.section_button[0]:
            self.section_value[0] = 'AS1'
        if self.section_button[1]:
            self.section_value[1] = 'AS2'
        if self.section_button[2]:
            self.section_value[2] = 'MT1'
        if self.section_button[3]:
            self.section_value[3] = 'MT2'
        if self.section_button[4]:
            self.section_value[4] = 'PR'

        if self.section_value != '':
            views.product_data.product_data['section'] = self.section_value
            views.Product_Qrcode(False).run()
            pygame.quit()
        else:
            print("Please select product section")

    def cancel_click(self):
        views.product_data.product_data['section'] = ''
        views.Product_Management().run()
        pygame.quit()

    def toggle_button(self, event):
        if self.section_button[event - 1]:
            self.section_button[event - 1] = False
        else:
            self.section_button[event - 1] = True

    def run(self):
        """Initialize Caption and Valiable."""
        pygame.display.set_caption(self.caption + config.VERSION)
        print("Product_Data :", views.product_data.product_data)
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
                        elements.Title(self.title, pos=(240, 67), app=(self.screen)).draw()  
                    """Initialize Button."""
                    if row == 3 and column == 1:
                        if self.section_button[0]:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   AS1', position3, app=(self.screen)).draw()
                    if row == 3 and column == 6:
                        if self.section_button[1]:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   AS2', position3, app=(self.screen)).draw()
                    if row == 5 and column == 1:
                        if self.section_button[2]:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   MT1', position3, app=(self.screen)).draw()
                    if row == 5 and column == 6:
                        if self.section_button[3]:
                            elements.Button(self.screen, config.green, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.blue, x, y, config.bwidth + 428, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('   MT2', position3, app=(self.screen)).draw()
                    if row == 7 and column == 4:
                        if self.section_button[4]:
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