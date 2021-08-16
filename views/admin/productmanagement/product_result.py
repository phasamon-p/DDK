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



class Product_Result:
    """Create a single-window app with multiple scenes."""

    def __init__(self, editstage):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        self.next_button = True # Set default avtivation status of next button
        self.previous_button = False # Set default avtivation status of previous button
        self.index = 0 # Set default index value of listview page
        self.editstage = editstage
        if self.editstage:
            self.caption = 'Update product information'
            self.title = 'Update PRODUCT INFORMATION'
        else:
            self.caption = 'Confirm product information'
            self.title = 'CONFIRM PRODUCT INFORMATION'

        self.shortcuts = {
            (K_x, KMOD_LMETA): 'print("cmd+X")',
            (K_x, KMOD_LALT): 'print("alt+X")',
            (K_x, KMOD_LCTRL): 'home.App().run()',
            (K_x, KMOD_LMETA + KMOD_LSHIFT): 'print("cmd+shift+X")',
            (K_x, KMOD_LMETA + KMOD_LALT): 'print("cmd+alt+X")',
            (K_x, KMOD_LMETA + KMOD_LALT + KMOD_LSHIFT): 'print("cmd+alt+shift+X")',
        }

        self.click = {
            # Click previous button
            (8, 4): 'self.previousbutton_click()',
            (9, 4): 'self.previousbutton_click()',
            (10, 4): 'self.previousbutton_click()',
            (8, 5): 'self.previousbutton_click()',
            (9, 5): 'self.previousbutton_click()',
            (10, 5): 'self.previousbutton_click()',
            # Click next button
            (8, 6): 'self.nextbutton_click()',
            (9, 6): 'self.nextbutton_click()',
            (10, 6): 'self.nextbutton_click()',
            (8, 7): 'self.nextbutton_click()',
            (9, 7): 'self.nextbutton_click()',
            (10, 7): 'self.nextbutton_click()',
            # Click confirm button
            (8, 8): 'self.confirm_click()',
            (9, 8): 'self.confirm_click()',
            (10, 8): 'self.confirm_click()',
            (8, 9): 'self.confirm_click()',
            (9, 9): 'self.confirm_click()',
            (10, 9): 'self.confirm_click()',
            # Click back button
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

    def nextbutton_click(self):
        if self.next_button:
            self.next_button = False
            self.previous_button = True
            self.index = 1
        else:
            self.next_button = False

    def previousbutton_click(self):
        if self.previous_button:
            self.next_button = True
            self.previous_button = False
            self.index = 0
        else:
            self.previous_button = False

    def confirm_click(self):
        if self.editstage:
            self.set_data()
            services.updateproductbyid(views.product_data.old_qrcode, self.product_data)
            services.insertproductlocker(self.product_data[1], self.product_data[7], self.product_data[10], self.product_data[11]) #insert product locker
            views.product_data.productdata_reset()
            views.product_data.list_reset()
            views.Product_Management().run()
            pygame.quit() 
        else:
            self.set_data()
            services.insertproduct(self.product_data) # Insert nmew product
            services.insertproductlocker(self.product_data[1], self.product_data[7], self.product_data[10], self.product_data[11]) #insert product locker
            views.product_data.productdata_reset()
            views.product_data.list_reset()
            views.Product_Management().run()
            pygame.quit()

    def back_click(self):
        if self.editstage:
            views.Other(True).run()
            pygame.quit() 
        else:
            views.Other(False).run()
            pygame.quit()

    def set_data(self):
        self.product_data = []
        self.product_data.append(views.product_data.section())
        self.product_data.append(views.product_data.product_data['qrcode'])
        self.product_data.append(views.product_data.product_data['item_number'])
        self.product_data.append(views.product_data.product_data['product_name'])
        self.product_data.append(views.product_data.product_data['part_number'])
        self.product_data.append(views.product_data.product_data['part_name'])
        self.product_data.append(views.product_data.product_data['drawing_number'])
        self.product_data.append(views.product_data.product_data['locker_number'])
        self.product_data.append(views.product_data.product_data['quantity'])
        self.product_data.append(views.product_data.product_data['other'])
        self.product_data.append(views.product_data.product_data['drawer'])
        self.product_data.append(views.product_data.product_data['cavity'])
        return self.product_data 

    def string_locker(self, lockernumber):
        if config.locker_type > 0:
            if int(lockernumber) == 1:
                return "A"
            if int(lockernumber) == 2:
                return "B"
            if int(lockernumber) == 3:
                return "C"
            if int(lockernumber) == 4:
                return "D"
            if int(lockernumber) == 5:
                return "E"
            if int(lockernumber) == 6:
                return "F"
            if int(lockernumber) == 7:
                return "G"
            if int(lockernumber) == 8:
                return "H"
            if int(lockernumber) == 9:
                return "I"
            if int(lockernumber) == 10:
                return "J"
            if int(lockernumber) == 11:
                return "K"
            if int(lockernumber) == 12:
                return "L"
            if int(lockernumber) == 13:
                return "M"
            if int(lockernumber) == 14:
                return "N"
            if int(lockernumber) == 15:
                return "O"
            if int(lockernumber) == 16:
                return "P"
        else:
            if int(lockernumber) == 1:
                return "A"
            if int(lockernumber) == 2:
                return "B"
            if int(lockernumber) == 3:
                return "C"
            if int(lockernumber) == 4:
                return "D"
            if int(lockernumber) == 5:
                return "E"
            if int(lockernumber) == 6:
                return "F"
            if int(lockernumber) == 7:
                return "G"
            if int(lockernumber) == 8:
                return "H"
            if int(lockernumber) == 9:
                return "I"
            if int(lockernumber) == 10:
                return "J"
            if int(lockernumber) == 11:
                return "K"
            if int(lockernumber) == 12:
                return "L"

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
                    position3 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 10, (config.margin + config.bheight) * row + (config.bheight / 3.5) + 30)
                    position4 = ((config.margin + config.bwidth) * column + (config.bwidth / 2.1) + 10, (config.margin + config.bheight) * row + (config.bheight / 3.5) - 5)
                    if row == 0 and column == 0:
                        elements.Title(self.title, pos=(30, 67), app=(self.screen)).draw()
                        elements.Header_Table('PRODUCT INFORMATION', 1, 3, app=(self.screen)).draw()
                        elements.Rectangle(1, 4, 7, 7, app=(self.screen)).draw()
                        if self.index == 0:
                            elements.Header_Result('  Product section : ', 1, 4, app=(self.screen)).draw()
                            elements.Header_Result('  Product qrcode : ', 1, 5, app=(self.screen)).draw()
                            elements.Header_Result('  Item number : ', 1, 6, app=(self.screen)).draw()
                            elements.Header_Result('  Product name : ', 1, 7, app=(self.screen)).draw()
                            elements.Header_Result('  Part number : ', 1, 8, app=(self.screen)).draw()
                            elements.Header_Result('  Part name  : ', 1, 9, app=(self.screen)).draw()
                            elements.Header_Result('  Drawing number: ', 1, 10, app=(self.screen)).draw()
                            # User information
                            elements.Header_Table(views.product_data.section(), 4, 4, app=(self.screen)).draw()
                            elements.Header_Table(views.product_data.product_data['qrcode'], 4, 5, app=(self.screen)).draw()
                            elements.Header_Table(views.product_data.product_data['item_number'], 4, 6, app=(self.screen)).draw()
                            elements.Header_Table(views.product_data.product_data['product_name'], 4, 7, app=(self.screen)).draw()
                            elements.Header_Table(views.product_data.product_data['part_number'], 4, 8, app=(self.screen)).draw()
                            elements.Header_Table(views.product_data.product_data['part_name'], 4, 9, app=(self.screen)).draw()
                            elements.Header_Table(views.product_data.product_data['drawing_number'], 4, 10, app=(self.screen)).draw()
                        else:
                            elements.Header_Result('  Product locker : ', 1, 4, app=(self.screen)).draw()
                            elements.Header_Result('  Product drawer : ', 1, 5, app=(self.screen)).draw()
                            elements.Header_Result('  Product cavity : ', 1, 6, app=(self.screen)).draw()
                            elements.Header_Result('  Product quantity : ', 1, 7, app=(self.screen)).draw()
                            elements.Header_Result('  Product other : ', 1, 8, app=(self.screen)).draw()
                            # User information
                            elements.Header_Table(views.product_data.lengh_lockeraccess(), 4, 4, app=(self.screen)).draw()
                            elements.Header_Table(views.product_data.product_data['drawer'], 4, 5, app=(self.screen)).draw()
                            elements.Header_Table(views.product_data.product_data['cavity'], 4, 6, app=(self.screen)).draw()
                            elements.Header_Table(views.product_data.product_data['quantity'], 4, 7, app=(self.screen)).draw()
                            elements.Header_Table(views.product_data.product_data['other'], 4, 8, app=(self.screen)).draw()
                    """Initialize Button."""
                    if row == 4 and column == 8:
                        if self.previous_button:
                            elements.Button(self.screen, config.dark_gray, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.gray, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('  PREVIOUS', position3, app=(self.screen)).draw()
                    if row == 6 and column == 8:
                        if self.next_button:
                            elements.Button(self.screen, config.dark_gray, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        else:
                            elements.Button(self.screen, config.gray, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('     NEXT', position3, app=(self.screen)).draw()
                    if row == 8 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('  CONFIRM', position3, app=(self.screen)).draw()
                    if row == 10 and column == 8:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 214, config.bheight).Rect()
                        elements.Text_Button_Medium('      BACK', position4, app=(self.screen)).draw()
                   
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