import requests

url = "https://digimoncard.io/api-public/search.php?n=Aldamon&desc=include a Digimon card&color=red&type=digimon&attribute=Variable&card=BT4-016&pack=BT-04: Booster Great Legend&sort=name&sortdirection=desc&series=Digimon Card Game&digitype=Wizard&evocost=3&evocolor=Red"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

for item in range(len(response.text) - 1):
    print(response.text[item])
