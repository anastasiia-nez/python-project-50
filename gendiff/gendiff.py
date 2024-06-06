from gendiff.parsing import parse


def make_diff_string(key, value, modification='changeless'):
    result = ''
    if modification == 'changeless':
        result = f'    {key}: {value}'
    if modification == 'old':
        result = f'  - {key}: {value}'
    if modification == 'new':
        result = f'  + {key}: {value}'
    return result.lower()


def make_column(strings_set):
    result = ''
    for string in strings_set:
        result += f'{string}\n'
    result = '{\n' + result + '}'
    return result


# {
#   - follow: false
#     host: hexlet.io
#   - proxy: 123.234.53.22
#   - timeout: 50
#   + timeout: 20
#   + verbose: true
# }


def generate_diff(path1, path2):
    data1 = parse(path1)
    data2 = parse(path2)

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

    result = make_column(strings)
    return result
