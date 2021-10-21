import config
import mysql.connector
from mysql.connector import Error
from views.admin.usermanagement.user_data import *
import time
import datetime
import services
import views

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

def get_requestlog():
    try:
        connection = mysqlconnect()

        mySql_select_query = "select * from request_log"

        cursor = connection.cursor()
        cursor.execute(mySql_select_query)
        # get all records
        records = cursor.fetchall()
        date = records[0][1]
        day = date.day
        print("log ", records[0][1])
        print("day ", day)

        for row in records:
            print(row)
        return

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def getlast_idlog():
    try:
        connection = mysqlconnect()

        mySql_select_query = "select * from request_log"

        cursor = connection.cursor()
        cursor.execute(mySql_select_query)
        # get all records
        records = cursor.fetchall()

        return records[len(records) - 1][0]

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def getrequestlog_bydate(date):
    try:
        connection = mysqlconnect()
        print("date ", date)
        mySql_select_query = "select * from request_log WHERE date= %s"

        cursor = connection.cursor()
        cursor.execute(mySql_select_query, (date,))
        # get all records
        records = cursor.fetchall()
        return records

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def insert_requestlog(employee,product):
    try:
        connection = mysqlconnect()
        mySql_insert_query = """INSERT INTO request_log (date, time, personid, qrcode, request, recheck, activity, status) 
                                                       VALUES ( %s, %s, %s, %s, %s, %s, %s, %s) """
        for x in range(len(product)):
            record = (datetime.datetime.now().date(), datetime.datetime.now().time(), employee['requester_id'], product[x].qrcode, product[x].quantity, "False", "request", 1)
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            views.request_data.list_idcheck_add(getlast_idlog())
            
    except mysql.connector.Error as e:
        print("Failed to update columns of table: {}".format(e))
        return False

def update_requestlog_check():
        try:
            connection = mysqlconnect()
            cursor = connection.cursor()
            for x in range(len(views.request_data.request_list2_check)):
                if views.request_data.request_list2_check[x]:
                    sql_Update_Query = "UPDATE request_log set recheck = %s where id = %s"
                    input = ("True", views.request_data.request_list2_idcheck[x])
                    cursor.execute(sql_Update_Query, input)
                    connection.commit()
            return True

        except mysql.connector.Error as e:
            print("Failed to update columns of table: {}".format(e))
            return False
        finally:
            if connection.is_connected():
                connection.close()
                cursor.close()
                print("MySQL connection is closed")

def insert_emergency_requestlog(employee,product):
    try:
        connection = mysqlconnect()
        mySql_insert_query = """INSERT INTO request_log (date, time, personid, qrcode, request, recheck, activity, status) 
                                                       VALUES ( %s, %s, %s, %s, %s, %s, %s, %s) """
        for x in range(len(product)):
            record = (datetime.datetime.now().date(), datetime.datetime.now().time(), employee['requester_id'], product[x].qrcode, product[x].quantity, "False", "emergency", 1)
            cursor = connection.cursor()
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            views.request_data.list_idcheck_add(getlast_idlog())
            
    except mysql.connector.Error as e:
        print("Failed to update columns of table: {}".format(e))
        return False