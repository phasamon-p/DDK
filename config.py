import pygame
from pygame.locals import *

locker_type = 0 #Set default locker type (0 is 12 lockers, 1 is 16 lockers)

db = {
    "host": "localhost",
    "database": "ddk_lockers",
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
dark_yellow = (164, 137, 0)

COLOR_INACTIVE = black
COLOR_ACTIVE = blue

VERSION = " (DDK firmware V1.1)"

stop = False

# Set size of screen
pygame.display.init()  # Initialize the display module
pygame.display.get_surface()
# screensize = width, height = (pygame.display.Info().current_w, pygame.display.Info().current_h) 
screensize = width, height = (1280,800) 
flags  = RESIZABLE

time_extention = 0
door_status = False
time_out = 600 # Set time out 10 minutes exit to home page. 
