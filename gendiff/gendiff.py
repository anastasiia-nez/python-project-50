import json


def make_diff_string(key, value, modification='not_changed'):
    """The make_diff_string creates a string with a modification sign at the beginning.  # noqa: E501
    Default modification is 'not_changed'. Other options: 'old', 'new'."""
    result = ''
    if modification == 'not_changed':
        result = f'  {key}: {value}'
    if modification == 'old':
        result = f'- {key}: {value}'
    if modification == 'new':
        result = f'+ {key}: {value}'
    return result

# {
#  - follow: false
#    host: hexlet.io
#  - proxy: 123.234.53.22
#  - timeout: 50
#  + timeout: 20
#  + verbose: true
# }


def make_column(iterator):
    result = ''
    for i in iterator:
        result += f'{i}\n'
    return result


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

        diff = data1 | data2
        keys_ = diff.keys()
        keys_ = sorted(keys_)
        strings = []

        for key in keys_:
            if key in data1 and key not in data2:
                strings.append(make_diff_string(key, data1[key], 'old'))

            if key in data2 and key not in data1:
                strings.append(make_diff_string(key, data2[key], 'new'))

            if key in data1 and key in data2 and data1[key] == data2[key]:
                strings.append(make_diff_string(key, diff[key]))
            if key in data1 and key in data2 and data1[key] != data2[key]:
                strings.append(make_diff_string(key, data1[key], 'old'))
                strings.append(make_diff_string(key, data2[key], 'new'))

        result = '{\n' + make_column(strings) + '}'
        return result
