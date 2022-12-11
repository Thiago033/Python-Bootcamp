# import csv

# with open("section-025/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
    
#     temperatures = []
    
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

import pandas

# data = pandas.read_csv("section-025/weather_data.csv")

# temp_data = data["temp"].tolist()
# average = sum(temp_data)/len(temp_data)
# print(average)

# print(data.temp.mean())


# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# data_dict = {
#     "students": ["Any", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("section-025/new_data.csv")

data = pandas.read_csv("section-025/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("section-025/squirrel_count.csv")
