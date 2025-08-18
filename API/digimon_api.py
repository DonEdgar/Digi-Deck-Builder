import requests

def call_api(URL):

    payload = {}
    headers = {}

    response = requests.request("GET", URL, headers=headers, data=payload)

    return response.text
