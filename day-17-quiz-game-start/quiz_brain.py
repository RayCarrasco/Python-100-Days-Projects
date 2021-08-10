class QuizBrain:
    """"Creates a QuizBrain object (QuestionBank)"""

    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        """"Print the next question and ask teh user for true/false, return the users answer"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, current_question.answer.lower())

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number} \n")
