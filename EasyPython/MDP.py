import tkinter as tk
from tkinter import messagebox
import os
import hashlib


class UserManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Gestion des utilisateurs")
        self.master.geometry("400x300")

        self.users = self.load_users()

        # Conteneur pour les pages
        self.container = tk.Frame(self.master)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        self.show_frame("LoginPage")

    def load_users(self):
        """Charge les utilisateurs à partir du fichier users.txt."""
        if not os.path.exists("users.txt"):
            return {}

        users = {}
        with open("users.txt", "r") as file:
            for line in file:
                username, password_hash = line.strip().split("|")
                users[username] = password_hash
        return users

    def save_users(self):
        """Sauvegarde les utilisateurs dans le fichier users.txt."""
        with open("users.txt", "w") as file:
            for username, password_hash in self.users.items():
                file.write(f"{username}|{password_hash}\n")

    def show_frame(self, page_name):
        """Affiche la frame spécifiée."""
        # Détruit la frame actuelle pour éviter les conflits
        for widget in self.container.winfo_children():
            widget.destroy()

        if page_name == "LoginPage":
            frame = LoginPage(parent=self.container, controller=self)
        elif page_name == "RegisterPage":
            frame = RegisterPage(parent=self.container, controller=self)

        self.frames[page_name] = frame
        frame.pack(fill="both", expand=True)


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Connexion", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self, text="Nom d'utilisateur").pack()
        self.user_var = tk.StringVar()
        self.user_entry = tk.Entry(self, textvariable=self.user_var)
        self.user_entry.pack()

        tk.Label(self, text="Mot de passe").pack()
        self.pass_var = tk.StringVar()
        self.pass_entry = tk.Entry(self, textvariable=self.pass_var, show='*')
        self.pass_entry.pack()

        tk.Button(self, text="Se connecter", command=self.login).pack(pady=10)
        tk.Button(self, text="Créer un compte", command=lambda: controller.show_frame("RegisterPage")).pack()

    def login(self):
        username = self.user_var.get()
        password = self.pass_var.get()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        if username in self.controller.users and self.controller.users[username] == hashed_password:
            messagebox.showinfo("Connexion réussie", f"Bienvenue, {username}!")
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, text="Inscription", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self, text="Nom d'utilisateur").pack()
        self.user_var = tk.StringVar()
        self.user_entry = tk.Entry(self, textvariable=self.user_var)
        self.user_entry.pack()

        tk.Label(self, text="Mot de passe").pack()
        self.pass_var = tk.StringVar()
        self.pass_entry = tk.Entry(self, textvariable=self.pass_var, show='*')
        self.pass_entry.pack()

        tk.Button(self, text="Créer un compte", command=self.register).pack(pady=10)
        tk.Button(self, text="Retour à la connexion", command=lambda: controller.show_frame("LoginPage")).pack()

    def register(self):
        username = self.user_var.get().strip()
        password = self.pass_var.get().strip()

        if not username or not password:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
            return

        if username in self.controller.users:
            messagebox.showerror("Erreur", "Nom d'utilisateur déjà pris")
        else:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            self.controller.users[username] = hashed_password
            self.controller.save_users()
            messagebox.showinfo("Succès", "Compte créé avec succès")
            self.controller.show_frame("LoginPage")


if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagerApp(root)
    root.mainloop()
