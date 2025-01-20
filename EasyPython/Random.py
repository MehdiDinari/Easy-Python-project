import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu de Devinette")
        self.master.geometry("400x300")
        self.master.configure(bg="#f0f0f0")

        self.numero = random.randint(1, 100)

        self.title_label = tk.Label(master, text="Devinez le numéro!", font=("Helvetica", 16), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.instruction_label = tk.Label(master, text="Entrez un nombre entre 1 et 100:", font=("Helvetica", 12), bg="#f0f0f0")
        self.instruction_label.pack()

        self.entry = tk.Entry(master, font=("Helvetica", 14), width=10)
        self.entry.pack(pady=10)

        self.button = tk.Button(master, text="Deviner", command=self.check_guess, font=("Helvetica", 12), bg="#4CAF50", fg="white")
        self.button.pack(pady=10)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 12), bg="#f0f0f0")
        self.result_label.pack(pady=20)

        self.reset_button = tk.Button(master, text="Réinitialiser", command=self.reset_game, font=("Helvetica", 12), bg="#f44336", fg="white")
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess == self.numero:
                self.result_label.config(text=f"Bravo, la réponse était {self.numero}!", fg="green")
            elif guess > self.numero:
                self.result_label.config(text="Essayer plus petit.", fg="blue")
            else:
                self.result_label.config(text="Essayer plus grand.", fg="blue")
        except ValueError:
            self.result_label.config(text="Veuillez entrer un nombre valide.", fg="red")

    def reset_game(self):
        self.numero = random.randint(1, 100)
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()