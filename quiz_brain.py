import html
class QuizBrain:
    correct_answer = None
    def __init__(self, a_list):
        self.question_number = 0
        self.question_list = a_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text=html.unescape(current_question.question)
        self.correct_answer=current_question.answer
        return f"Q{self.question_number}:{q_text}"

        # user_answer = input(f"Q{self.question_number}:{q_text} (True/False):")
        # self.compare_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def compare_answer(self,user_answer):
        if user_answer== self.correct_answer:
            print("you got it right!")
            self.score = self.score + 1
            return True
        else:
            # self.end = False
            return False
        #     print("you are wrong!")
        # print(f"Your score is:{self.score}/{self.question_number}")
        # print(f"The correct answer was:{self.correct_answer}")
