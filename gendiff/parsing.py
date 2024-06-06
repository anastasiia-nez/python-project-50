import json
import yaml


def parse(path):
    file_name = path.split('/')[-1]
    format_ = file_name.split('.')[-1]

    if format_ in ['yaml', 'yml']:
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
            return data

    try:
        with open(path, 'r') as file:
            data = json.load(file)
            return data
    except TypeError:
        print('Wrong file format!')
