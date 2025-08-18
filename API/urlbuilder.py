from query_builder import query_builder

params = query_builder()

def urlbuilder(params):

    BASEURL = "https://digimoncard.io/api-public/search.php?"
    URL = ""

    for item in params:
        if params[item] != "":
            URL = item + "=" + params[item]
