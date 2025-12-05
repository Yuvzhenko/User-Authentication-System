import tkinter as tk
from tkinter import messagebox
import json
import os

class authentification():

    def __init__(self, root):
        self.tries=3
        self.root=root

        self.root.title("User Authentification Management System")
        self.root.geometry("600x400")

        self.filename="users.json"

        # load the users from the file
        self.users = self.load_users()

        #-------UI-------
        self.frame_left=tk.Frame(self.root)
        self.frame_left.pack(side=tk.LEFT, padx=20, pady=20)

        self.name=tk.Label(self.frame_left, text="User Name:")
        self.name.grid(row=0, column=0, sticky="w")
        self.nameIn=tk.Entry(self.frame_left)
        self.nameIn.grid(row=0, column=1, pady=5)

        self.code=tk.Label(self.frame_left, text="Password:")
        self.code.grid(row=1, column=0, sticky="w")
        self.codeIn=tk.Entry(self.frame_left, show="*")
        self.codeIn.grid(row=1, column=1, pady=5)

        # Sign in button
        self.sign_in_button=tk.Button(self.frame_left, text="Sign In", command=self.sign_in, bg="#ddd", width=10)
        self.sign_in_button.grid(row = 2 ,column=0, pady=15, padx=5)

        # Registration button
        self.registration_button = tk.Button(self.frame_left, text="Register", command=self.register, bg="#ddd", width=10)
        self.registration_button.grid(row=2, column=1, pady=15, padx=5)

        self.status=tk.Label(self.frame_left, text="", fg="red", font=("Arial", 8))
        self.status.grid(row=3, column=0, columnspan=2)

        self.frame_right = tk.Frame(self.root)
        self.frame_right.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.list=tk.Listbox(self.frame_right, bg="sky blue", font=("Arial", 12))
        self.list.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(self.frame_right, orient="vertical", command=self.list.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")
        self.list.config(yscrollcommand=scrollbar.set)

        self.log_message("System ready. Please login or register")

    def sign_in(self):
        userName=self.nameIn.get()
        userCode=self.codeIn.get()

        signedIn=False
        for i in self.users:
            if userName == i["Name"] and userCode == i["Code"]:
                #self.list.insert(tk.END, f"Welcome {userName}")
                self.log_message(f"Success: Welcome back, {userName}!", color="green")
                messagebox.showinfo("Success", f"Welcome {userName}")
                signedIn=True
                self.tries = 3
                self.status.config(text="")
                self.clear()
                break
            

        if not signedIn:
            self.tries -= 1
            self.log_message(f"Failed attempt for user: {userName}", color="red")
            self.clear()

            if self.tries > 0:
                self.status.config(text="Incorrect username or password. Try again")
            else:
                self.block_access()
    
    def register(self):
        new_name = self.nameIn.get()
        new_code = self.codeIn.get()

        # checking if the fields is not empty
        if not new_name or not new_code:
            messagebox.showerror("Error", "The fields cannot be empty")
            return
        
        # checking if the name is not in use
        for i in self.users:
            if i["Name"] == new_name:
                messagebox.showerror("Error", "User with such name already exists")
                return
        
        # adding the new user 
        new_user_data = {"Name":new_name, "Code":new_code}
        self.users.append(new_user_data)

        self.save_user()

        self.log_message(f"New user registered: {new_name}", "green")
        messagebox.showinfo("Success", "Registration successful!")
        self.clear()
        self.tries = 3

        self.unblock_access()

    def block_access(self):
        self.sign_in_button.config(state=tk.DISABLED)
        self.status.config(text="Too many incorrect attempts. Please try again later")

    def unblock_access(self):
        self.sign_in_button.config(state=tk.ACTIVE)
        self.status.config(text="")
    
    def log_message(self, message, color="black"):
        self.list.insert(tk.END, message)
        self.list.itemconfig(tk.END, {'fg': color})
        self.list.see(tk.END)
        
    def clear(self):
        self.nameIn.delete(0, tk.END)
        self.codeIn.delete(0, tk.END)

    def save_user(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.users, file, indent=4)

    def load_users(self):
        if not os.path.exists(self.filename):
            return[]
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return[]

if __name__ == "__main__":
    root = tk.Tk()
    obj=authentification(root)
    root.mainloop()