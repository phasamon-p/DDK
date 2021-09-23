import config
import mysql.connector
from mysql.connector import Error
#from views.admin.usermanagement.user_data import *
import time
import datetime
#import services
#import views

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

########################################### ABOUT LOG ###########################################

def getdate():
    try:
        date = datetime.datetime.now()
        day = date.day
        month = date.month
        year = date.year
        hour = date.hour
        minute = date.minute
        second = date.second
        print("datetime : ", date)
        print("day : ", day)
        print("month : ", month)
        print("year : ", year)
        print("hour : ", hour)
        print("minute : ", minute)
        print("second : ", second)
    except Error as e:
        print("Error : ", e)

def insert_emegency_log(user_id,locker):
    try:
        connection = mysqlconnect()
        mySql_insert_query = """INSERT INTO admin_log (adminid, date_login, time_login, status) VALUES ( %s, %s, %s, %s) """
        mySql_insert_query = """INSERT INTO emergency_log (personid, date, time, activity, locker, status)VALUES ( %s, %s, %s, %s, %s, %s ) """

        record = (user_id['user_id'], datetime.datetime.now().date(), datetime.datetime.now().time(), 'open', locker, 1)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record)
        connection.commit()      
    except mysql.connector.Error as e:
        print("Failed to update columns of table: {}".format(e))
        return False