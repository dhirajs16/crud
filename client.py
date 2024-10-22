import json
import requests

URL = ''

def get_data(id = None):
    data = {}
    if id is not None:
        data = {id : id}
        json_data = json.dumps(data)
        res = requests.get(url=URL, data=json_data)

        data = res.json()
        print(data)

get_data()