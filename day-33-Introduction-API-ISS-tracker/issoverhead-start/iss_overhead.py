import smtplib
import time
import requests
from datetime import datetime

MY_LAT = 19.452400
MY_LONG = -99.117746
FROM_MAIL = "g.rafafara666@gmail.com"
FROM_PASSWORD = "FFSe_4siAcGM_a:"


def is_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    is_in_latitude = iss_latitude - 5 <= MY_LAT <= iss_latitude + 5
    is_in_longitude = iss_longitude - 5 <= MY_LONG <= iss_longitude + 5
    return is_in_latitude and is_in_longitude


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    resp = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    resp.raise_for_status()
    dat = resp.json()
    sunrise = int(dat["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(dat["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow()
    hour_now = int(time_now.hour)

    return sunset < hour_now < sunrise


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_MAIL, password=FROM_PASSWORD)
        connection.sendmail(
            from_addr=FROM_MAIL,
            to_addrs="ray_Carr_@outlook.com",
            msg=f"ISS is over you, look up!\n\n"
                f"ISS is over your head"
        )


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def main():
    while True:
        if is_dark() and is_over_head():
            send_email()
        print("Cycle executed")
        time.sleep(60)


if __name__ == "__main__":
    main()


