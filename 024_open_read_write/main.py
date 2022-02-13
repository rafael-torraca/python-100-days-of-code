# with open("C:/Users/rafael/Desktop/my_file.txt", "r") as file:
#     contents = file.read()
#     print(contents)

with open("my_file.txt", "w") as file:
    file.write("\nNew text. 3")

with open("my_file.txt", "a") as file:
    file.write("\nNew text. 42")



