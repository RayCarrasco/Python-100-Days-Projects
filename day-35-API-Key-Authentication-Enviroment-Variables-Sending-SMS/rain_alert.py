import requests
import os
from twilio.rest import Client


LATITUDE = 19.452384
LONGITUDE = -99.117877

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
APPI_KEY = os.environ.get("OWM_API_KEY")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PNONE")
my_number = os.environ.get("MY_NUMBER")


def send_sms(body_message, from_number, to_number):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body_message,
        from_=TWILIO_PHONE_NUMBER,
        to=my_number
    )
    print(message.status)


def get_hourly_prediction():
    parameters = {
        "lat": LATITUDE,
        "lon": LONGITUDE,
        "appid": APPI_KEY,
        "exclude": ["current,minutely,daily,alerts"]
    }
    response = requests.get(url=OWM_ENDPOINT, params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["hourly"]


def is_going_to_rain(hourly_weather: list) -> bool:
    for hour in hourly_weather[0:11]:
        if 700 > int(hour["weather"][0]["id"]):
            return True
        else:
            return False


def main():
    if is_going_to_rain(get_hourly_prediction()):
        body_message = "Hoy lloverá. Recuerda tu paraguas ☔"
        send_sms(body_message, TWILIO_PHONE_NUMBER, my_number)
    else:
        print("Nel")


if __name__ == '__main__':
    main()
