# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇

quantity_student_heights = len(student_heights)

# height_sum = 0
# for n in range(0, quantity_student_heights):
#     height_sum += student_heights[n]

total_height = 0
for height in student_heights:
    total_height += height


# average_height = height_sum / quantity_student_heights

average_height = total_height / quantity_student_heights

average_height_rounded = round(average_height)

print(average_height_rounded)
