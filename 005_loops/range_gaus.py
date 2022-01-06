total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)


total2 = 0
for number2 in range(2, 101, 2):
    total2 += number2
print(total2)
