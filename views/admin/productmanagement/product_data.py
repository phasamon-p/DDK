import pygame
from pygame.locals import *

# Set Valiable of activattion input box
inbox_active = [False, False]

# Valiable and function of request product
request_list = []
old_qrcode = ''

def list_add(object):
    request_list.append(object)

def list_delete():
    request_list.pop()

def list_reset():
    request_list.clear()

product_data = {    'section' : [False, False, False, False, False],
                    'qrcode' : "",
                    'item_number' : "",
                    'product_name' : "",
                    'part_number' : "",
                    'part_name' : "",
                    'drawing_number' : "",
                    'locker_number' : [False, False, False, False, False, False, False, False, False, False, False, False],
                    'quantity' : "",
                    'other' : "",
                    'drawer' : "",
                    'cavity' : ""}

def add(object):
    product_data.append(object)

def delete():
    product_data.pop()

def reset():
    product_data.clear()

def locker_reset():
    for x in range(len(product_data['locker_number'])):
        product_data['locker_number'][x] = False

def lengh_lockeraccess():
    y = 0
    for x in range(len(product_data['locker_number'])):
        if product_data['locker_number'][x]:
            y += 1
    return str(y)

def section():
    text = ''
    for x in range(len(product_data['section'])):
        if product_data['section'][x]:
            if text == '':
                text += product_data['section'][x]
            else: 
                text += ' ' + product_data['section'][x]
    return str(text)

def productdata_reset():
    product_data['section'] = [False, False, False, False, False]
    product_data['qrcode'] = ''
    product_data['item_number'] = ''
    product_data['product_name'] = ''
    product_data['part_number'] = ''
    product_data['part_name'] = ''
    product_data['drawing_number'] = ''
    product_data['locker_number'] = [False, False, False, False, False, False, False, False, False, False, False, False]
    product_data['quantity'] = ''
    product_data['other'] = ''
    product_data['drawer'] = ''
    product_data['cavity'] = ''

def productdata_setedit(data):
 
    product_data['section'] =  data.section
    product_data['qrcode'] =  data.qrcode
    product_data['item_number'] =  data.item_number
    product_data['product_name'] =  data.product_name
    product_data['part_number'] =  data.part_number
    product_data['part_name'] =  data.part_name
    product_data['drawing_number'] =  data.drawing_number
    product_data['locker_number'] =  data.locker_number
    product_data['quantity'] =  data.quantity
    product_data['other'] =  data.other
    product_data['drawer'] = data.drawer
    product_data['cavity'] = data.cavity
    
    old_qrcode = data.qrcode

