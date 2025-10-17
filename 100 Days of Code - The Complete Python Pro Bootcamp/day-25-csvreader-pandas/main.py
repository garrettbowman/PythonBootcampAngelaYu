# import csv
# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#

# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         temperatures.append(row[1])
#
#     del temperatures[0]
#     print(temperatures)

import pandas

# data = pandas.read_csv("./weather_data.csv")

# print(data["temp"])

# data_dict = data.to_dict()
#
# print(data_dict)

# temp_list = data["temp"].tolist()
#
# print(temp_list)
#
# average = sum(temp_list) / len(temp_list)
#
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
#
# print(data[data.temp == data["temp"].max()])
#
#
# monday = data[data.day == "Monday"]
#
# print(monday.condition)
#
# monday_temp = monday.temp[0]
# monday_temp_c = 9/5 * monday_temp +32
#
# print(monday_temp)
# print(monday_temp_c)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cin_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

# print(cin)
# print(len(cin))
# print(gray)
# print(len(gray))
# print(black)
# print(len(black))

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray_count,cin_count,black_count]

}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")