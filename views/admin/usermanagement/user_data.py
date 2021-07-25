import pygame
from pygame.locals import *

request_list = []
old_id = ''

def list_add(object):
    request_list.append(object)

def list_delete():
    request_list.pop()

def list_reset():
    request_list.clear()

user_data = {   'user_id' : "",
                'user_name' : "",
                'user_lname' : "",
                'department' : [False, False, False, False, False],
                'fingerid' : "",
                'permission' : "",
                'locker_access' : [False, False, False, False, False, False, False, False, False, False, False, False]}

def add(object):
    user_data.append(object)

def delete():
    user_data.pop()

def reset():
    user_data.clear()

def lockeraccess_reset():
    for x in range(len(user_data['locker_access'])):
        user_data['locker_access'][x] = False

def lengh_lockeraccess():
    y = 0
    for x in range(len(user_data['locker_access'])):
        if user_data['locker_access'][x]:
            y += 1
    return str(y)

def department():
    text = ''
    for x in range(len(user_data['department'])):
        if user_data['department'][x]:
            if text == '':
                text += user_data['department'][x]
            else: 
                text += ' ' + user_data['department'][x]
    return str(text)

def userdata_reset():
    user_data['user_id'] = ''
    user_data['user_name'] = ''
    user_data['user_lname'] = ''
    user_data['department'] = [False, False, False, False, False]
    user_data['fingerid'] = ''
    user_data['permission'] = ''
    user_data['locker_access'] = [False, False, False, False, False, False, False, False, False, False, False, False]

def userdata_setedit(data):
    user_data['user_id'] = data.user_id   
    user_data['user_name'] = data.user_name   
    user_data['user_lname'] = data.user_lname   
    user_data['department'] = data.department   
    user_data['fingerid'] = data.fingerid   
    user_data['permission'] = data.permission   
    user_data['locker_access'] = data.locker   
    old_id = data.user_id   

        

