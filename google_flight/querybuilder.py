import json

with open('airports.json') as data_file:
    data = json.load(data_file)


def get_iata_num(location):
    "Get IATA number for a given city."
    # TODO: Make thi sbetter so it can find cities with similar names or find multiple airports in the same city
    for i in data:
        city = data[i]['city']
        if location == city:
            iata = data[i]['iata']
        else:
            continue
    return iata
