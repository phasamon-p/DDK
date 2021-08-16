import pygame
from pygame.locals import *
import config
# Valiable and function of request product
request_list = []
request_list2 = []
request_list2_check = []
request_list2_idcheck = []

if config.locker_type > 0:
    locker_time = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
else:
    locker_time = [False, False, False, False, False, False, False, False, False, False, False, False]

def list_idcheck_add(object):
    request_list2_idcheck.append(object)

def llist_idcheck_delete():
    request_list2_idcheck.pop()

def list_idcheck_reset():
    request_list2_idcheck.clear()

def list_check_add(object):
    request_list2_check.append(object)

def llist_check_delete():
    request_list2_check.pop()

def list_check_reset():
    request_list2_check.clear()

def list_add(object):
    request_list.append(object)

def list_delete():
    request_list.pop()

def list_reset():
    request_list.clear()

def add(object):
    request_list2.append(object)

def delete():
    request_list2.pop()

def reset():
    request_list2.clear()


# Set Valiable of activattion list view button
inbox_active = [False, False]

requester_data = {   'requester_id' : "",
                'requester_name' : "",
                'requester_lname' : "",
                'department' : [False, False, False, False, False],
                'fingerid' : "",
                'permission' : "",
                'locker_access' : [False, False, False, False, False, False, False, False, False, False, False, False]}

def requester_add(object):
    requester_data.append(object)

def requester_delete():
    requester_data.pop()

def requester_reset():
    requester_data.clear()

def lockeraccess_reset():
    for x in range(len(requester_data['locker_access'])):
        requester_data['locker_access'][x] = False

def lengh_lockeraccess():
    y = 0
    for x in range(len(requester_data['locker_access'])):
        if requester_data['locker_access'][x]:
            y += 1
    return str(y)

def department():
    text = ''
    for x in range(len(requester_data['department'])):
        if requester_data['department'][x]:
            if text == '':
                text += requester_data['department'][x]
            else: 
                text += ' ' + requester_data['department'][x]
    return str(text)

def requesterdata_reset():
    requester_data['requester_id'] = ''
    requester_data['requester_name'] = ''
    requester_data['requester_lname'] = ''
    requester_data['department'] = [False, False, False, False, False]
    requester_data['fingerid'] = ''
    requester_data['permission'] = ''
    requester_data['locker_access'] = [False, False, False, False, False, False, False, False, False, False, False, False]
    
def requesterdata_setedit(data):
    requester_data['requester_id'] = data.requester_id   
    requester_data['requester_name'] = data.requester_name   
    requester_data['requester_lname'] = data.requester_lname   
    requester_data['department'] = data.department   
    requester_data['fingerid'] = data.fingerid   
    requester_data['permission'] = data.permission   
    requester_data['locker_access'] = data.locker 


def check_lockeraccess():
    if config.locker_type == 0:
        access_list = [False, False, False, False, False, False, False, False, False, False, False, False]
    else:
        access_list = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    
    for x in range(len(request_list2)):
        locker = request_list2[x].locker_number.split(",")
        # print("locker", locker)
        # print("request_list2[x].locker_number", request_list2[x].locker_number)
        for y in range(len(locker)):
            # print(requester_data['locker_access'])
            # print(x, int(locker[y]) +1)
            if requester_data['locker_access'][int(locker[y]) - 1]:
                access_list[int(locker[y]) - 1] = True
            else:
                return False
    return access_list