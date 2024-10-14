class User:
    def __init__(self, id, firstname, lastname, username, password, role_id, is_active):
        self.id = id
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.password = password
        self.role_id = role_id
        # 0 => False
        # 1 => True
        self.is_active = bool(is_active)

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def show_role_title(self):
        match self.role_id:
            case 1:
                return "Admin"
            case 2:
                return "Default User"
            case _:
                raise ValueError("Invalid value for role id.")
