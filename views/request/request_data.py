import pygame
from pygame.locals import *

# Valiable and function of request product
request_list = []

def add(object):
    request_list.append(object)

def delete():
    request_list.pop()

# Set Valiable of activattion list view button
inbox_active = [False, False]
