import config
import mysql.connector 
from mysql.connector import Error
# from views.admin.usermanagement.user_data import *
import time
import adafruit_fingerprint
#If using with a computer such as Linux/RaspberryPi, Mac, Windows with USB/serial converter:
import serial
try:
    uart = serial.Serial("/dev/ttyUSB0", baudrate=57600, timeout=1)
    finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)
    
except:
    print('Finger Print Error')

# If using with Linux/Raspberry Pi and hardware UART:
#import serial
#uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)

########################################### ABOUT CONECTION ########################################### 


def mysqlconnect():
    try:
        return mysql.connector.connect(host=config.db["host"], database=config.db["database"], user=config.db["user"], password=config.db["password"])
        # if connection.is_connected():
        #     db_Info = connection.get_server_info()
        #     print("Connected to MySQL Server version ", db_Info)
        #     cursor = connection.cursor()
        #     cursor.execute("select database();")
        #     record = cursor.fetchone()
        #     print("You're connected to database: ", record)
    except Error as e:
        return e

########################################### ABOUT FINGER PRINT ##########################################

def getfingerid():
    try:
        connection = mysqlconnect()
        sql_Select_Query = "select * from locker_count"
        cursor = connection.cursor()
        cursor.execute(sql_Select_Query)
        # get all records
        records = cursor.fetchall()
        return records[0][1] + 1

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

            "UPDATE locker_count set count = %s where id = %s "

def updatefinrgerprint(id):
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()
        mySql_update_query = "UPDATE locker_count set count = %s where id = %s "
        cursor.execute(mySql_update_query, (id, 1))
        connection.commit()

        return True

    except mysql.connector.Error as error:
        print("Failed e record: ", format(error))
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

########################################### ABOUT FINGER PRINT ADAFRUIT ##########################################

def get_fingerprint():
    """Get a finger print image, template it, and see if it matches!"""
    try:
        print("Waiting for image...")
        while finger.get_image() != adafruit_fingerprint.OK:
            pass
        print("Templating...")
        if finger.image_2_tz(1) != adafruit_fingerprint.OK:
            return False
        print("Searching...")
        if finger.finger_search() != adafruit_fingerprint.OK:
            return False
        return [True, finger.finger_id, finger.confidence]
    except:
        print('Finger Print Error')

def enroll_finger(location):
    """Take a 2 finger images and template it, then store in 'location'"""
    for fingerimg in range(1, 3):
        if fingerimg == 1:
            print("Place finger on sensor...", end="", flush=True)
        else:
            print("Place same finger again...", end="", flush=True)
        while True:
            i = finger.get_image()
            if i == adafruit_fingerprint.OK:
                print("Image taken")
                break
            if i == adafruit_fingerprint.NOFINGER:
                print(".", end="", flush=True)
            elif i == adafruit_fingerprint.IMAGEFAIL:
                print("Imaging error")
                return False
            else:
                print("Other error")
                return False

        print("Templating...", end="", flush=True)
        i = finger.image_2_tz(fingerimg)
        if i == adafruit_fingerprint.OK:
            print("Templated")
        else:
            if i == adafruit_fingerprint.IMAGEMESS:
                print("Image too messy")
            elif i == adafruit_fingerprint.FEATUREFAIL:
                print("Could not identify features")
            elif i == adafruit_fingerprint.INVALIDIMAGE:
                print("Image invalid")
            else:
                print("Other error")
            return False

        if fingerimg == 1:
            print("Remove finger")
            time.sleep(1)
            while i != adafruit_fingerprint.NOFINGER:
                i = finger.get_image()
    print("Creating model...", end="", flush=True)
    i = finger.create_model()
    if i == adafruit_fingerprint.OK:
        print("Created")
    else:
        if i == adafruit_fingerprint.ENROLLMISMATCH:
            print("Prints did not match")
        else:
            print("Other error")
        return False

    print("Storing model #%d..." % location, end="", flush=True)
    i = finger.store_model(location)
    if i == adafruit_fingerprint.OK:
        print("Stored")
    else:
        if i == adafruit_fingerprint.BADLOCATION:
            print("Bad storage location")
        elif i == adafruit_fingerprint.FLASHERR:
            print("Flash storage error")
        else:
            print("Other error")
        return False

    return True


##################################################

def get_num():
    """Use input() to get a valid number from 1 to 127. Retry till success!"""
    i = 0
    while (i > 127) or (i < 1):
        try:
            i = int(input("Enter ID # from 1-127: "))
        except ValueError:
            pass
    return i

def delete_fingerprint(location):
    if finger.delete_model(location) == adafruit_fingerprint.OK:
        print("Deleted!")
        return True
    else:
        print("Failed to delete")
        return False

# while True:
#     print("----------------")
#     if finger.read_templates() != adafruit_fingerprint.OK:
#         raise RuntimeError("Failed to read templates")
#     print("Fingerprint templates:", finger.templates)
#     print("e) enroll print")
#     print("f) find print")
#     print("d) delete print")
#     print("----------------")
#     c = input(" ")

#     if c == "e":
#         enroll_finger(get_num())
#     if c == "f":
#         if get_fingerprint():
#             print("Detected #", finger.finger_id, "with confidence", finger.confidence)
#         else:
#             print("Finger not found")
#     if c == "d":
#         if finger.delete_model(get_num()) == adafruit_fingerprint.OK:
#             print("Deleted!")
#         else:
#             print("Failed to delete")