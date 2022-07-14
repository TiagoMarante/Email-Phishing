import json


def to_json(data):
    data_string = '{ "Message": "' + data + '"}'
    return json.loads(data_string)
