wheather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}


def convert_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


wheather_f = {day: convert_to_f(temp_c) for (day, temp_c) in wheather_c.items()}

print(wheather_f)
