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

        self.fontname = 'fonts/SEGOEUIB.TTF'
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