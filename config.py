import pygame
from pygame.locals import *

db = {
    "host": "localhost",
    "database": "medicallocker",
    "user": "root",
    "password": "1234",
}

bsize = bwidth, bheight = (102, 62)
margin = 5

# Set colors
white = (255, 255, 255)
blue = (17, 41, 126)
black = (60, 60, 60)
red = (174, 12, 12)
green = (0, 170, 0)
yellow = (253, 215, 125)
blue_arm = (2, 89, 154)
light_blue = (59, 55, 89)
dark_gray = (23, 23, 23) 
gray = (136, 136, 136) 

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

stop = False

# Set size of screen
pygame.display.init()  # Initialize the display module
pygame.display.get_surface()
# screensize = width, height = (pygame.display.Info().current_w, pygame.display.Info().current_h) 
screensize = width, height = (1280,800) 
flags = RESIZABLE