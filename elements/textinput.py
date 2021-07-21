from types import prepare_class
import pygame
from pygame.locals import *
import config 
import elements
import views

active1 = False
active2 = False
class InputBox:

    def __init__(self, start_row, start_column, w_column, h_row, app, active = bool, numpad_active = bool):
        self.fontname = 'fonts/SEGOEUIB.TTF'
        self.fontsize = 32
        self.border = 3
        self.set_font()
        self.app = app
        self.start_row = start_row
        self.start_column = start_column
        self.w_column = w_column  
        self.h_row = h_row
        self.set_size()
        self.color = config.COLOR_INACTIVE
        self.text = ""
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = active
        self.numpad_active = numpad_active
        
        self.numpad = {
            # Click numpad button
            (8, 5): 'self.update("1")',
            (9, 5): 'self.update("2")',
            (10, 5): 'self.update("3")',
            (8, 6): 'self.update("4")',
            (9, 6): 'self.update("5")',
            (10, 6): 'self.update("6")',
            (8, 7): 'self.update("7")',
            (9, 7): 'self.update("8")',
            (10, 7): 'self.update("9")',
            (8, 8): 'self.update("*")',
            (9, 8): 'self.update("0")',
            (10, 8): 'self.update("#")',
        }

    def set_size(self):
        if self.h_row > 1:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + ((self.w_column -1 ) * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
            else: 
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - (self.border * 2), ((self.h_row * config.bheight) - self.border))
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))
    
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize) 
    
    def numpad_click(self, x, y):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = x // (config.bwidth + config.margin)
        row_click = y // (config.bheight + config.margin)
        if (column_click, row_click) in self.numpad:
            exec(self.numpad[column_click, row_click])

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN or event.type == FINGERDOWN:
            if self.numpad_active & self.active:
                if event.type == FINGERDOWN:
                    x = event.x * config.width
                    y = event.y * config.height
                    self.numpad_click(x, y)
                else:
                    x, y = event.pos
                    self.pos_mouse = x, y = event.pos
                    self.numpad_click(x, y)
        if event.type == pygame.KEYDOWN:
            if self.active:
                # if event.key == pygame.K_RETURN:
                #     print(self.text)
                #     self.text = ''
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode                  
                self.text_render()
        return self.text

    def update(self, data):
        # Resize the box if the text is too long.
        if data == '*':
            print(self.text)
            self.text = ''
            self.text_render()
        elif data == '#':
            self.text = self.text[:-1]
            self.text_render()
        else:
            self.text += data
            self.text_render()
        return self.text

    def text_render(self):
        # Re-render the text.
            if len(self.text) > 40:
                self.txt_surface = self.font.render(self.text[len(self.text) - 40:], True, self.color)
            else:
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.color = config.COLOR_ACTIVE if self.active else config.COLOR_INACTIVE
        # Blit the text.
        self.app.blit(self.txt_surface, (self.rect.x+20, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)


class Product_Search:
    def __init__(self, start_row, start_column, w_column, h_row, app, active = bool, numpad_active = bool):
        self.fontname = 'fonts/SEGOEUIB.TTF'
        self.fontsize = 32
        self.border = 3
        self.set_font()
        self.app = app
        self.start_row = start_row
        self.start_column = start_column
        self.w_column = w_column  
        self.h_row = h_row
        self.set_size()
        self.color = config.COLOR_INACTIVE
        self.text = ""
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = active
        self.numpad_active = numpad_active
        
        self.numpad = {
            # Click numpad button
            (8, 6): 'self.update("1")',
            (9, 6): 'self.update("2")',
            (10, 6): 'self.update("3")',
            (8, 7): 'self.update("4")',
            (9, 7): 'self.update("5")',
            (10, 7): 'self.update("6")',
            (8, 8): 'self.update("7")',
            (9, 8): 'self.update("8")',
            (10, 8): 'self.update("9")',
            (8, 9): 'self.update("*")',
            (9, 9): 'self.update("0")',
            (10, 9): 'self.update("#")',
        }

    def set_size(self):
        if self.h_row > 1:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + ((self.w_column -1 ) * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
            else: 
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - (self.border * 2), ((self.h_row * config.bheight) - self.border))
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))
    
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize) 
    
    def numpad_click(self, x, y):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = x // (config.bwidth + config.margin)
        row_click = y // (config.bheight + config.margin)
        if (column_click, row_click) in self.numpad:
            exec(self.numpad[column_click, row_click])

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN or event.type == FINGERDOWN:
            if self.numpad_active & self.active:
                if event.type == FINGERDOWN:
                    x = event.x * config.width
                    y = event.y * config.height
                    self.numpad_click(x, y)
                else:
                    x, y = event.pos
                    self.pos_mouse = x, y = event.pos
                    self.numpad_click(x, y)
        if event.type == pygame.KEYDOWN:
            if self.active:
                # if event.key == pygame.K_RETURN:
                #     print(self.text)
                #     self.text = ''
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode                  
                self.text_render()
        return self.text

    def update(self, data):
        # Resize the box if the text is too long.
        if data == '*':
            print(self.text)
            self.text = ''
            self.text_render()
        elif data == '#':
            self.text = self.text[:-1]
            self.text_render()
        else:
            self.text += data
            self.text_render()
        return self.text

    def text_render(self):
        # Re-render the text.
            if len(self.text) > 40:
                self.txt_surface = self.font.render(self.text[len(self.text) - 40:], True, self.color)
            else:
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.color = config.COLOR_ACTIVE if self.active else config.COLOR_INACTIVE
        # Blit the text.
        self.app.blit(self.txt_surface, (self.rect.x+20, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)


class User_Search:
    def __init__(self, start_row, start_column, w_column, h_row, app, active = bool, numpad_active = bool):
        self.fontname = 'fonts/SEGOEUIB.TTF'
        self.fontsize = 32
        self.border = 3
        self.set_font()
        self.app = app
        self.start_row = start_row
        self.start_column = start_column
        self.w_column = w_column  
        self.h_row = h_row
        self.set_size()
        self.color = config.COLOR_INACTIVE
        self.text = ""
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = active
        self.numpad_active = numpad_active
        
        self.numpad = {
            # Click numpad button
            (8, 6): 'self.update("1")',
            (9, 6): 'self.update("2")',
            (10, 6): 'self.update("3")',
            (8, 7): 'self.update("4")',
            (9, 7): 'self.update("5")',
            (10, 7): 'self.update("6")',
            (8, 8): 'self.update("7")',
            (9, 8): 'self.update("8")',
            (10, 8): 'self.update("9")',
            (8, 9): 'self.update("*")',
            (9, 9): 'self.update("0")',
            (10, 9): 'self.update("#")',
        }

    def set_size(self):
        if self.h_row > 1:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + ((self.w_column -1 ) * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
            else: 
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - (self.border * 2), ((self.h_row * config.bheight) - self.border))
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))
    
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize) 
    
    def numpad_click(self, x, y):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = x // (config.bwidth + config.margin)
        row_click = y // (config.bheight + config.margin)
        if (column_click, row_click) in self.numpad:
            exec(self.numpad[column_click, row_click])

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN or event.type == FINGERDOWN:
            if self.numpad_active & self.active:
                if event.type == FINGERDOWN:
                    x = event.x * config.width
                    y = event.y * config.height
                    self.numpad_click(x, y)
                else:
                    x, y = event.pos
                    self.pos_mouse = x, y = event.pos
                    self.numpad_click(x, y)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode                  
                self.text_render()
        return self.text

    def update(self, data):
        # Resize the box if the text is too long.
        if data == '*':
            print(self.text)
            self.text = ''
            self.text_render()
        elif data == '#':
            self.text = self.text[:-1]
            self.text_render()
        else:
            self.text += data
            self.text_render()
        return self.text

    def text_render(self):
        # Re-render the text.
            if len(self.text) > 40:
                self.txt_surface = self.font.render(self.text[len(self.text) - 40:], True, self.color)
            else:
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.color = config.COLOR_ACTIVE if self.active else config.COLOR_INACTIVE
        # Blit the text.
        self.app.blit(self.txt_surface, (self.rect.x+20, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)

class InputBox_2:
    """This input box for using two element in same page"""
    def __init__(self, start_row, start_column, w_column, h_row , app, active = bool, numpad_active = bool):
        self.fontname = 'fonts/SEGOEUIB.TTF'
        self.fontsize = 32
        self.border = 3
        self.set_font()
        self.app = app
        self.start_row = start_row
        self.start_column = start_column
        self.w_column = w_column  
        self.h_row = h_row
        self.set_size()
        self.color = config.COLOR_INACTIVE
        self.text = ""
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = active
        self.numpad_active = numpad_active
        
        self.numpad = {
            # Click numpad button
            (8, 4): 'self.update("1")',
            (9, 4): 'self.update("2")',
            (10, 4): 'self.update("3")',
            (8, 5): 'self.update("4")',
            (9, 5): 'self.update("5")',
            (10, 5): 'self.update("6")',
            (8, 6): 'self.update("7")',
            (9, 6): 'self.update("8")',
            (10, 6): 'self.update("9")',
            (8, 7): 'self.update("*")',
            (9, 7): 'self.update("0")',
            (10, 7): 'self.update("#")'
        }

        self.num_press = {
            # Click numpad button
            ("1"): 'self.update("1")',
            ("2"): 'self.update("2")',
            ("3"): 'self.update("3")',
            ("4"): 'self.update("4")',
            ("5"): 'self.update("5")',
            ("6"): 'self.update("6")',
            ("7"): 'self.update("7")',
            ("8"): 'self.update("8")',
            ("9"): 'self.update("9")',
            ("0"): 'self.update("0")',
        }

    def set_size(self):
        if self.h_row > 1:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + ((self.w_column -1 ) * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
            else: 
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - (self.border * 2), ((self.h_row * config.bheight) - self.border))
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))
    
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def numpad_click(self, x, y):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = x // (config.bwidth + config.margin)
        row_click = y // (config.bheight + config.margin)
        if (column_click, row_click) in self.numpad:
            exec(self.numpad[column_click, row_click])

    def numpad_press(self, event):
        """Find the mouse position in the gird and execute the event."""
        if (event.unicode) in self.num_press:
            exec(self.num_press[event.unicode])
    
    def handle_event(self, event, index):
        if event.type == MOUSEBUTTONDOWN or event.type == FINGERDOWN:
            if self.numpad_active & self.active:
                if event.type == FINGERDOWN:
                    x = event.x * config.width
                    y = event.y * config.height
                    self.numpad_click(x, y)
                else:
                    x, y = event.pos
                    self.pos_mouse = x, y = event.pos
                    self.numpad_click(x, y)
            # If the user clicked on the input_box rect.
            if event.type == FINGERDOWN:
                if self.rect.collidepoint(event.x * config.width,event.y * config.height):
                    if index == 1:
                    # Toggle the active variable.
                        views.request_data.inbox_active[0] = True
                        views.request_data.inbox_active[1] = False
                    if index == 2:
                        views.request_data.inbox_active[1] = True
                        views.request_data.inbox_active[0] = False
            elif event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    if index == 1:
                    # Toggle the active variable.
                        views.request_data.inbox_active[0] = True
                        views.request_data.inbox_active[1] = False
                    if index == 2:
                        views.request_data.inbox_active[1] = True
                        views.request_data.inbox_active[0] = False
            else:
                pass
                # self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if index == 2:
                        self.numpad_press(event)
                    else:
                        self.text += event.unicode                  
                # Re-render the text.
                self.text_render()
        return self.text

    def update(self, data):
        # Resize the box if the text is too long.
        if data == '*':
            print(self.text)
            self.text = ''
            self.text_render()
        elif data == '#':
            self.text = self.text[:-1]
            self.text_render()
        else:
            self.text += data
            self.text_render()
        return self.text

    def text_render(self):
        # Re-render the text.
            if len(self.text) > 40:
                self.txt_surface = self.font.render(self.text[len(self.text) - 40:], True, self.color)
            else:
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.color = config.COLOR_ACTIVE if self.active else config.COLOR_INACTIVE
        # Blit the text.
        self.app.blit(self.txt_surface, (self.rect.x+20, self.rect.y+5))
        # print(111)
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)

class InputBox_Number: 
    """This input box is require number only user"""
    def __init__(self, start_row, start_column, w_column, h_row, text, app, active = bool, numpad_active = bool):
        self.fontname = 'fonts/SEGOEUIB.TTF'
        self.fontsize = 32
        self.border = 3
        self.set_font()
        self.app = app
        self.start_row = start_row
        self.start_column = start_column
        self.w_column = w_column  
        self.h_row = h_row
        self.set_size()
        self.color = config.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = active
        self.numpad_active = numpad_active
        
        self.numpad = {
            # Click numpad button
            (8, 4): 'self.update("1")',
            (9, 4): 'self.update("2")',
            (10, 4): 'self.update("3")',
            (8, 5): 'self.update("4")',
            (9, 5): 'self.update("5")',
            (10, 5): 'self.update("6")',
            (8, 6): 'self.update("7")',
            (9, 6): 'self.update("8")',
            (10, 6): 'self.update("9")',
            (8, 7): 'self.update("*")',
            (9, 7): 'self.update("0")',
            (10, 7): 'self.update("#")',
        }

        self.num_press = {
            # Click numpad button
            ("1"): 'self.update("1")',
            ("2"): 'self.update("2")',
            ("3"): 'self.update("3")',
            ("4"): 'self.update("4")',
            ("5"): 'self.update("5")',
            ("6"): 'self.update("6")',
            ("7"): 'self.update("7")',
            ("8"): 'self.update("8")',
            ("9"): 'self.update("9")',
            ("0"): 'self.update("0")',
        }

    def set_size(self):
        if self.h_row > 1:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + ((self.w_column -1 ) * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
            else: 
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - (self.border * 2), ((self.h_row * config.bheight) - self.border))
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))
    
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize) 
    
    def numpad_click(self, x, y):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = x // (config.bwidth + config.margin)
        row_click = y // (config.bheight + config.margin)
        if (column_click, row_click) in self.numpad:
            exec(self.numpad[column_click, row_click])
    
    def numpad_press(self, event):
        """Find the mouse position in the gird and execute the event."""
        if (event.unicode) in self.num_press:
            exec(self.num_press[event.unicode])

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN or event.type == FINGERDOWN:
            if self.numpad_active & self.active:
                if event.type == FINGERDOWN:
                    x = event.x * config.width
                    y = event.y * config.height
                    self.numpad_click(x, y)
                else:
                    x, y = event.pos
                    self.pos_mouse = x, y = event.pos
                    self.numpad_click(x, y)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.numpad_press(event)                
                self.text_render()
        return self.text

    def update(self, data):
        # Resize the box if the text is too long.
        if data == '*':
            print(self.text)
            self.text = ''
            self.text_render()
        elif data == '#':
            self.text = self.text[:-1]
            self.text_render()
        else:
            self.text += data
            self.text_render()
        return self.text

    def text_render(self):
        # Re-render the text.
            if len(self.text) > 40:
                self.txt_surface = self.font.render(self.text[len(self.text) - 40:], True, self.color)
            else:
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.color = config.COLOR_ACTIVE if self.active else config.COLOR_INACTIVE
        # Blit the text.
        self.app.blit(self.txt_surface, (self.rect.x+20, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)


class InputBox_Userid: 
    """This input box is require number only user"""
    def __init__(self, start_row, start_column, w_column, h_row, text, app, active = bool, numpad_active = bool):
        self.fontname = 'fonts/SEGOEUIB.TTF'
        self.fontsize = 32
        self.border = 3
        self.set_font()
        self.app = app
        self.start_row = start_row
        self.start_column = start_column
        self.w_column = w_column  
        self.h_row = h_row
        self.set_size()
        self.color = config.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = active
        self.numpad_active = numpad_active
        
        self.numpad = {
            # Click numpad button
            (8, 4): 'self.update("1")',
            (9, 4): 'self.update("2")',
            (10, 4): 'self.update("3")',
            (8, 5): 'self.update("4")',
            (9, 5): 'self.update("5")',
            (10, 5): 'self.update("6")',
            (8, 6): 'self.update("7")',
            (9, 6): 'self.update("8")',
            (10, 6): 'self.update("9")',
            (8, 7): 'self.update("*")',
            (9, 7): 'self.update("0")',
            (10, 7): 'self.update("#")',
        }

        self.num_press = {
            # Click numpad button
            ("1"): 'self.update("1")',
            ("2"): 'self.update("2")',
            ("3"): 'self.update("3")',
            ("4"): 'self.update("4")',
            ("5"): 'self.update("5")',
            ("6"): 'self.update("6")',
            ("7"): 'self.update("7")',
            ("8"): 'self.update("8")',
            ("9"): 'self.update("9")',
            ("0"): 'self.update("0")',
        }

    def set_size(self):
        if self.h_row > 1:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + ((self.w_column -1 ) * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
            else: 
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - (self.border * 2), ((self.h_row * config.bheight) - self.border))
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))
    
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize) 
    
    def numpad_click(self, x, y):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = x // (config.bwidth + config.margin)
        row_click = y // (config.bheight + config.margin)
        if (column_click, row_click) in self.numpad:
            exec(self.numpad[column_click, row_click])
    
    def numpad_press(self, event):
        """Find the mouse position in the gird and execute the event."""
        if (event.unicode) in self.num_press:
            exec(self.num_press[event.unicode])

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN or event.type == FINGERDOWN:
            if self.numpad_active & self.active:
                if event.type == FINGERDOWN:
                    x = event.x * config.width
                    y = event.y * config.height
                    self.numpad_click(x, y)
                else:
                    x, y = event.pos
                    self.pos_mouse = x, y = event.pos
                    self.numpad_click(x, y)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode         
                    # self.numpad_press(event)                
                self.text_render()
        return self.text

    def update(self, data):
        # Resize the box if the text is too long.
        if data == '*':
            print(self.text)
            self.text = ''
            self.text_render()
        elif data == '#':
            self.text = self.text[:-1]
            self.text_render()
        else:
            self.text += data
            self.text_render()
        return self.text

    def text_render(self):
        # Re-render the text.
            if len(self.text) > 40:
                self.txt_surface = self.font.render(self.text[len(self.text) - 40:], True, self.color)
            else:
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.color = config.COLOR_ACTIVE if self.active else config.COLOR_INACTIVE
        # Blit the text.
        self.app.blit(self.txt_surface, (self.rect.x+20, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)

class InputBox_Text:
    """This input box is require text and number"""
    def __init__(self, start_row, start_column, w_column, h_row, text, app, active = bool, numpad_active = bool):
        self.fontname = 'fonts/SEGOEUIB.TTF'
        self.fontsize = 32
        self.border = 3
        self.set_font()
        self.app = app
        self.start_row = start_row
        self.start_column = start_column
        self.w_column = w_column  
        self.h_row = h_row
        self.set_size()
        self.color = config.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = active
        self.numpad_active = numpad_active
        
        self.numpad = {
            # Click clear button
            (8, 6): 'self.update("*")',
            (9, 6): 'self.update("*")',
            (10, 6): 'self.update("*")',
            (8, 7): 'self.update("*")',
            (9, 7): 'self.update("*")',
            (10, 7): 'self.update("*")',
            # Click backspace button
            (8, 4): 'self.update("#")',
            (9, 4): 'self.update("#")',
            (10, 4): 'self.update("#")',
            (8, 5): 'self.update("#")',
            (9, 5): 'self.update("#")',
            (10, 5): 'self.update("#")',
        }

    def set_size(self):
        if self.h_row > 1:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + ((self.w_column -1 ) * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
            else: 
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - (self.border * 2), ((self.h_row * config.bheight) - self.border))
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))
    
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize) 
    
    def numpad_click(self, x, y):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = x // (config.bwidth + config.margin)
        row_click = y // (config.bheight + config.margin)
        if (column_click, row_click) in self.numpad:
            exec(self.numpad[column_click, row_click])

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN or event.type == FINGERDOWN:
            if self.numpad_active & self.active:
                if event.type == FINGERDOWN:
                    x = event.x * config.width
                    y = event.y * config.height
                    self.numpad_click(x, y)
                else:
                    x, y = event.pos
                    self.pos_mouse = x, y = event.pos
                    self.numpad_click(x, y)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode                  
                self.text_render()
        return self.text

    def update(self, data):
        # Resize the box if the text is too long.
        if data == '*':
            print(self.text)
            self.text = ''
            self.text_render()
        elif data == '#':
            self.text = self.text[:-1]
            self.text_render()
        else:
            self.text += data
            self.text_render()
        return self.text

    def text_render(self):
        # Re-render the text.
            if len(self.text) > 40:
                self.txt_surface = self.font.render(self.text[len(self.text) - 40:], True, self.color)
            else:
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.color = config.COLOR_ACTIVE if self.active else config.COLOR_INACTIVE
        # Blit the text.
        self.app.blit(self.txt_surface, (self.rect.x+20, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)

class InputBox_Qrcode:
    """This input box is require text and number"""
    def __init__(self, start_row, start_column, w_column, h_row, text, app, active = bool, numpad_active = bool):
        self.fontname = 'fonts/SEGOEUIB.TTF'
        self.fontsize = 32
        self.border = 3
        self.set_font()
        self.app = app
        self.start_row = start_row
        self.start_column = start_column
        self.w_column = w_column  
        self.h_row = h_row
        self.set_size()
        self.color = config.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = active
        self.numpad_active = numpad_active
        
        self.numpad = {
            # Click clear button
            (8, 6): 'self.update("*")',
            (9, 6): 'self.update("*")',
            (10, 6): 'self.update("*")',
            (8, 7): 'self.update("*")',
            (9, 7): 'self.update("*")',
            (10, 7): 'self.update("*")',
            # Click backspace button
            (8, 4): 'self.update("#")',
            (9, 4): 'self.update("#")',
            (10, 4): 'self.update("#")',
            (8, 5): 'self.update("#")',
            (9, 5): 'self.update("#")',
            (10, 5): 'self.update("#")',
        }

    def set_size(self):
        if self.h_row > 1:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + ((self.w_column -1 ) * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
            else: 
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            if self.w_column > 1:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - (self.border * 2), ((self.h_row * config.bheight) - self.border))
            else:
                self.rect = pygame.Rect((self.start_row * config.bwidth) + ((self.start_row + 1) * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))
    
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize) 
    
    def numpad_click(self, x, y):
        """Find the mouse positionm in the gird and execute the event."""
        column_click = x // (config.bwidth + config.margin)
        row_click = y // (config.bheight + config.margin)
        if (column_click, row_click) in self.numpad:
            exec(self.numpad[column_click, row_click])

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN or event.type == FINGERDOWN:
            if self.numpad_active & self.active:
                if event.type == FINGERDOWN:
                    x = event.x * config.width
                    y = event.y * config.height
                    self.numpad_click(x, y)
                else:
                    x, y = event.pos
                    self.pos_mouse = x, y = event.pos
                    self.numpad_click(x, y)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode                  
                self.text_render()
        return self.text

    def update(self, data):
        # Resize the box if the text is too long.
        if data == '*':
            print(self.text)
            self.text = ''
            self.text_render()
        elif data == '#':
            self.text = self.text[:-1]
            self.text_render()
        else:
            self.text += data
            self.text_render()
        return self.text

    def text_render(self):
        # Re-render the text.
            if len(self.text) > 40:
                self.txt_surface = self.font.render(self.text[len(self.text) - 40:], True, self.color)
            else:
                self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self):
        self.color = config.COLOR_ACTIVE if self.active else config.COLOR_INACTIVE
        # Blit the text.
        self.app.blit(self.txt_surface, (self.rect.x+20, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)

