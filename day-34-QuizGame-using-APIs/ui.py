from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

# User Interface


class QuizInterface():
    attribute = None

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self. window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # label
        self.score_lab = Label(text="score: 0", bg= THEME_COLOR, fg="white")
        self.score_lab.grid(row=0, column=1)

        # canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_q_tet = self.canvas.create_text(
            150,
            125,
            text="Question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, bg=THEME_COLOR, relief="flat", command=self.true_button_clicked)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_img , bg=THEME_COLOR, relief="flat", command=self.false_button_clicked)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():

            self.score_lab.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_q_tet, text=q_text)
        else:
            self.canvas.itemconfig(
                self.canvas_q_tet,
                text="You have reached the end of the quizz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.canvas.config(bg="white")

    def true_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



