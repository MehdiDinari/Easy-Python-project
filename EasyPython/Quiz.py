import tkinter as tk
from tkinter import messagebox, font


class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("600x400")  # Taille de la fenêtre
        self.master.config(bg="#f0f0f0")  # Couleur de fond

        self.score = 0
        self.question_index = 0

        self.questions = [
            ("La capitale du Maroc?", "rabat"),
            ("La capitale de la France?", "paris"),
            ("La capitale de l'Espagne?", "madrid"),
            ("La capitale du Portugal?", "lisbonne"),
            ("La capitale de l'Italie?", "rome")
        ]

        self.title_font = font.Font(family="Helvetica", size=16, weight="bold")
        self.question_font = font.Font(family="Helvetica", size=14)
        self.button_font = font.Font(family="Helvetica", size=12)

        self.title_label = tk.Label(master, text="Bienvenue dans le Quiz!", font=self.title_font, bg="#f0f0f0")
        self.title_label.pack(pady=20)

        self.question_label = tk.Label(master, text="", font=self.question_font, bg="#f0f0f0")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(master, font=self.question_font, width=30)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Soumettre", command=self.check_answer, font=self.button_font,
                                       bg="#4CAF50", fg="white")
        self.submit_button.pack(pady=10)

        self.start_button = tk.Button(master, text="Commencer le Quiz", command=self.start_quiz, font=self.button_font,
                                      bg="#2196F3", fg="white")
        self.start_button.pack(pady=10)

    def start_quiz(self):
        self.score = 0
        self.question_index = 0
        self.show_question()

    def show_question(self):
        if self.question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.question_index][0])
            self.answer_entry.delete(0, tk.END)
        else:
            self.show_result()

    def check_answer(self):
        user_answer = self.answer_entry.get().lower()
        correct_answer = self.questions[self.question_index][1]

        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Résultat", "Correcte")
        else:
            messagebox.showinfo("Résultat", "Incorrecte")

        self.question_index += 1
        self.show_question()

    def show_result(self):
        percentage = (self.score * 100) / len(self.questions)
        messagebox.showinfo("Quiz terminé",
                            f"Votre score est {self.score}\nVotre score en pourcentage est {percentage:.2f} %")
        self.ask_replay()

    def ask_replay(self):
        replay = messagebox.askyesno("Rejouer", "Voulez-vous jouer à nouveau ?")
        if replay:
            self.start_quiz()
        else:
            self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()