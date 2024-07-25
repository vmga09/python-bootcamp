class QuizBrain:
    def __init__(self,question_list) -> None:
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        top_list =  len(self.question_list)
        if top_list > self.question_number:
            return True
        else: 
            return False

    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False) : ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Yor are correct")
        else:
            print(f"Yor are wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

