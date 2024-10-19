from tkinter import Frame, Label, Button


class HomeFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.current_user=None
        self.main_view = main_view

        self.grid_columnconfigure(0, weight=1)

        self.welcome_label = Label(self)
        self.welcome_label.grid(row=0, column=0, pady=10)

        self.logout_button = Button(self, text="Logout", command=self.logout)
        self.logout_button.grid(row=1, column=0, pady=(0, 10), padx=20, sticky="ew")

        self.user_management_button = None

    def set_current_user(self, current_user):
        self.user_management_button = Button(self, text="User Management", command=self.go_to_user_management)
        self.current_user=current_user
        self.welcome_label.config(text=f"Welcome {current_user.get_fullname()}")
        if current_user.role_id==1:
            self.user_management_button = Button(self, text="User Management", command=self.go_to_user_management,state="normal")
            # if current_user.show_role_title() == "Admin":
            self.user_management_button.grid(row=2, column=0, pady=(0, 10), padx=20, sticky="ew")
        else:
            self.user_management_button = Button(self, text="User Management", command=self.go_to_user_management,state="disabled")
            self.user_management_button.grid(row=2, column=0, pady=(0, 10), padx=20, sticky="ew")

    def logout(self):
        self.main_view.switch_frame("login")

    def go_to_user_management(self):
       user_management_frame= self.main_view.switch_frame("user_management")
       user_management_frame.set_current_user(self.current_user)
