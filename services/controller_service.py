# from views.admin.usermanagement.user_data import reset
import board
import busio
import time
import digitalio
import config
import time
import views
import services
from adafruit_mcp230xx.mcp23017 import MCP23017

import subprocess

i2c = busio.I2C(board.SCL, board.SDA)
mcp = [0,0,0,0,0,0,0,0]
pin = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
error = False
mux_out = [0,1,2,3]
mux_in = [4,5,6,7]
IR = [0,7,6,5,4,3,2,0,0,0,0,0,0,0]
if config.locker_type == 0:
        buzzer = [0,15]
        on_circuit = [0,12]
else:
        buzzer = [1,1]
        on_circuit = [1,0]
on_sensor = [1,3]

extention_time = 0

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

# def lockertimeout(lockNo, now): # function check timeout after touch\
#         if (getStatus(lockNo)):
#             if (time.time() - now) > tout: 
#                 alarmOn()
#                 return False
# #             else:
# #                 alarmOff()
# #                 return True
#         else:
#             alarmOff()
#             return True

def lockertimeout(): # function check timeout after touch
        status = False
        for x in range(16):
                if getStatus(x + 1):
                        status = True
        tout = services.getbuzzer() * 60
        if status:
                if config.locker_type > 0:
                        if services.getStatus_2(8):
                                config.time_extention += 60 
                        # Check status locker 8
                        if services.getStatus(1):
                                if (time.time() - views.request_data.locker_time[7]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False
                        # Check status locker 7
                        if services.getStatus(2):
                                if (time.time() - views.request_data.locker_time[6]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 6
                        if services.getStatus(3):
                                if (time.time() - views.request_data.locker_time[5]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 5
                        if services.getStatus(4):
                                if (time.time() - views.request_data.locker_time[4]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 4
                        if services.getStatus(5):
                                if (time.time() - views.request_data.locker_time[3]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 3
                        if services.getStatus(6):
                                if (time.time() - views.request_data.locker_time[2]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 2
                        if services.getStatus(7):
                                if (time.time() - views.request_data.locker_time[1]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 1
                        if services.getStatus(8):
                                if (time.time() - views.request_data.locker_time[0]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False
                        # Check status locker 16
                        if services.getStatus(9):
                                if (time.time() - views.request_data.locker_time[15]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 15
                        if services.getStatus(10):
                                if (time.time() - views.request_data.locker_time[14]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 14
                        if services.getStatus(11):
                                if (time.time() - views.request_data.locker_time[13]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 13
                        if services.getStatus(12):
                                if (time.time() - views.request_data.locker_time[12]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False
                        # Check status locker 12
                        if services.getStatus(13):
                                if (time.time() - views.request_data.locker_time[11]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 11
                        if services.getStatus(14):
                                if (time.time() - views.request_data.locker_time[10]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 10
                        if services.getStatus(15):
                                if (time.time() - views.request_data.locker_time[9]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False
                        # Check status locker 9
                        if services.getStatus(16):
                                if (time.time() - views.request_data.locker_time[8]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False
                else:
                        if services.getStatus(12):
                                config.time_extention += 60 
                        # Check status locker 8
                        if services.getStatus(1):
                                if (time.time() - views.request_data.locker_time[7]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False
                        # Check status locker 7
                        if services.getStatus(2):
                                if (time.time() - views.request_data.locker_time[6]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 6
                        if services.getStatus(3):
                                if (time.time() - views.request_data.locker_time[5]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 5
                        if services.getStatus(4):
                                if (time.time() - views.request_data.locker_time[4]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 4
                        if services.getStatus(5):
                                if (time.time() - views.request_data.locker_time[3]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 3
                        if services.getStatus(6):
                                if (time.time() - views.request_data.locker_time[2]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 2
                        if services.getStatus(7):
                                if (time.time() - views.request_data.locker_time[1]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 1
                        if services.getStatus(8):
                                if (time.time() - views.request_data.locker_time[0]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False
                        # Check status locker 12
                        if services.getStatus(13):
                                if (time.time() - views.request_data.locker_time[11]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 11
                        if services.getStatus(14):
                                if (time.time() - views.request_data.locker_time[10]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False 
                        # Check status locker 10
                        if services.getStatus(15):
                                if (time.time() - views.request_data.locker_time[9]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False
                        # Check status locker 9
                        if services.getStatus(16):
                                if (time.time() - views.request_data.locker_time[8]) > (tout + config.time_extention):
                                        alarmOn()
                                        return False
        else:
                alarmOff()
                config.time_extention = 0
                return True
        alarmOff()

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

def getStatus_2(lockNo):
        try:
            relay = ((lockNo-1) // 16) + 5 #div get status
            pos = ((lockNo-1) % 16)   #mod get pos
            return not pin[relay][pos].value
        except:
            print("I2C error")

def getAllStatus():
        if config.locker_type > 0:
                locker = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
        else:
                locker = [False, False, False, False, False, False, False, False, False, False, False, False]
        
        for x in range(len(locker)):
                try:
                        relay = ((x + 1) // 16) + 4 #div get status
                        pos = ((x + 1) % 16)   #mod get pos
                        if not pin[relay][pos].value:
                                locker[x + 1] = True
                except:
                        print("I2C error")
        return locker

def lockerrequest_open(data):
        if config.locker_type == 0:
                relay = 0
        else:
                relay = 0 
        print("Data request : ", data)
        for x in range(len(data)):
                if data[x]:
                        relay = (((x + 1) - 1) // 16) + relay  #div get relay
                        pos = (((x + 1) - 1) % 16)   #mod get pos
                        try: 
                                """" add 16 locker control """
                                if relay >= 0 and pos >= 0 :
                                        pin[relay][pos].value = False    # Set pin to HIGH (ON) (1)
                                        time.sleep(0.5)
                                        pin[relay][pos].value = True    # Set pin to Low (ON) (1)
                                        time.sleep(0.5)
                                        views.request_data.locker_time[x] = time.time()
                        except:
                                print("Lock I2C error")
                                return False
        return True

def locker_open(relay, lockNo):
        relay = ((lockNo-1) // 16) + relay  #div get relay
        pos = ((lockNo-1) % 16)   #mod get pos
        print(relay, pos)
        try: 
            if relay >= 0 and pos >= 0 :
                pin[relay][pos].value = False    # Set pin to HIGH (ON) (1)
                time.sleep(0.5)
                pin[relay][pos].value = True    # Set pin to Low (ON) (1)
                time.sleep(0.5)
                views.request_data.locker_time[lockNo - 1] = time.time()
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
    print("Buzeer No. 8 : ", getStatus_2(8))



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
#         locker_open(1, i )

#     if c == "d":
#         status = False

#     if c == "1":
#         init()

#     if c == "p":
#         res = subprocess.call("ping 8.8.8.8 -c 1 | grep 'received' | awk -F',' '{ print $2}' | awk '{ print $1}'", shell=True)
#         print("Res : ", res)




