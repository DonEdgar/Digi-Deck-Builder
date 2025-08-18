from typing import Dict

def urlbuilder(params: Dict[str, str]):

    BASEURL = "https://digimoncard.io/api-public/search.php?"
    QUERY = ""

    param_length = len([parameters for parameters in params.keys()]) -1

    for idx, (param, value) in enumerate(params.items()):
        if idx < param_length: # and value != "":
            QUERY += f"{param}={value}&"
        elif idx == param_length:
            QUERY += f"{param}={value}"

    URL = BASEURL + QUERY

    return URL
