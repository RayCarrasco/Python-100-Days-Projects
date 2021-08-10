from data import question_data


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuestionBank:
    def __init__(self):
        self.question_bank = []
        for item in question_data:
            self.question_bank.append(Question(text=item["question"], answer=item["correct_answer"]))
