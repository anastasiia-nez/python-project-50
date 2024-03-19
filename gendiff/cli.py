import argparse
from gendiff.gendiff import generate_diff


def cli():
    parser = argparse.ArgumentParser(
    prog='gendiff',  # noqa: E122
    description='Compares two configuration files and shows a difference.')  # noqa: E122, E501

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str, help='set format of output', required=False)  # noqa: E501
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
