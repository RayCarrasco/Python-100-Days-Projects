import requests


def get_questions():
    parameters={
        "amount": 10,
        "type": "boolean"
    }
    response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean", params=parameters)
    data = response.json()

    return data["results"]


question_data = get_questions()
