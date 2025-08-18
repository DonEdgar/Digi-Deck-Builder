colors = ["Black", "Blue", "Colorless", "Green", "Purple", "Red", "White", "Yellow"]

card_types = ["Digimon", "Tamer", "Option", "Digi-Egg"]

def query_builder():
    params = {}

    def filter_non_empty_values(params):
        updated_params = {}

        for key, value in params.items():
            if value != "":
                updated_params[key] = value

        return updated_params
    
    card_name = input("Enter card name (leave blank if no name): ")

    params["n"] = card_name # n = name

    card_color = input("Enter card color (leave blank if no color): ")

    params["color"] = card_color
    
    #if card_color not in colors:
        #print("Please enter one of the following colors:")
        #for color in colors:
            #print("\t colors[color]")

    card_level = input("Enter card level (leave blank if no level): ")

    params["level"] = card_level

    card_type = input("Enter card type (leave blank if no type): ")

    params["type"] = card_type

    card_rarity = input("Enter card rarity (leave blank if no type): ")

    params["rarity"] = card_rarity

    updated_params = filter_non_empty_values(params)

    return updated_params
