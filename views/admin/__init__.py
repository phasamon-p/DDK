from views.admin.system_managment import System_Management
from views.admin.usermanagement import User_Management, User_Id, user_data, User_Name, User_Lname, User_Department, User_Permission, User_Lockeraccess, User_Finger, User_Result
from views.admin.productmanagement import Product_Management, Item_Number, product_data, Product_Name, Part_Number, Part_Name, Drawing_Number, Product_Locker, Quantity, Other, Product_Result, Product_Section, Product_Qrcode
from views.admin.lockermanagement import Locker_Control, locker_data, Locker_Control2, Locker_Management, Buzzer_Setting

__all__ = { 'System_Management',
            'User_Management',
            'Product_Management',
            'User_Id',
            'user_data',
            'User_Name',
            'User_Lname',
            'User_Department',
            'User_Permission',
            'User_Lockeraccess',
            'User_Finger',
            'User_Result',
            'Item_Number',
            'product_data',
            'Product_Name',
            'Part_Number',
            'Part_Name',
            'Drawing_Number',
            'Product_Locker',
            'Quantity',
            'Other',
            'Product_Result',
            'Product_Section',
            'Product_Qrcode',
            'Locker_Control',
            'locker_data',
            'Locker_Control2',
            'Locker_Management',
            'Buzzer_Setting'}