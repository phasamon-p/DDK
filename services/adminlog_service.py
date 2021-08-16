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

def get_adminlog():
    try:
        connection = mysqlconnect()

        mySql_select_query = "select * from admin_log"

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

        mySql_select_query = "select * from admin_log"

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

def getadminlog_bydate(date):
    try:
        connection = mysqlconnect()
        print("date ", date)
        mySql_select_query = "select * from admin_log WHERE date= %s"

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

def insert_adminlog(admin):
    try:
        connection = mysqlconnect()
        mySql_insert_query = """INSERT INTO admin_log (adminid, date_login, time_login, status) VALUES ( %s, %s, %s, %s) """
        record = (admin['admin_id'], datetime.datetime.now().date(), datetime.datetime.now().time(), 1)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        views.admin_data.adminlog_id = getlast_idlog()
        print("admin last id ",views.admin_data.adminlog_id)
            
    except mysql.connector.Error as e:
        print("Failed to update columns of table: {}".format(e))
        return False

def update_adminlog_logout():
        try:
            connection = mysqlconnect()
            cursor = connection.cursor()
            sql_Update_Query = "UPDATE admin_log set date_logout = %s, time_logout = %s where id = %s"
            input = (datetime.datetime.now().date(), datetime.datetime.now().time(), views.admin_data.adminlog_id)
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
