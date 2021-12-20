print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip wold you like to give? 10, 12 or 15? "))
total_people = int(input("How many people to split the bill? "))


total_bill_and_percentage = total_bill * (1 + percentage / 100)
each_people_part = total_bill_and_percentage / total_people
final_amount = round(each_people_part, 2)
# final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay: {final_amount:.2f}")
