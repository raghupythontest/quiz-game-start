from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
question_bank: list[Question] = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)
quiz_ui=QuizInterface(quiz)


# while quiz.still_has_question():
#     quiz.next_question()

print("\n\nYou have completed the quiz")
print(f"your score is:{quiz.score}/{len(question_bank)}")