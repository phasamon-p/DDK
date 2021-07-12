import pygame
from pygame.locals import *

user_data = {   'user_id' : "",
                'user_name' : "",
                'user_lname' : "",
                'department' : "",
                'fingerid' : "",
                'permission' : ""}

def add(object):
    user_data.append(object)

def delete():
    user_data.pop()

def reset():
    user_data.clear()


