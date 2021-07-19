import config
import mysql.connector
from mysql.connector import Error

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

def insertproduct(section, qr_code, item_no, product_name, part_no, part_name,drawing_no, locker, quantity, other):

    try:
        print("a")
        connection = mysqlconnect()
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO products (section, qr_code, item_no, product_name, part_no, part_name, drawing_no, locker, quantity, other) 
                                                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        record = (section, qr_code, item_no, product_name, part_no, part_name, drawing_no, locker, quantity, other)
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


insertproduct("AS1", "1001", "ITEM0001", "MOLAA", "P001", "PART","DRAW", "L1", 1, "AASA")