from question_model import QuestionBank
from quiz_brain import QuizBrain

bank = QuestionBank()
qbrain = QuizBrain(bank.question_bank)

while qbrain.still_has_questions():
    qbrain.next_question()

print(f"You completed the quiz\n"
      f"Your final score was: {qbrain.score}/{len(bank.question_bank)}")