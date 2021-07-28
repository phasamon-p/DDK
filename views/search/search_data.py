import pygame
from pygame.locals import *
import config

request_list = []

def list_add(object):
    request_list.append(object)

def list_delete():
    request_list.pop()

def list_reset():
    request_list.clear()