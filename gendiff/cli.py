import argparse


def cli():
    parser = argparse.ArgumentParser(
    prog='gendiff',  # noqa: E122
    description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    print(args.filename, args.count, args.verbose)
