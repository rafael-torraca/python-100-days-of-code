# Create a program using maths and f-Strings that tells us how many days, weeks,
# months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time
# left in this format:
# You have x days, y weeks, and z months left.

age = input("What is your current age?")

age_as_int = int(age)

years_left = 90 - age_as_int
months_left = 12 * years_left
weeks_left = 52 * years_left
days_left = 365 * years_left

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
print(years_left)
