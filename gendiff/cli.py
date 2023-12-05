import argparse


def cli():
    parser = argparse.ArgumentParser(
    prog='gendiff',  # noqa: E122
    description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', type=str, required=True)
    parser.add_argument('second_file', type=str, required=True)
    parser.add_argument('-h', '--help', type=str, required=False)
    args = parser.parse_args()
    print(args.filename, args.count, args.verbose)
