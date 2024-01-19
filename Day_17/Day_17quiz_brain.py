class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def next_question(self):
        question=self.question_list[self.question_number]
        self.question_number += 1
        user_input=input(f'{self.question_number}.Q: {question.text} (True/False)?')
        self.check_anserw(user_input,question.answer)

    def check_anserw(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score +=1
            print("You are right!")
        else:
            print("You are wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")


    def still_has_questions(self):
            return self.question_number < len(self.question_list)





