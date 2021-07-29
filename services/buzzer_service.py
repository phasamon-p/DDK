import config
import mysql.connector
from mysql.connector import Error

########################################### ABOUT CONECTION ########################################### 
def mysqlconnect():
    try:
        return mysql.connector.connect(host = config.db["host"], database = config.db["database"], user = config.db["user"], password = config.db["password"])
        # if connection.is_connected():
        #     db_Info = connection.get_server_info()
        #     print("Connected to MySQL Server version ", db_Info)
        #     cursor = connection.cursor()
        #     cursor.execute("select database();")
        #     record = cursor.fetchone()
        #     print("You're connected to database: ", record)
            
    except Error as e:
        return e

# def insertproduct(section, qr_code, item_no, product_name, part_no, part_name,drawing_no, locker, quantity, other):
def insertbuzzer():
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO locker_count (id, count) VALUES (%s, %s) """
        record = (2, 0)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        return True

    except mysql.connector.Error as e:

        print("Error reading data from MySQL table", e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def updatebuzzer(data):
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()
        mySql_insert_query = "UPDATE locker_count set count = %s, status = %s where id = 2"
        cursor.execute(mySql_insert_query, (data, 2,))
        connection.commit()
        return True

    except mysql.connector.Error as e:

        print("Error reading data from MySQL table", e)

    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def getbuzzer():
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM locker_count WHERE id = 2 "
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        if cursor.rowcount:
            return records[0][1]
        else:
            return False

    except mysql.connector.Error as error:
        print("Failed e record: ", error)
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")

