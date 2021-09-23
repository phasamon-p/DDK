import pygame
from pygame.locals import *
import config 

request_list = []
old_id = ''

def list_add(object):
    request_list.append(object)

def list_delete():
    request_list.pop()

def list_reset():
    request_list.clear()

emergency_data = { 'user_id' : "",
                   'locker' :1}

def add(object):
    emergency_data.append(object)

def delete():
    emergency_data.pop()

def reset():
    emergency_data.clear()

def userdata_reset():
    emergency_data['user_id'] = ''


        

