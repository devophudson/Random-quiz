from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    question_text = questions["text"]
    question_answer = questions["answer"]
    new_question = Questions(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You've be completed the challenge! ")
print(f"Your final score is {quiz.score}/{quiz.question_number}")


