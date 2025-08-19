import json

import query_builder
import urlbuilder
import digimon_api

def raw_to_json():
    params = query_builder.query_builder()

    url = urlbuilder.urlbuilder(params)

    raw_json = digimon_api.call_api(url)

    cleaned_json = json.dumps(raw_json)

    return cleaned_json

json_string = raw_to_json()

print(json_string)