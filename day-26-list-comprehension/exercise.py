# # Exercise 1
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
# # Write your 1 line code 👇 below:
# squared_numbers = [n ** 2 for n in numbers]
# # Write your code 👆 above:
# print(squared_numbers)
#
# # Exercise 2
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
# result = {word: len(word) for word in sentence.split()}
# # Write your code below:
# print(result)
#
# # Exercise 3
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
# weather_f = {day: (temp_c * 9 / 5) + 32 for day, temp_c in weather_c.items()}
# # Write your code 👇 below:
# print(weather_f)
#
# # Iterate in pandas data frame
#
#
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}
#
# for (key, value) in student_dict.items():
#     print(f"***{key}: {value}")
#
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through a data frame
# for key, value in student_data_frame.items():
#     print(f"###{key}: ->{value}")

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row["student"] == "Angela":
        print(row.score)
