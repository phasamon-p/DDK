""" Main managing user interface """
import pygame
from pygame.locals import *
import json

import serial
import views
import services
import config

if __name__ == '__main__':
    services.init()
    views.Home().run()
    pygame.quit()