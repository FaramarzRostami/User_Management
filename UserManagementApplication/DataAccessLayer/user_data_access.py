import sqlite3
from Common.Entities.user import User
from Common.Entities.role import  Role
from DataAccessLayer import database_name


class UserDataAccess:
    def get_user_with_username_password(self, username, password):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   password,
                   role_id,
                   is_active
            FROM   User
            Where  username = ?
            AND    password = ?""", (username, password))

            data = cursor.fetchone()

            if data:
                # user = User(data[0], data[1], data[2], data[3], None)
                user = User(*data)
                user.password = None

                return user

    def register_user(self, firstname,lastname,username, password,role_id):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(f"""
            INSERT INTO User (
                     first_name,
                     last_name,
                     username,
                     password,
                     role_id,
                     is_active
                 )
                 VALUES (
                     '{firstname}',
                     '{lastname}',
                     '{username}',
                     '{password}',
                     {role_id},
                     0
                 )""")

            connection.commit()

    def get_user_list(self, user_id):
        user_list = []
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT id,
                   first_name,
                   last_name,
                   username,
                   password,
                   role_id,
                   is_active
            FROM   User
            Where  id   !=  ?""", (user_id,))

            data = cursor.fetchall()

            for item in data:
                user = User(*item)
                user.password = None
                user_list.append(user)

        return user_list

    def get_role_list(self):
        role_list = []
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            SELECT id,
                   title
            FROM   Role""")

            data = cursor.fetchall()

            for item in data:
                role = Role(*item)
                role_list.append(role)

        return role_list

    def update_is_active(self, user_id, new_value):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            Update  User
            Set     is_active   =   ?
            Where   id          =   ?""", (new_value, user_id))

            connection.commit()

    def update_role(self, user_id, new_value):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            Update  User
            Set     role_id   =   ?
            Where   id          =   ?""", (new_value, user_id))

            connection.commit()

    def update_is_manager(self, user_id, new_value):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            Update  User
            Set     role_id   =   ?
            Where   id          =   ?""", (new_value, user_id))

            connection.commit()
