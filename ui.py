from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"



class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):# we specify the datatype that quiz_brain has QuizBrain datatype
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config( bg=THEME_COLOR)
        self.score_label = Label(text = f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="White", font=('Arial', 10))
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.score_label.grid(column=1, row=0, pady=20)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20, padx=20)
        self.question_text = self.canvas.create_text(150,125, width=300, text = self.quiz.next_question(), font=('Arial', 20, 'italic'), fill=THEME_COLOR)
        right = PhotoImage(file="day_34/images/true.png")
        wrong = PhotoImage(file="day_34/images/false.png")
        self.true = Button(image=right,highlightthickness=0, borderwidth=0, command=self.check_answer_true)
        self.true.grid(column=0,row=2, pady=20)
        self.false = Button(image=wrong,highlightthickness=0, borderwidth=0, command=self.check_answer_false)
        self.false.grid(column=1,row=2, pady=20)
        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = self.q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = f"You've reached the end of the quiz. Your final score is {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
        self.canvas.config(bg="white")
    def check_answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
        # self.get_next_question()

    def check_answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)


    def give_feedback(self, is_right: bool):
        if is_right:
            self.score_label.config(text = f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)