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
    drawer = ""
    cavity = ""

class product_edit():
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
    drawer = ""
    cavity = ""

class Product_Edit:
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
        self.product_data = views.product_data.request_list
        self.product_list = product_list()
        self.product_edit = product_edit()

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
            (8, 4): 'self.search_click()',
            (9, 4): 'self.search_click()',
            (10, 4): 'self.search_click()',
            # Click delete button
            (8, 5): 'self.delete_click()',
            (9, 5): 'self.delete_click()',
            (10, 5): 'self.delete_click()',
            # Click cancel button
            (8, 10): 'self.cancel_click()',
            (9, 10): 'self.cancel_click()',
            (10, 10): 'self.cancel_click()',
            # Click edit information button
            (1, 9): 'self.editinformation_click()',
            (2, 9): 'self.editinformation_click()',
            (3, 9): 'self.editinformation_click()',
            (1, 10): 'self.editinformation_click()',
            (2, 10): 'self.editinformation_click()',
            (3, 10): 'self.editinformation_click()',
            # Click next button
            (5, 9): 'self.editinventory_click()',
            (6, 9): 'self.editinventory_click()',
            (7, 9): 'self.editinventory_click()',
            (5, 10): 'self.editinventory_click()',
            (6, 10): 'self.editinventory_click()',
            (7, 10): 'self.editinventory_click()',
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
        self.data = services.selectproductbysearch(self.search_value.replace("\r", ""))
        print("data", self.data)
        if self.data[0]:
            self.drawers = services.getproduct_drawer(self.data[1][0][0][2])
            self.product_list.section = self.data[1][0][0][1]
            self.product_list.qrcode = self.data[1][0][0][2]
            self.product_list.item_number = self.data[1][0][0][3]
            self.product_list.product_name = self.data[1][0][0][4]
            self.product_list.part_number = self.data[1][0][0][5]
            self.product_list.part_name = self.data[1][0][0][6]
            self.product_list.drawing_number = self.data[1][0][0][7]
            self.product_list.locker_number = services.getproductlocker_string(self.data[1][0][0][2])
            self.product_list.quantity = str(self.data[1][0][0][9])
            self.product_list.other = self.data[1][0][0][10]
            self.product_list.drawer = self.drawers[3] 
            self.product_list.cavity = self.drawers[4] 
            views.product_data.list_reset()
            views.product_data.list_add(self.product_list)
            views.product_data.old_qrcode = self.data[1][0][0][2]
        else:
            self.search_input.update("*")
            views.product_data.productdata_reset()
            views.product_data.list_reset()
            print("don't have product")

    def delete_click(self):
        print("delete")
        if len(views.product_data.request_list) > 0:
            services.deleteproductbyid(self.data[1][0][0][0])
            services.deleteproductlockerbybarcode(self.data[1][0][0][2])
            self.search_value = ''
            self.search_input.update("*")
            views.product_data.productdata_reset()
            views.product_data.list_reset()
        else:
            print("Please searching product")

    def cancel_click(self):
        views.product_data.productdata_reset()
        views.product_data.list_reset()
        views.Product_Management().run() 
        pygame.quit()

    def editinformation_click(self):
        if len(views.product_data.request_list) > 0:
            self.setdata()
            views.Product_Section(True).run() 
            pygame.quit()
        else:
            print("Please searching product")

    def editinventory_click(self):
        if len(views.product_data.request_list) > 0:
            self.setdata()
            views.Inventory_Edit(True).run() 
            pygame.quit()
        else:
            print("Please searching product")
    
    def setdata(self):
        if self.data[0]:
            self.drawers = services.getproduct_drawer(self.data[1][0][0][2])
            self.product_edit.section = services.getsection_bool(self.data[1][0][0][2])
            self.product_edit.qrcode = self.data[1][0][0][2]
            self.product_edit.item_number = self.data[1][0][0][3]
            self.product_edit.product_name = self.data[1][0][0][4]
            self.product_edit.part_number = self.data[1][0][0][5]
            self.product_edit.part_name = self.data[1][0][0][6]
            self.product_edit.drawing_number = self.data[1][0][0][7]
            self.product_edit.locker_number = services.getproductlocker_byqrcode_bool(self.data[1][0][0][2])
            self.product_edit.quantity = str(self.data[1][0][0][9])
            self.product_edit.other = self.data[1][0][0][10]
            self.product_edit.drawer = self.drawers[3] 
            self.product_edit.cavity = self.drawers[4] 
        views.product_data.productdata_setedit(self.product_edit)

    def run(self):
        """Initialize Caption and Valiable."""
        pygame.display.set_caption('Product search' + config.VERSION)
        self.search_input = elements.Product_Search(1, 3, 7, 1, app = (self.screen), active = True, numpad_active = True)
        """Run the main event loop."""
        while self.running:
            self.number = 1
            self.screen.fill(Color('white'))
            self.product_listview = elements.Productedit_Listview(1, 5, 7, 4, app=(self.screen),data = self.product_data, index = self.index)
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
                        elements.Header_Table('No.', 1, 4, app=(self.screen)).draw()
                        elements.Header_Table('Product name', 2, 4, app=(self.screen)).draw()
                        elements.Header_Table('QTY.', 5, 4, app=(self.screen)).draw()
                        elements.Header_Table('Locker', 6, 4, app=(self.screen)).draw()
                        # elements.Rectangle(1, 5, 7, 5, app=(self.screen)).draw()
                        self.search_input.draw() 
                        self.product_listview.draw()                     
                    if row == 3 and column == 8:
                        elements.Button(self.screen, config.green, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('      SEARCH', position5, app=(self.screen)).draw()
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
                    if row == 9 and column == 1:
                        elements.Button(self.screen, config.blue, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('       EDIT', position2, app=(self.screen)).draw()
                        elements.Text_Button_Medium('INFORMATION', position3, app=(self.screen)).draw()    
                    if row == 9 and column == 5:
                        elements.Button(self.screen, config.blue_arm, x, y, config.bwidth + 214, config.bheight + 67).Rect()
                        elements.Text_Button_Medium('        EDIT', position2, app=(self.screen)).draw()
                        elements.Text_Button_Medium('   INVENTORY', position3, app=(self.screen)).draw()
                    if row == 10 and column == 8:
                        elements.Button(self.screen, config.red, x, y, config.bwidth + 214, config.bheight).Rect()
                        elements.Text_Button_Medium('     BACK', position4, app=(self.screen)).draw()
                                

            for event in pygame.event.get():
                self.search_value = self.search_input.handle_event(event)
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.search_click()
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