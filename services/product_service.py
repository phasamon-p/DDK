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
def insertproduct(data):
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO products (section, qr_code, item_no, product_name, part_no, part_name, drawing_no, locker, quantity, other, status) 
                                                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
        qrcode = data[1].replace("\r", "")
        record = (data[0], qrcode, data[2], data[3], data[4], data[5], data[6], '', data[8], data[9], 1)
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

def getproductlocker(qrcode):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM products_lockers WHERE pl_products = %s "
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (qrcode.replace("\r", ""),))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount

        if cursor.rowcount:
            return [True, records,rowcount]
            print(records)

        else:
            return [False, records,rowcount]
            print(records)

    except mysql.connector.Error as error:
        print("Failed e record: ", error)
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def qrcode_check(qrcode):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT qr_code FROM products WHERE qr_code = %s "
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (qrcode.replace("\r", ""),))
        # get all records
        records = cursor.fetchall()


        if cursor.rowcount:
            return records
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

def getproductlocker2(qrcode):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM products_lockers WHERE pl_products = %s "
        cursor = connection.cursor()
        print(qrcode.replace("\r", ""))
        cursor.execute(sql_select_Query, (qrcode.replace("\r", ""),))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount
        print(records)

        if cursor.rowcount:
            return records[0][2]
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

def getproduct_drawer(qrcode):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM products_lockers WHERE pl_products = %s "
        cursor = connection.cursor()
        print(qrcode.replace("\r", ""))
        cursor.execute(sql_select_Query, (qrcode.replace("\r", ""),))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount
        if cursor.rowcount:
            return records[0]
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

def getproductlocker_string(qrcode):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM products_lockers WHERE pl_products = %s "
        cursor = connection.cursor()
        # print(qrcode.replace("\r", ""))
        cursor.execute(sql_select_Query, (qrcode.replace("\r", ""),))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount

        if cursor.rowcount:
            data = ''
            for x in range(len(records)):
                if len(data) > 0:
                    data += "," + str(records[x][2])
                else:
                    data += str(records[x][2])
            return data
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

def getsection_bool(qrcode):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM products WHERE qr_code = %s "
        cursor = connection.cursor()
        print(qrcode.replace("\r", ""))
        cursor.execute(sql_select_Query, (qrcode.replace("\r", ""),))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount

        if cursor.rowcount:
            data = records[0][1].split()
            section = [False, False, False, False, False]
            for x in range(len(data)):
                if data[x] == 'AS1':
                   section[0] = True
                if data[x] == 'AS2':
                   section[1] = True
                if data[x] == 'MT1':
                   section[2] = True
                if data[x] == 'MT2':
                   section[3] = True
                if data[x] == 'PR':
                   section[4] = True
            return section
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

def getproductlockerbylocker(barcode, locker):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM products_lockers WHERE pl_products = %s and pl_locker = %s "
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (barcode, locker))
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

def getquantity_byqrcode(qrcode):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT quantity FROM products WHERE qr_code = %s"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (qrcode,))
        # get all records
        records = cursor.fetchall()
        if cursor.rowcount:
            return records[0][0]
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

def getproductlocker_byqrcode_bool(barcode):
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM products_lockers WHERE pl_products = %s "
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (barcode.replace("\r",""),))
        # get all records
        records = cursor.fetchall()
        print(records)
        if cursor.rowcount:
            if config.locker_type > 0:
                locker = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
            else:
                locker = [False, False, False, False, False, False, False, False, False, False, False, False]
            
            for x in range(len(records)):
                locker[records[x][2] - 1] = True

            return locker
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

def insertproductlocker(qrcode, permission, drawer, cavity):
    try:
        # print("permission:", permission)
        # print("drawer:", drawer)
        # print("cavity:", cavity)
        connection = mysqlconnect()
        cursor = connection.cursor()
        for x in range(len(permission)):
#             print("lengh of ml_locker :", len(permission))
            if permission[x]:
                if not getproductlockerbylocker(qrcode.replace("\r", ""), x + 1):
                    mySql_insert_query = """INSERT INTO products_lockers (pl_products, pl_locker, pl_drawer, pl_cavity, status) VALUES ( %s, %s, %s, %s, %s) """
                    record = (qrcode.replace("\r", ""), x + 1, int(drawer), int(cavity), 1)
                    cursor.execute(mySql_insert_query, record)
                    connection.commit()
                else:
                    print("update")
                    sql_Update_Query = "UPDATE products_lockers set pl_products = %s, pl_locker = %s , pl_drawer = %s, pl_cavity = %s, status = %s where pl_products = %s and pl_locker = %s"
                    # mySql_insert_query = """INSERT INTO products_lockers (pl_products, pl_locker, pl_drawer, pl_cavity, status) VALUES ( %s, %s, %s, %s, %s) """
                    record = (qrcode.replace("\r", ""), x + 1, int(drawer), int(cavity), 1, qrcode.replace("\r", ""), x + 1)
                    cursor.execute(sql_Update_Query, record)
                    connection.commit()
#                     print("Insert ml_locker : ", record)
            else:
                mySql_delete_query = "DELETE from products_lockers where pl_products = %s and pl_locker = %s "
                record = (qrcode.replace("\r", ""), x + 1)
                cursor.execute(mySql_delete_query, record)
                connection.commit()
#                 print("Delete ml_locker : ", record)
        return True

    except mysql.connector.Error as error:
        print("Failed e record: ", error)
        return False

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed ")

def deleteproductlockerbybarcode(barcode):
    try:
        connection = mysqlconnect()

        sql_Delete_Query = "Delete from products_lockers where pl_products = %s "
        cursor = connection.cursor()
        cursor.execute(sql_Delete_Query, (barcode.replace("\r",""),))
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

def selectproduct():
    try:
        connection = mysqlconnect()

        sql_select_Query = "select * from products"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        # get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)

        print("\nPrinting each row")
        rowcount = cursor.rowcount
        print(rowcount)
        return records

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def selectproductbybarcode(qrcode):
    try:
        connection = mysqlconnect()

        sql_select_Query = "SELECT * FROM products WHERE qr_code = %s "

        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (qrcode,))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount
        print("Total number of rows in table: ", cursor.rowcount)

        if cursor.rowcount:
            return [True, [records]]
        else:
            return [False, [records]]

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def selectproductbysearch(search): ##
    print(str(search))
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM products WHERE qr_code LIKE %s " 
        
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, ("%" + search + "%",))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount
        print("Total number of rows in table: ", cursor.rowcount)

        if cursor.rowcount:
            return [True, [records]]
        else:
            return [False, [records]]

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def selectproductbysearch_2(search): ##
    print(str(search))
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM products WHERE section = %s " \
                           "OR qr_code = %s " \
                           "OR item_no = %s " \
                           "OR product_name = %s " \
                           "OR part_no = %s " \
                           "OR part_name = %s " \
                           "OR drawing_no = %s"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, (search,search,search,search,search,search,search,))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount
        print("Total number of rows in table: ", cursor.rowcount)

        if cursor.rowcount:
            return records
        else:
            return False

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def selectproductbysearch_like(search): ##
    print(str(search))
    try:
        connection = mysqlconnect()
        sql_select_Query = "SELECT * FROM products WHERE section LIKE %s " \
                           "OR qr_code LIKE %s " \
                           "OR item_no LIKE %s " \
                           "OR product_name LIKE %s " \
                           "OR part_no LIKE %s " \
                           "OR part_name LIKE %s " \
                           "OR drawing_no LIKE %s"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query, ("%" + search + "%","%" + search + "%","%" + search + "%","%" + search + "%","%" + search + "%","%" + search + "%","%" + search + "%",))
        # get all records
        records = cursor.fetchall()
        rowcount = cursor.rowcount
        print("Total number of rows in table: ", cursor.rowcount)

        if cursor.rowcount:
            return records
        else:
            return False

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

# def updateproductbyid(id, section, qr_code, item_no, product_name, part_no, part_name,drawing_no, locker, quantity, other):
def updateproductbyid(qrcode, data):
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()
        # sql_Update_Query = "UPDATE products set section = %s, qr_code = %s , item_no = %s, product_name = %s, " \
        #                    "part_no = %s, part_name = %s,drawing_no = %s, locker = %s, quantity = %s, " \
        #                    "other = %s where qr_code = %s "
        # input = (data[0], data[1].replace("\r", ""), data[2], data[3], data[4], data[5], data[6],'', data[8], data[9] ,qrcode.replace("\r", ""))
        print(data, qrcode)
        sql_Update_Query = "UPDATE products set section = %s, qr_code = %s , item_no = %s, product_name = %s, " \
                           "part_no = %s, part_name = %s,drawing_no = %s, locker = %s, quantity = %s, " \
                           "other = %s, status = %s where qr_code = %s "
        input = (data[0], data[1].replace("\r", ""), data[2], data[3], data[4], data[5], data[6],'', data[8], data[9], 2,qrcode.replace("\r", ""))

        print(cursor.execute(sql_Update_Query, input))
        connection.commit()
        print("Multiple columns updated successfully ")
        return True

    except mysql.connector.Error as e:
        print("Failed to update columns of table: {}".format(e))
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def updatequantity_byqrcode(data):
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()
        for x in range(len(data)):
            old_quantity = getquantity_byqrcode(data[x].qrcode)
            value = old_quantity - int(data[x].quantity)
            sql_Update_Query = "UPDATE products set quantity = %s where qr_code = %s"
            input = (value, data[x].qrcode.replace("\r",""))
            cursor.execute(sql_Update_Query, input)
            connection.commit()

        print("Multiple columns updated successfully ")
        return True

    except mysql.connector.Error as e:
        print("Failed to update columns of table: {}".format(e))
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def updateinventory_byqrcode(qrcode, data):
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()    
        sql_Update_Query = "UPDATE products set quantity = %s where qr_code = %s"
        input = (int(data), qrcode.replace("\r",""))
        cursor.execute(sql_Update_Query, input)
        connection.commit()
        print("Multiple columns updated successfully ")
        return True

    except mysql.connector.Error as e:
        print("Failed to update columns of table: {}".format(e))
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

def deleteproductbyid(id):
    try:
        connection = mysqlconnect()
        sql_Delete_Query = "Delete from products where id = %s "
        cursor = connection.cursor()
        cursor.execute(sql_Delete_Query, (id,))
        connection.commit()
        return True

    except mysql.connector.Error:
        return False
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")