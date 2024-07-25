from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for _ in question_data:
    question_bank.append(Question(_["text"],_["answer"]))


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You complete quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")