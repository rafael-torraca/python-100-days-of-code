from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
extracted_questions = question_data["results"]

for question in extracted_questions:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

