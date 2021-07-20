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


def selectperson():
    try:
        connection = mysqlconnect()

        sql_Select_Query = "select * from person"
        cursor = connection.cursor()
        cursor.execute(sql_Select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        rowcount = cursor.rowcount
        return [records, rowcount]

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


def selectpersonbyid(id):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM person WHERE personid = %s "
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (id,))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount
        print("Total number of rows in table: ", cursor.rowcount)

        if cursor.rowcount:
            return [True, records, rowcount]
        else:
            return [False, records, rowcount]

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


def getpersonbyfingerid(fingerid):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM person WHERE fingerid = %s "
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (fingerid,))
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        if cursor.rowcount:
            return [True, records]
        else:
            return [False, records]

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


def getpersoncount():
    try:
        connection = mysqlconnect()

        sql_Select_Query = "select * from person"
        cursor = connection.cursor()
        cursor.execute(sql_Select_Query)
        # get all records
        print("Total number of rows in table: ", cursor.rowcount)
        rowcount = cursor.rowcount
        return rowcount

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")


def getpersonbyid(id):
    try:
        connection = mysqlconnect()

        sql_select_Query = "SELECT * FROM person WHERE personid = %s "

        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (id,))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount
        print("Total number of rows in table: ", cursor.rowcount)

        if cursor.rowcount:
            return [True, [records, rowcount]]
        else:
            return [False, [records, rowcount]]

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def insertperson(personid, name, lname, department, fingerid, role):
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO person (personid, name, lname, department ,fingerid, permission) VALUES ( %s, %s, %s, %s, %s, %s) """
        permission = role
        record = (personid, name, lname, department, fingerid, permission)
        cursor.execute(mySql_insert_query, record)
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


def updatepersonbyid(id, name, lname, department, fingerid, role):
    try:
        connection = mysqlconnect()

        sql_Update_Query = "UPDATE person set personid = %s, name = %s, lname = %s, department = %s, fingerid = %s, permission = %s where personid = %s "
        cursor = connection.cursor()
        # print(" role:", role)
        record = (id, name, lname, department, fingerid, role, id)

        cursor.execute(sql_Update_Query, record)
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


def deletepersonbyid(id):
    try:
        connection = mysqlconnect()

        sql_Delete_Query = "Delete from person where personid = %s "
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
