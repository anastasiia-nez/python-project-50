import subprocess
from gendiff.gendiff import generate_diff


FIRST_FILE_PATH = 'gendiff/json/file1.json'
SECOND_FILE_PATH = 'gendiff/json/file2.json'


def test_help_message():
    command = subprocess.run(['gendiff', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    assert command.returncode == 0
    assert """usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
""" in command.stdout


def test_generate_diff():
    assert generate_diff(FIRST_FILE_PATH, SECOND_FILE_PATH) == '''{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
}'''
