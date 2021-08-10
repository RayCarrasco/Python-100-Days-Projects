with open('./Input/Names/invited_names.txt', mode='r') as names:
    names_list = names.readlines()

with open('./Input/Letters/starting_letter.txt', mode='r') as letter:
    starting_letter = letter.read()

for name in names_list:
    striped_name = name.strip()
    new_letter = starting_letter.replace("[name]", f"{striped_name}")

    with open(f'./Output/ReadyToSend/letter_for_{striped_name}.txt', mode='a') as write_letter:
        for line in new_letter:
            write_letter.write(line)

