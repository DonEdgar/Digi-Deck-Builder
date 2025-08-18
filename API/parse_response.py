import json

from query_builder import query_builder
from urlbuilder import urlbuilder
from digimon_api import call_api

params = query_builder()

url = urlbuilder(params)

raw_json = call_api(url)

cleaned_json = json.dumps(raw_json)

print(cleaned_json)
