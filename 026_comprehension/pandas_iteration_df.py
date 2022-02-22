student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(key, value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# print(student_data_frame)

#Loop through a data frame

# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    print(row.student)
    if row.student == "Angela":
        print(row.score)


# {new_key: new_value for (key, value) in dict.items()}

# {new_key: new_value for (index, row) in df.iterrows()}
