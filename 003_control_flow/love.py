# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()


def count_letters_1(name):
    t = name.count("t")
    r = name.count("r")
    u = name.count("u")
    e = name.count("e")

    l = name.count("l")
    o = name.count("o")
    v = name.count("v")
    e2 = name.count("e")

    true = str(t + r + u + e)
    love = str(l + o + v + e2)
    return true + love


love_score = count_letters_1(lower_case_string)
love_score_to_int = int(love_score)

if love_score_to_int < 10 or love_score_to_int > 90:
    print(f"Your score is {love_score_to_int}, you go together like coke and mentos.")
elif 40 < love_score_to_int < 50:
    print(f"Your score is {love_score_to_int}, you are alright together.")
else:
    print(f"Your score is {love_score_to_int}.")
