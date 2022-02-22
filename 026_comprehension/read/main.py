
def read_files(path):
    with open(path) as data_file:
        data_content = data_file.readlines()
        return_data = []
        for data in data_content:
            striped_data = data.strip()
            return_data.append(striped_data)
        return return_data


file1 = read_files("file1.txt")
file2 = read_files("file2.txt")
#
result = [int(n) for n in file1 if n in file2]
#
# # Write your code above 👆
#
print(result)

# ==================================================================

with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result_2 = [int(num) for num in file_1_data if num in file_2_data]

print(result_2)
