
import pandas

# data = pandas.read_csv("weather_data.csv")

# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["day"])
# print(data.day)

# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# temp_f = int(monday.temp) * (9/5) + 32
# print(temp_f)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 80]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# TODO 1: Primary Fur Color


# --------------- My Solution ----------------------
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# fur_data = squirrel_data["Primary Fur Color"].to_list()
#
# squirrel_count_dict = {
#     "Fur Color": ["grey", "red", "black"],
#     "Count": [0, 0, 0]
# }
#
# for fur_color in fur_data:
#     if fur_color == 'Gray':
#         squirrel_count_dict["Count"][0] += 1
#     elif fur_color == 'Cinnamon':
#         squirrel_count_dict["Count"][1] += 1
#     elif fur_color == 'Black':
#         squirrel_count_dict["Count"][2] += 1
#
# data = pandas.DataFrame(squirrel_count_dict)
# data.to_csv("squirrel_count.csv")


# --------------- Instructor Solution ----------------------
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
