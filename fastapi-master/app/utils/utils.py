import json


def to_json(data):
    if("Healthy" in data):
        data_string = '{ "Message": "' + data + '"}'
        return json.loads(data_string)
    else:
        return json.loads(data)