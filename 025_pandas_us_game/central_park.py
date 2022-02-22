import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data["Primary Fur Color"].value_counts())
data["Primary Fur Color"].value_counts().to_csv("squirrel.csv")


grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrel, cinnamon_squirrel, black_squirrel)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel, cinnamon_squirrel, black_squirrel]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)
