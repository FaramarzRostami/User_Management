from tkinter import Frame, Label, Button, messagebox, Checkbutton, IntVar
from tkinter.ttk import Treeview
from BusinessLogicLayer.user_business_logic import UserBusinessLogic

class UserManagementFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.row_list = []
        self.user_business = UserBusinessLogic()
        self.main_view = main_view

        self.current_user = None
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.header_label = Label(self, text="User Management Form")
        self.header_label.grid(row=0, column=0, pady=10, padx=10)

        self.back_button = Button(self, text="Back", command=self.back)
        self.back_button.grid(row=1, column=0, pady=(0, 10), padx=20, sticky="w")

        self.active_button = Button(self, text="Active", command=self.active)
        self.active_button.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.deactive_button = Button(self, text="Deactive", command=self.deactive)
        self.deactive_button.grid(row=1, column=1, pady=(0, 10), padx=10, sticky="e")

        self.role_button = Button(self, text="Change role", command=self.role)
        self.role_button.grid(row=1, column=2, pady=(0, 10), padx=10, sticky="e")

        self.user_treeview = Treeview(self, columns=("firstname", "lastname", "username", "role", "status"))
        self.user_treeview.grid(row=2, column=0, columnspan=3, pady=(0, 10), padx=10, sticky="nsew")

        self.user_treeview.heading("#0", text="NO")
        self.user_treeview.heading("#1", text="First Name")
        self.user_treeview.heading("#2", text="Last Name")
        self.user_treeview.heading("#3", text="Username")
        self.user_treeview.heading("#4", text="Role")
        self.user_treeview.heading("#5", text="Status")


    def set_current_user(self, current_user):
        self.current_user = current_user

        result = self.user_business.get_user_list(current_user)

        self.get_user_list()

    def load_data(self, user_list):
        for row in self.row_list:
            self.user_treeview.delete(row)

        self.row_list.clear()

        row_number = 1
        for user in user_list:
            row = self.user_treeview.insert("", "end", iid=user.id, text=str(row_number),
                                            values=(
                                                user.first_name, user.last_name, user.username, user.show_role_title(),
                                                "Active" if user.is_active else "Deactive"))

            self.row_list.append(row)
            row_number += 1

    def active(self):
        active_user_list = self.user_treeview.selection()

        self.user_business.active_user(self.current_user, active_user_list)

        self.get_user_list()

    def deactive(self):
        deactive_user_list = self.user_treeview.selection()

        self.user_business.deactive_user(self.current_user, deactive_user_list)

        self.get_user_list()

    def role(self):
        role_user_list = self.user_treeview.selection()
        user_list=self.user_business.get_user_list(self.current_user)
        cnt=0
        for row in self.row_list:
            # if str(user_list.data[cnt].id)==role_user_list:
            if row == role_user_list[0]:
                self.user_business.role_user(self.current_user, role_user_list,user_list.data[cnt].role_id)# role_user_list[0])
            cnt+=1

        self.get_user_list()

    def get_user_list(self):
        result = self.user_business.get_user_list(self.current_user)

        if result.success:
            self.load_data(result.data)
        else:
            messagebox.showerror("Error", result.message)

    def back(self):
        self.main_view.switch_frame("home")
