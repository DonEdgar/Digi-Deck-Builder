import requests
from urlbuilder import urlbuilder
from query_builder import query_builder


params = query_builder()

URL = urlbuilder(params)
print(URL)

def call_api(URL):

    payload = {}
    headers = {}

    response = requests.request("GET", URL, headers=headers, data=payload)

    print(response.text)

call_api(URL)
