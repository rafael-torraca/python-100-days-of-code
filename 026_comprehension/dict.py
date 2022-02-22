# new_dict = {new_key:new_value for item in list}

# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

import random

students_scores = {student: random.randint(1, 100) for student in names}

print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score > 70}

print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word: len(word) for word in sentence.split()}

print(result)
