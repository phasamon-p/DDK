import pygame
from pygame.locals import *

# Valiable and function of request product
request_list = []

def add(object):
    request_list.append(object)

def delete():
    request_list.pop()

def reset():
    request_list.clear()

# Set Valiable of activattion list view button
inbox_active = [False, False]

