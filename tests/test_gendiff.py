import subprocess
from gendiff.gendiff import generate_diff


FIRST_FILE_PATH_FOR_FLAT = 'tests/fixtures/json/file1.json'
SECOND_FILE_PATH_FOR_FLAT = 'tests/fixtures/json/file2.json'
HELP = 'tests/fixtures/cli_help.txt'
flat_diff_json_1_result = 'tests/fixtures/flat_diff_json_1.txt'


def test_help_message():
    command = subprocess.run(['gendiff', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    assert command.returncode == 0
    with open(HELP) as file:
        expected_result = file.read()
        assert command.stdout == expected_result


def test_generate_diff():
    with open(flat_diff_json_1_result) as file:
        expected_result = file.read()
        assert generate_diff(FIRST_FILE_PATH_FOR_FLAT, SECOND_FILE_PATH_FOR_FLAT) == expected_result

    