import tkinter as tk
import random
from PIL import Image, ImageTk


class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Pierre-Papier-Ciseaux")
        self.master.geometry("400x400")
        self.master.configure(bg="#f0f0f0")

        self.choices = ("Paper", "Rock", "Scissors")
        self.Myscore = 0
        self.ComputerScore = 0

        self.title_label = tk.Label(master, text="Choisissez entre Pierre, Papier, Ciseaux", font=("Helvetica", 16),
                                    bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Helvetica", 14), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="Votre score: 0, Score de l'ordinateur: 0", font=("Helvetica", 12),
                                    bg="#f0f0f0")
        self.score_label.pack(pady=10)

        self.button_frame = tk.Frame(master, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        try:
            self.rock_image = Image.open("rock.png").resize((100, 100), Image.LANCZOS)
            self.paper_image = Image.open("paper.png").resize((100, 100), Image.LANCZOS)
            self.scissors_image = Image.open("scissors.png").resize((100, 100), Image.LANCZOS)

            self.rock_image = ImageTk.PhotoImage(self.rock_image)
            self.paper_image = ImageTk.PhotoImage(self.paper_image)
            self.scissors_image = ImageTk.PhotoImage(self.scissors_image)
        except FileNotFoundError as e:
            print(f"Erreur lors du chargement des images: {e}")
            self.master.quit()

        self.rock_button = tk.Button(self.button_frame, image=self.rock_image, command=lambda: self.play("Rock"),
                                     bg="#f0f0f0", borderwidth=0)
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.button_frame, image=self.paper_image, command=lambda: self.play("Paper"),
                                      bg="#f0f0f0", borderwidth=0)
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.button_frame, image=self.scissors_image,
                                         command=lambda: self.play("Scissors"), bg="#f0f0f0", borderwidth=0)
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.quit_button = tk.Button(master, text="Quitter", command=self.master.quit, font=("Helvetica", 12),
                                     bg="#f44336", fg="white")
        self.quit_button.pack(pady=20)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result_text = f"Ordinateur a choisi: {computer_choice}\n"

        if computer_choice == user_choice:
            result_text += "Match nul!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                (user_choice == "Paper" and computer_choice == "Rock") or \
                (user_choice == "Scissors" and computer_choice == "Paper"):
            result_text += "Vous gagnez!"
            self.Myscore += 1
        else:
            result_text += "Ordinateur gagne!"
            self.ComputerScore += 1

        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Votre score: {self.Myscore}, Score de l'ordinateur: {self.ComputerScore}")


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
