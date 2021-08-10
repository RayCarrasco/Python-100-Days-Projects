import pandas
import datetime as dt
import smtplib
from random import choice

FROM_MAIL = "g.rafafara666@gmail.com"
FROM_PASSWORD = "FFSe_4siAcGM_a:"


##################### Extra Hard Starting Project ######################
# 1. Update the birthdays.csv
def get_birthdays():
    now = dt.datetime.now()
    birthdays = pandas.read_csv("birthdays.csv")
    birthdays_this_month = birthdays[birthdays.month == now.month]

    return birthdays_this_month[birthdays_this_month.day == now.day]

# 2. Check if today matches a birthday in the birthdays.csv
def there_congratulations(birthdays):
    now = dt.datetime.now()
    if birthdays.name.count() != 0:
        return True



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def get_cards():
    cards_to_choose = []
    for n in range(1,4):
        with open(f"letter_templates/letter_{n}.txt", "r") as data_letter:
            cards_to_choose.append(data_letter.read())
    return cards_to_choose


# 4. Send the letter generated in step 3 to that person's email address.

def send_email(destination, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_MAIL, password=FROM_PASSWORD)
        connection.sendmail(
            from_addr=FROM_MAIL,
            to_addrs=destination,
            msg=f"subject: Happy birthday!\n\n"
                f"{message}"
        )


def get_names_and_emails(data_to_congratulate):
    names_and_emails = {}
    for index, row in data_to_congratulate.iterrows():
        names_and_emails[row["name"]] = row["email"]
    return names_and_emails

# main function
def main():
    cards = get_cards()
    to_congratulate = get_birthdays()
    if there_congratulations(to_congratulate):
        congratulations_to_send = get_names_and_emails(to_congratulate)
        for name, email in congratulations_to_send.items():
            personal_card = choice(cards)
            message = personal_card.replace("[NAME]", f"{name}").replace("[FROM_NAME]", "Raymundo")
            send_email(email, message)



if __name__ == "__main__":
    main()
