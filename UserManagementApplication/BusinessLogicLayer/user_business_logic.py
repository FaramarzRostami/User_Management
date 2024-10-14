import hashlib
from Common.ResponseModels.response import Response
from DataAccessLayer.user_data_access import UserDataAccess

class UserBusinessLogic:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def login(self, username, password):
        if len(username) < 3 or len(password) < 3:
            return Response(False, "Invalid request.", None)

        password_hash = hashlib.md5(password.encode()).hexdigest()

        user = self.user_data_access.get_user_with_username_password(username, password_hash)

        if not user:
            return Response(False, "Invalid username or password.", None)
        else:
            if user.is_active:
                return Response(True, None, user)
            else:
                return Response(False, "Your account is deactive.", None)

    def register(self, firstname, lastname, username, password,role_id):
        if len(username) < 3 or len(password) < 3 or len(firstname) == 0 or len(lastname) == 0:
            return Response(False, "Invalid information.", None)

        password_hash = hashlib.md5(password.encode()).hexdigest()

        self.user_data_access.register_user(firstname, lastname, username, password_hash,role_id)
        return True

    def get_user_list(self, current_user):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access Denied.", None)

        user_list = self.user_data_access.get_user_list(current_user.id)

        return Response(True, None, user_list)

    def get_role_list(self):
        role_list = self.user_data_access.get_role_list()

        return role_list

    def active_user(self, current_user, user_list):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access Denied.", None)

        for user_id in user_list:
            self.user_data_access.update_is_active(user_id, 1)

    def deactive_user(self, current_user, user_list):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access Denied.", None)

        for user_id in user_list:
            self.user_data_access.update_is_active(user_id, 0)

    def role_user(self, current_user, user_list,role_user_id):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access Denied.", None)

        for user_id in user_list:
            self.user_data_access.update_role(user_id, 2 if role_user_id==1 else 1)

    def manager_user(self, current_user, user_list,choice):
        if not current_user.is_active:
            return Response(False, "Your account is deactive.", None)

        if current_user.show_role_title() != "Admin":
            return Response(False, "Access Denied.", None)

        for user_id in user_list:
            self.user_data_access.update_is_manager(user_id, choice)
