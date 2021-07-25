from views.admin.system_managment import System_Management
from views.admin.usermanagement import User_Management, User_Id, user_data, User_Name, User_Lname, User_Department, User_Permission, User_Lockeraccess, User_Finger, User_Result, User_Edit
from views.admin.productmanagement import Product_Management, Item_Number, product_data, Product_Name, Part_Number, Part_Name, Drawing_Number, Product_Locker, Quantity, Other, Product_Result, Product_Section, Product_Qrcode, Product_Edit, Inventory_Edit
from views.admin.lockermanagement import Locker_Control, locker_data, Locker_Control2, Locker_Management, Buzzer_Setting
from views.admin.admin_finger import Admin_Finger
import views.admin.admin_data as admin_data


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
            'Buzzer_Setting',
            'admin_data',
            'Product_Edit',
            'User_Edit',
            'Admin_Finger',
            'Inventory_Edit'}