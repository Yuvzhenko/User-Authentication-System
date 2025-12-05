import tkinter as tk
from tkinter import messagebox

class authentification():

    def __init__(self, root):

        self.users=[
            {"Name":"david","Code":"1234"},
            {"Name":"max","Code":"4321"},
            {"Name":"john","Code":"0000"}
        ]
        self.tries=3
        self.root=root

        self.root.title("User Authentification Management System")

        self.frame1=tk.Frame(self.root, width=30, height=50)
        self.frame1.pack(side=tk.LEFT)

        self.frame2 = tk.Frame(self.root, width=50, height=30)
        self.frame2.pack(side=tk.RIGHT)

        self.name=tk.Label(self.frame1, text="User Name:")
        self.name.pack(side=tk.TOP, padx=10, pady=5)
        self.nameIn=tk.Entry(self.frame1)
        self.nameIn.pack(side=tk.TOP, pady=5, padx=10)

        self.code=tk.Label(self.frame1, text="Password:")
        self.code.pack(side=tk.TOP, pady=10, padx=10)
        self.codeIn=tk.Entry(self.frame1)
        self.codeIn.pack(side=tk.TOP, pady=10, padx=10)

        self.button=tk.Button(self.frame1, text="Sign In", command=self.signIn)
        self.button.pack(side=tk.TOP, padx=10, pady=15)

        self.list=tk.Listbox(self.frame2, bg="sky blue", font=("Arial Black", 15), width=60, height=30)
        self.list.pack(side=tk.RIGHT)
        

    def signIn(self):
        userName=self.nameIn.get()
        userCode=self.codeIn.get()

        signedIn=False
        for i in self.users:
            if userName == i["Name"] and userCode == i["Code"]:
                self.list.insert(tk.END, f"Welcome {userName}")
                signedIn=True
                self.clear()
                break
            

        if not signedIn:
            self.tries -= 1
            if self.tries > 0:
                self.list.insert(tk.END, "Incorrect username or password. Try again")
                self.clear()
            else:
                tk.messagebox.showerror("Block", "Too many incorrect attempts. Please try again later")
        else:
            self.tries = 3
        
    def clear(self):
        self.nameIn.delete(0, tk.END)
        self.codeIn.delete(0, tk.END)


root = tk.Tk()
obj=authentification(root)
root.mainloop()