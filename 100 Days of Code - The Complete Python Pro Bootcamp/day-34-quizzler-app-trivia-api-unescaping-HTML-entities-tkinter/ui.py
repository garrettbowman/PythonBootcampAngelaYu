from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"



class QuizInterface:

    def __init__(self,quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="#FFFFFF", highlightthickness=0)

        self.question_text = self.canvas.create_text(
            150, 125,
            text="dsfsd",
            fill="black",
            font=(FONT_NAME, 20, "italic"),
            width=280
        )
        self.canvas.grid(column=0, row=1,columnspan=2, pady=50)
        self.get_next_question()
        true_img = PhotoImage(file="images/true.png")

        false_img = PhotoImage(file="images/false.png")

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2,pady=20)

        self.true_button = Button(image= true_img, highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(column=0, row=2,pady=20)

        self.score_label = Label(text="Score: 0", fg="#FFFFFF", bg=THEME_COLOR, font=(FONT_NAME, 20))
        self.score_label.grid(column=1, row=0)
        self.window.mainloop()

    def get_next_question(self):

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)

    def true_pressed(self):
        self.quiz.check_answer("true")

    def false_pressed(self):
        self.quiz.check_answer("false")