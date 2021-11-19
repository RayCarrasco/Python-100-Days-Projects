import requests
import os
from datetime import datetime

# Token and username must be changed to your user
TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("USER_NAME")

GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
set_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
actualizar_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"
header = {"X-USER-TOKEN": TOKEN}


def crear_usuario():
    users_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    response = requests.post(url=pixela_endpoint, json=users_params)
    print(response.text)


def crear_grafica():
    graph_user_params = {
        "id": "graph1",
        "name": "Cycling graph",
        "unit": "kilometers",
        "type": "float",
        "color": "ajisai",
    }

    response = requests.post(url=graph_endpoint, json=graph_user_params, headers=header)
    print(response.text)


def agregar_pixel(date: datetime):
    # date = datetime.now()
    pixel_user_params = {
        "date": date.strftime("%Y%m%d"),
        "quantity": "5.1",
    }

    response = requests.post(url=set_pixel_endpoint, json=pixel_user_params, headers=header)
    print(response.text)


def crear_fecha(year, month, day) -> datetime:
    # https://www.w3schools.com/python/python_datetime.asp
    date = datetime(year=year, month=month, day=day)
    return date


def actualizar_pixel():
    update_pixel_params = {
        "quantity": "9.9",
    }
    url_date = f"{actualizar_endpoint}20211119"
    response = requests.put(url=url_date, json=update_pixel_params, headers=header)
    print(response.text)


def borrar_pixel():
    url_date = f"{actualizar_endpoint}20211119"
    response = requests.delete(url=url_date, headers=header)
    print(response.text)


def main():
    agregar_pixel(crear_fecha(2021, 11, 19))


if __name__ == '__main__':
    main()
