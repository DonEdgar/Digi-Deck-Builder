import requests
import urlbuilder
"""
url = "https://digimoncard.io/api-public/search.php?n=Aldamon&desc=include a Digimon card&color=red&type=digimon&attribute=Variable&card=BT4-016&pack=BT-04: Booster Great Legend&sort=name&sortdirection=desc&series=Digimon Card Game&digitype=Wizard&evocost=3&evocolor=Red"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
"""

test_params = {"n": "Agumon", "color": "red", "level": "3"}

URL = urlbuilder.urlbuilder(test_params)

def test_api(url):
     url = url
     
     payload = {}
     
     headers = {}
     response = requests.request("GET", url, headers=headers, data=payload)
     print(response.text)


test_api(URL)
