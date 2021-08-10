#  FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

#  KeError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

#  IndexError
# fruit_list = ["apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#  TypeError
#  text = "abc"
#  print(text + 5)

# Use of exceptions
# try:
#     file = open("a_file.txt")
#     # a_dictionary = {"key": "value"}
#     # value = a_dictionary["non_existing_key"]
# except FileNotFoundError as error_message:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# # except KeyError as error_message:
# #     print(f"The Key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error that I made up.")

# height = float(input("Height: "))
# weight = float(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters")
#
# bmi = weight/(height ** 2)
# print(f"BMI: {bmi}")


