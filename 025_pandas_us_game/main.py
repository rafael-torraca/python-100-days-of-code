# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))
print(data["temp"])

data_dict = data.to_dict()

print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))

print(data["temp"].mean())

print(data["temp"].max())
print(data["temp"].min())

#Get data in columns
print(data["condition"])
print(data.condition)

#get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp)
monday_temp_f = (int(monday.temp) * 9/5) + 32
print(monday_temp_f)

# create a dataframe from scratch
data_dictionary = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data_dict_df = pandas.DataFrame(data_dictionary)

print(data_dict_df)
data_dict_df.to_csv("new_data_.csv")
data_dict_df.to_html("new_html.html")