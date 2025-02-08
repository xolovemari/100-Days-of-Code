from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "light pink"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Cute Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 25))
        self.score_label.grid(row=0, column=1)

        ribbon_image = PhotoImage(file="day 34/images/ribbow.png")
        self.ribbon_label = Label(image=ribbon_image, bg=THEME_COLOR)
        self.ribbon_label.grid(row=0, column=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="Some question text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        
        correct_image = PhotoImage(file="day 34/images/true.png")
        self.correct_button = Button(command=self.true_clicked, image=correct_image, highlightthickness=0)
        self.correct_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="day 34/images/false.png")
        self.wrong_button = Button(command=self.false_clicked, image=wrong_image, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)