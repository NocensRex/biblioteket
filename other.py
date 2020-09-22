from pprint import pprint
import json


def write_to_file(data):
    keys = list(data.__dict__.keys())
    big_list = []
    for key in keys:
        category = data.__dict__[key]
        for row in category:
            temp_list = []
            temp_list.append(key)
            for item in row.__dict__:
                temp_list.append(row.__dict__[item])
            big_list.append(temp_list)
    pprint(big_list)


def write_to_json(data):
    temp_dict = {}
    keys = list(data.__dict__.keys())
    data_dict = data.__dict__
    for key in keys:
        temp_list = []
        object_list = data_dict[key]
        for object in object_list:
            temp_list.append(object.__dict__)
        temp_dict[key] = temp_list

    with open('data/test.json', 'w') as f:
        json.dump(temp_dict, f, indent=4, sort_keys=True)


def read_from_file(filename):
    pass
