import smtplib
from random import choice
import datetime as dt

DAYS_OF_THE_WEEK=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Destination = "ray_carr_@outlook.com"

FROM_MAIL = "example@yahoo.com"
FROM_PASSWORD = "123"


def get_day_of_the_week():
    return DAYS_OF_THE_WEEK[dt.datetime.now().weekday()]


def get_quotes():
    with open("quotes.txt", "r") as data_file:
        return data_file.readlines()


def get_random_quote():
    return choice(get_quotes())


def send_email():
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=FROM_MAIL, password=FROM_PASSWORD)
        connection.sendmail(
            from_addr=FROM_MAIL,
            to_addrs=Destination,
            msg=f"subject: Motivational Quote of the Friday\n\n"
                f"{get_random_quote()}"
        )


def main():
    if get_day_of_the_week() == "Friday":
        send_email()
        print("Done")


if __name__ == "__main__":
    main()

