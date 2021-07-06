import pygame
from pygame.locals import *
import config 

class InputBox:

    def __init__(self, x, y, w, h, text, app):
        self.fontname = None # 'fonts/SEGOEUIB.TTF'
        self.fontsize = 32
        self.set_font()
        self.app = app
        self.rect = pygame.Rect(x, y, w, h)
        self.color = config.COLOR_INACTIVE
        self.text = text
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

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
        self.app.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(self.app, self.color, self.rect, 5)