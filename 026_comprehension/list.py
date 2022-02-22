# for loop
numbers = [1, 2, 3, 4, 5]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# List Comprehension
new_list_comprehension = [n + 1 for n in numbers]
print(new_list_comprehension)

# Rang List Comprehension
range_list = [n * 2 for n in range(1, 5)]
print(range_list)

# Conditional List Comprehension
only_pairs = [n for n in range(1, 11) if n % 2 == 0]
print(only_pairs)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

uppercase_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_names)