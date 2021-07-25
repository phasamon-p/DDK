import pygame
from pygame.locals import *

admin_data = {   'admin_id' : "",
                'admin_name' : "",
                'admin_lname' : "",
                'department' : [False, False, False, False, False],
                'fingerid' : "",
                'permission' : "",
                'locker_access' : [False, False, False, False, False, False, False, False, False, False, False, False]}

def add(object):
    admin_data.append(object)

def delete():
    admin_data.pop()

def reset():
    admin_data.clear()

def lockeraccess_reset():
    for x in range(len(admin_data['locker_access'])):
        admin_data['locker_access'][x] = False

def lengh_lockeraccess():
    y = 0
    for x in range(len(admin_data['locker_access'])):
        if admin_data['locker_access'][x]:
            y += 1
    return str(y)

def department():
    text = ''
    for x in range(len(admin_data['department'])):
        if admin_data['department'][x]:
            if text == '':
                text += admin_data['department'][x]
            else: 
                text += ' ' + admin_data['department'][x]
    return str(text)

def admindata_reset():
    admin_data['admin_id'] = ''
    admin_data['admin_name'] = ''
    admin_data['admin_lname'] = ''
    admin_data['department'] = [False, False, False, False, False]
    admin_data['fingerid'] = ''
    admin_data['permission'] = ''
    admin_data['locker_access'] = [False, False, False, False, False, False, False, False, False, False, False, False]
    
def admindata_setedit(data):
    admin_data['admin_id'] = data.admin_id   
    admin_data['admin_name'] = data.admin_name   
    admin_data['admin_lname'] = data.admin_lname   
    admin_data['department'] = data.department   
    admin_data['fingerid'] = data.fingerid   
    admin_data['permission'] = data.permission   
    admin_data['locker_access'] = data.locker 
        

