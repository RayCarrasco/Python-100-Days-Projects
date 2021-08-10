# Open a file allows to read the file
with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
    file.close()

# Write to a file, override the content of the file. If file does not exist, then it is created
# with open('my_file_created.txt', mode='w') as file:
#     file.write("New Text.")

# Append to a file, adds the texts to the end of the file
# with open('my_file.txt', mode='a') as file:
#     file.write("\nNew Text 2.")
