from data import question_data
from question_model import Question

question_bank = []
for _ in question_data:
    question_bank.append(Question(_["text"],_["answer"]))

print(question_bank[0].text)