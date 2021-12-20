import random
import my_module

print(my_module.PI)

random_integer = random.randint(1, 10)
print(random_integer)

# 0.000000 - 0.999999
random_float = random.random()
print(random_float)

# 0.000000 - 4.99999
print(random_float * 5)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
