import board
import busio
import time
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017

import subprocess

i2c = busio.I2C(board.SCL, board.SDA)
mcp = [0,0,0,0,0,0,0,0]
pin = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
error = False
mux_out = [0,1,2,3]
mux_in = [4,5,6,7]
IR = [0,7,6,5,4,3,2,0,0,0,0,0,0,0]
buzzer = [1,3]
on_circuit = [1,2]
on_sensor = [1,3]
tout = 1800

status = True 

try:
        mcp[0] = MCP23017(i2c, address=0x20)
        mcp[1] = MCP23017(i2c, address=0x21)
        mcp[2] = MCP23017(i2c, address=0x22)
        mcp[3] = MCP23017(i2c, address=0x23)
        mcp[4] = MCP23017(i2c, address=0x24)
        mcp[5] = MCP23017(i2c, address=0x25)
        mcp[6] = MCP23017(i2c, address=0x26)
        mcp[7] = MCP23017(i2c, address=0x27)
except:
        error = True
        print('I2C Error')


if not error:
        for i in mux_out:
                for j in range(16):
                        pin[i][j] = mcp[i].get_pin(j)
                        pin[i][j].switch_to_output(value=True)
        for i in mux_in:
                for j in range(16):
                        pin[i][j] = mcp[i].get_pin(j)
                        pin[i][j].direction = digitalio.Direction.INPUT
                        pin[i][j].pull = digitalio.Pull.UP  
def init():
        try:
                pin[on_circuit[0]][on_circuit[1]].value = False    # Set pin to HIGH (ON) (1)
                time.sleep(0.5)
        except:
                print("Init I2C error")

def uninit():
        try:
                pin[on_circuit[0]][on_circuit[1]].value = True    # Set pin to HIGH (ON) (1)
                time.sleep(0.5)
        except:
                print("Init I2C error")

def lockertimeout(lockNo, now): # function check timeout after touch
        if (getStatus(lockNo)):
            if (time.time() - now) > tout: 
                alarmOn()
                return False
#             else:
#                 alarmOff()
#                 return True
        else:
            alarmOff()
            return True

def alarmOn():
        try:
                pin[buzzer[0]][buzzer[1]].value = False    # Set pin to HIGH (ON) (1)
                time.sleep(0.5)
        except:
                print("Buzzer I2C error")
def alarmOff():
        try:
                pin[buzzer[0]][buzzer[1]].value = True    # Set pin to LOW (OFF) (1)
                time.sleep(0.5)
        except:
                print("Buzzer I2C error")  

def getStatus(lockNo):
        try:
            relay = ((lockNo-1) // 16) + 4 #div get status
            pos = ((lockNo-1) % 16)   #mod get pos
            return not pin[relay][pos].value
        except:
            print("I2C error")

def locker_open(relay, lockNo):
        relay = ((lockNo-1) // 16)+relay  #div get relay
        pos = ((lockNo-1) % 16)   #mod get pos
        print(relay, pos)
        try: 
            if relay >= 0 and pos >= 0 :
                pin[relay][pos].value = False    # Set pin to HIGH (ON) (1)
                time.sleep(0.5)
                pin[relay][pos].value = True    # Set pin to Low (ON) (1)
                time.sleep(0.5)
        except:
            print("Lock I2C error")
            
            
def locker_close(relay, lockNo):
        relay = ((lockNo-1) // 16) + relay  #div get relay
        pos = ((lockNo-1) % 16)   #mod get pos
        try:
            if relay >= 0 and pos >= 0 :
                    pin[relay][pos].value = True    # Set pin to LOW (OFF) (1)
        except:
            print("Lock I2C error")
            

def checkstatus():
    for x in range(18):
        print("No. ", x+1, " : ", getStatus(x+1))


def get_num():
    """Use input() to get a door number from 1 to 18."""
    i = 0
    while (i > 19) or (i < 1):
        try:
            i = int(input("Enter ID # from 1-18: "))
        except ValueError:
            pass
    return i

        
# while status:
#     init()
#     print("----------------")
#     print("Controller Testing:")
#     print("e) Door Status Checking")
#     print("f) Door Open")
#     print("p) Internet ping Checking")
#     print("d) Exit Testing")
#     print("----------------")
#     c = input(" ")

#     if c == "e":
#         checkstatus()

#     if c == "f":
#         i = get_num()
#         locker_open(0, i )

#     if c == "d":
#         status = False

#     if c == "1":
#         init()

#     if c == "p":
#         res = subprocess.call("ping 8.8.8.8 -c 1 | grep 'received' | awk -F',' '{ print $2}' | awk '{ print $1}'", shell=True)
#         print("Res : ", res)




