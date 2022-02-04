class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.questions_list: list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        c_answer = current_question.answer
        self.check_answer(user_answer, c_answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correc answer was: {c_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
