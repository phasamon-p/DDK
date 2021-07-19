import config
import mysql.connector
from mysql.connector import Error
from views.admin.usermanagement.user_data import *

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

########################################### ABOUT PERMISSION ###########################################

def getpermission(id):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM person_locker WHERE pl_person = %s "
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (id,))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount

        if cursor.rowcount:
            return [True, records,rowcount]
        else:
            return [False, records,rowcount]

    except mysql.connector.Error as error:
        print("Failed e record: ", error)
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            #print(records)
            print("MySQL connection is closed")


def getpermissionbylocker(id, locker):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM person_locker WHERE pl_person = %s and pl_locker = %s"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (id, locker))
        # get all records
        records = cursor.fetchall()

        print("rowcount :", cursor.rowcount)
        if cursor.rowcount:
            return True
        else:
            return False

    except mysql.connector.Error as error:
        print("Failed e record: ", error)
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def checkpermission(person, medical):
    try:
        # print("person:", person)
        # print("medical:", medical)
        for x in range(len(medical)):
            result = getmedicallocker2(medical[x][3])
            if not getpermissionbylocker(person, result):
                return False

        return True

    except Error as error:
        print("Failed e record: ", error)
        return False

def insertpermission(id, permission):
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()
        for x in range(len(permission)):
            print("lengh of permission :", len(permission))
            if permission[x]:
                if not getpermissionbylocker(id, permission[x]):
                    mySql_insert_query = """INSERT INTO person_locker (pl_person, pl_locker) VALUES ( %s, %s) """
                    record = (id, permission[x])
                    cursor.execute(mySql_insert_query, record)
                    connection.commit()
                    print("Insert permission : ", record)
            else:
                mySql_delete_query = "DELETE from person_locker where pl_person = %s and pl_locker = %s "
                record = (id, x+1)
                cursor.execute(mySql_delete_query, record)
                connection.commit()
                print("Delete permission : ", record)
        return True

    except mysql.connector.Error as error:
        print("Failed e record: ", error)
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
#getpermission("DDK01")

def deletepermissionbyid(id):
    try:
        connection = mysqlconnect()

        sql_Delete_Query = "Delete from person_locker where pl_person = %s "
        cursor = connection.cursor()
        cursor.execute(sql_Delete_Query, (id,))
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

##insertpermission("DDK01",[1])
#deletepermissionbyid("DDK01")

