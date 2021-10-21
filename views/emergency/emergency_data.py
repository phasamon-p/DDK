from numpy.core.numeric import True_
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

emergency_data = { 'user_id' :'',
                   'locker' :'',
                   'emergency_request':False}

def add(object):
    emergency_data.append(object)

def delete():
    emergency_data.pop()

def reset():
    emergency_data.clear()

def emergrncydata_reset():
    emergency_data ['user_id']=''
    emergency_data ['locker']=''
    emergency_data ['emergency_request']=False


    
        

