from tkinter import Frame, Label, Entry, Button, messagebox#, Checkbutton, IntVar
from BusinessLogicLayer.user_business_logic import UserBusinessLogic

class RegisterFrame(Frame):
    def __init__(self, window, main_view):
        super().__init__(window)

        self.main_view = main_view
        self.user_business_logic = UserBusinessLogic()
        # self.set_current_user = set_current_user()

        self.grid_columnconfigure(1, weight=1)

        self.title_label = Label(self, text="Register Form")
        self.title_label.grid(row=0, column=1, pady=10, sticky="w")

        self.firstname_label = Label(self, text="First Name")
        self.firstname_label.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="e")

        self.firstname_entry = Entry(self)
        self.firstname_entry.grid(row=1, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.lastname_label = Label(self, text="Last Name")
        self.lastname_label.grid(row=2, column=0, pady=(0, 10), padx=10, sticky="e")

        self.lastname_entry = Entry(self)
        self.lastname_entry.grid(row=2, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.username_label = Label(self, text="Username")
        self.username_label.grid(row=3, column=0, pady=(0, 10), padx=10, sticky="e")

        self.username_entry = Entry(self)
        # self.username_entry.insert(0, "Nafiseh1")
        self.username_entry.grid(row=3, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        self.password_label = Label(self, text="Password")
        self.password_label.grid(row=4, column=0, pady=(0, 10), padx=10, sticky="e")

        self.password_entry = Entry(self, show="*")
        # self.password_entry.insert(0, "111")
        self.password_entry.grid(row=4, column=1, pady=(0, 10), padx=(0, 20), sticky="ew")

        # self.var_role = IntVar()
        # self.var_role.set(0)
        # self.checkbutton = Checkbutton(self, text="Admin", variable=self.var_role)#,command=self.save_manager)
        # self.checkbutton.grid(row=5, column=1, pady=(0, 10), padx=(0, 20), sticky="w")

        self.back_button = Button(self, text="Back", command=self.back)
        self.back_button.grid(row=6, column=0, pady=(0, 10), padx=10, sticky="w")

        self.submit_button = Button(self, text="SUBMIT", command=self.submit)
        self.submit_button.grid(row=6, column=1, pady=(0, 10), padx=10, sticky="e")

    def submit(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        # role_check = self.var_role.get()
        self.user_business_logic.register(firstname, lastname, username, password,2)# 1 if role_check == 1 else 2)

        messagebox.showinfo("","Registered, You will be activated soon...")
        self.firstname_entry.delete(0, "end")
        self.lastname_entry.delete(0, "end")
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        # self.var_role.set(0)

    def back(self):
        self.main_view.switch_frame("login")

