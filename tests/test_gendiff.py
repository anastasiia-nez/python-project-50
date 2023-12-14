import subprocess


def test_help_message():
    result = subprocess.run(['gendiff', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    assert result.returncode == 0
    assert """usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help   show this help message and exit""" in result.stdout
