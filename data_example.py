import pygame
from pygame.locals import *
import json

product =  { 
            "product": [
                {"section": "AS1/AS2", "qrcode": "1111", "item_number": "A412002771", "product_name": "19TEAX24", "part_number": "S602", "part_name": "CUTTER", "drawing_number": "", "locker_number": "1", "other": ""},
                {"section": "AS1/AS2", "qrcode": "1111", "item_number": "A412003068", "product_name": "21D6X12", "part_number": "#209107", "part_name": "B2-CUTTER", "drawing_number": "", "locker_number": "1", "other": ""},
                {"section": "AS1/AS2", "qrcode": "1111", "item_number": "A412003069", "product_name": "21D6X12", "part_number": "#209309", "part_name": "B2-DIE", "drawing_number": "", "locker_number": "1", "other": ""},
                {"section": "AS1/AS2", "qrcode": "1111", "item_number": "A412003070", "product_name": "21D6X22", "part_number": "#103062", "part_name": "B1-CUT DIE B", "drawing_number": "", "locker_number": "1", "other": ""},
                {"section": "AS1/AS2", "qrcode": "1111", "item_number": "A412003071", "product_name": "21D6X22", "part_number": "#047", "part_name": "B1-CUT PUNCH A", "drawing_number": "", "locker_number": "1", "other": ""},
                {"section": "AS1/AS2", "qrcode": "1111", "item_number": "A412003072", "product_name": "21D6X22", "part_number": "#048", "part_name": "B1-CUT DIE A", "drawing_number": "", "locker_number": "1", "other": ""},
                {"section": "AS1/AS2", "qrcode": "1111", "item_number": "A412003073", "product_name": "21D6X22", "part_number": "#064", "part_name": "B1-CUT PUNCH B", "drawing_number": "", "locker_number": "1", "other": ""},
                {"section": "AS1/AS2", "qrcode": "1111", "item_number": "A412003074", "product_name": "21D6X22", "part_number": "#013", "part_name": "B1-DIE DETECT", "drawing_number": "", "locker_number": "1", "other": ""},
                {"section": "AS1/AS2", "qrcode": "1111", "item_number": "A412003075", "product_name": "21D6X22", "part_number": "#028", "part_name": "B1-PUNCH DETECT", "drawing_number": "", "locker_number": "1", "other": ""},
                {"section": "AS1/AS2", "qrcode": "1111", "item_number": "A412003076", "product_name": "21D6X22", "part_number": "#203002", "part_name": "B2-PUNCH", "drawing_number": "", "locker_number": "1", "other": ""},
                {"section": "MO1/MO2", "qrcode": "1111", "item_number": "AG21004267", "product_name": "TEBBT-BD-D1", "part_number": "#13-72", "part_name": "TRIMMING PUNCH", "drawing_number": "MO4D-TEBB-076", "locker_number": "1", "other": ""},
                {"section": "MO1/MO2", "qrcode": "1111", "item_number": "AG21004000", "product_name": "FCT-RA05-5A-500", "part_number": "#515", "part_name": "EHSF2.5-134.34-P1.5-N40", "drawing_number": "MODD-FTC-1125#1053", "locker_number": "1", "other": ""},
                {"section": "PR", "qrcode": "1111", "item_number": "A212020290", "product_name": "BB35AA-RAA0A100E", "part_number": "#56", "part_name": "TRIMMING 2 PUNCH", "drawing_number": "PRDD-BB35K-1467", "locker_number": "1", "other": "BB35AA-RAA0A100E#4"}],
            }