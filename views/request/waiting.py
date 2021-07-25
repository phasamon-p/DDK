""" Home (Main app) """
import pygame
from pygame.locals import *

import time
import os
import services
import config 
import elements
import views

class requester_data():
    requester_id = ""
    requester_name = ""
    requester_lname = ""
    department = ""
    fingerid = ""
    permission = ""
    locker = ""

class Waiting:
    """Create a single-window app with multiple scenes."""

    def __init__(self, data):
        """Initialize pygame and the application."""
        pygame.init() # Initialize the pygame
        pygame.display.init()  # Initialize the display module
        self.screen = pygame.display.set_mode(config.screensize, config.flags) # Set mode of screen
        self.screen.fill(Color('white')) # Set background color of screen
        self.running = True 
        self.data = data
        self.caption = 'Requester finger scan'
        self.title = 'REQUESTER FINGER SCAN'
    
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
                        elements.Title(self.title, pos=(200, 67), app=(self.screen)).draw()
                        if services.lockerrequest_open(self.data):
                            views.Request_Check()
                            pygame.quit()
                        else:
                            pass
            pygame.display.update()
            pygame.display.flip()
        pygame.quit()

class Person:
  def __init__(self):
    self.name = "Phasamon Panyee"
    self.age = 27