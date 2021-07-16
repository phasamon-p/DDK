import pygame
from pygame.locals import *
import config 

class Title():
    """Create a text object."""

    def __init__(self, text, pos, app, **option):
        self.text = text
        self.pos = pos
        self.app = app

        self.fontname = 'fonts/SEGOEUIB.TTF'
        self.fontsize = 72
        self.fontcolor = Color(config.black)
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        self.app.blit(self.img, self.rect)

class Text_Mainbutton():
    """Create a text object."""

    def __init__(self, text, pos, app, **option):
        self.text = text
        self.pos = pos
        self.app = app

        self.fontname = 'fonts/SEGOEUI.TTF'
        self.fontsize = 64
        self.fontcolor = Color(config.white)
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)
        
    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        self.app.blit(self.img, self.rect)

class Number():
    """Create a text object."""

    def __init__(self, text, pos, app, **option):
        self.text = text
        self.pos = pos
        self.app = app

        self.fontname = 'fonts/SEGOEUI.TTF'
        self.fontsize = 36
        self.fontcolor = Color(config.white)
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        self.app.blit(self.img, self.rect)

class Text_Button():
    """Create a text object."""

    def __init__(self, text, pos, app, **option):
        self.text = text
        self.pos = pos
        self.app = app

        self.fontname = 'fonts/SEGOEUI.TTF'
        self.fontsize = 48
        self.fontcolor = Color(config.white)
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        self.app.blit(self.img, self.rect)

class Text_Button_Medium():
    """Create a text object."""

    def __init__(self, text, pos, app, **option):
        self.text = text
        self.pos = pos
        self.app = app

        self.fontname = 'fonts/SEGOEUI.TTF'
        self.fontsize = 36
        self.fontcolor = Color(config.white)
        self.set_font()
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        self.app.blit(self.img, self.rect)    

class Header_Table():
    """Create a text object."""

    def __init__(self, text, column, row, app, **option):
        self.text = text
        self.fontname = 'fonts/SEGOEUI.TTF'
        self.fontsize = 30
        self.fontcolor = Color(config.black)
        self.set_font()
        self.column = column
        self.row = row
        self.pos = ((self.column * config.bwidth) + config.margin + 5 ,(self.row * config.bheight) + (config.margin * (self.row - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))
        self.app = app
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        self.app.blit(self.img, self.rect)    
    
class Header_Result():
    """Create a text object."""

    def __init__(self, text, column, row, app, **option):
        self.text = text
        self.fontname = 'fonts/SEGOEUI.TTF'
        self.fontsize = 30
        self.fontcolor = Color(config.blue)
        self.set_font()
        self.column = column
        self.row = row
        self.pos = ((self.column * config.bwidth) + config.margin + 5 ,(self.row * config.bheight) + (config.margin * (self.row - 1)) + ((config.bheight - self.fontsize + config.margin) / 2))
        self.app = app
        self.render()

    def set_font(self):
        """Set the font from its name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        self.app.blit(self.img, self.rect)    