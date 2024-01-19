from question_model import Question
from data import question_data as qd
from quiz_brain import QuizBrain

question_bank=[]
for i in qd:
    quesestion_text=i["question"]
    quesestion_answer=i["correct_answer"]
    new_que=Question(quesestion_text, quesestion_answer)
    question_bank.append(new_que)

quiz_brain=QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You've completed the questions!")
print(f"Your score is: {quiz_brain.score}/{quiz_brain.question_number}")
