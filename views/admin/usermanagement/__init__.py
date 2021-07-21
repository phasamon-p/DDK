from views.admin.usermanagement.user_managment import User_Management
from views.admin.usermanagement.user_id import User_Id
from views.admin.usermanagement.user_name import User_Name
import views.admin.usermanagement.user_data as user_data
from views.admin.usermanagement.user_lname import User_Lname
from views.admin.usermanagement.user_deparment import User_Department
from views.admin.usermanagement.user_permission import User_Permission
from views.admin.usermanagement.user_lockeraccess import User_Lockeraccess
from views.admin.usermanagement.user_finger import User_Finger
from views.admin.usermanagement.user_result import User_Result
from views.admin.usermanagement.user_edit import User_Edit

__all__ = { 'User_Management',
            'User_Id',
            'user_data',
            'User_Name',
            'User_Lname',
            'User_Department',
            'User_Permission',
            'User_Lockeraccess',
            'User_Finger',
            'User_Result',
            'User_Edit'}