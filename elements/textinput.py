import pygame
from pygame.locals import *
import config 

class InputBox:

    def __init__(self, start_row, start_column, w_column, h_row, text, app):
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
        self.active = False

    def set_size(self):
        if self.h_row > 1:
            self.rect = pygame.Rect((self.start_row * config.bwidth) + (self.start_row * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) + ((self.h_row- 1) * config.margin)) - self.border)
        else:
            self.rect = pygame.Rect((self.start_row * config.bwidth) + (self.start_row * config.margin), (self.start_column * config.bheight) + ((self.start_column + 1) * config.margin) + 1 ,((self.w_column * config.bwidth) + (self.w_column * config.margin)) - self.border, ((self.h_row * config.bheight) - self.border))
    
    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = config.COLOR_ACTIVE if self.active else config.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                if len(self.text) > 10:
                    self.txt_surface = self.font.render(self.text[len(self.text)-10:], True, self.color)
                else:
                    self.txt_surface = self.font.render(self.text, True, self.color)
        return self.text

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self):
        # Blit the text.
        self.app.blit(self.txt_surface, (self.rect.x+20, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, self.border)