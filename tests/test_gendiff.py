import subprocess
from gendiff.gendiff import generate_diff

HELP = 'tests/fixtures/results/cli_help.txt'
FIRST_PATH_FOR_FLAT_JSON_1 = 'tests/fixtures/json/flat1_1.json'
SECOND_PATH_FOR_FLAT_JSON_1 = 'tests/fixtures/json/flat1_2.json'
FLAT_JSON_RESULT_1 = 'tests/fixtures/results/flat_json_1.txt'
FIRST_PATH_FOR_FLAT_YAML_1 = 'tests/fixtures/yaml/flat1_1.yml'
SECOND_PATH_FOR_FLAT_YAML_1 = 'tests/fixtures/yaml/flat1_2.yml'
FLAT_YAML_RESULT_1 = 'tests/fixtures/results/flat_yaml_1.txt'


def test_help_message():
    command = subprocess.run(['gendiff', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    assert command.returncode == 0
    with open(HELP) as file:
        expected_result = file.read()
        assert command.stdout == expected_result


def test_generate_diff():
    with open(FLAT_JSON_RESULT_1) as file:
        expected_result = file.read()
        assert generate_diff(FIRST_PATH_FOR_FLAT_JSON_1, SECOND_PATH_FOR_FLAT_JSON_1) == expected_result
    with open(FLAT_YAML_RESULT_1) as file:
        expected_result = file.read()
        assert generate_diff(FIRST_PATH_FOR_FLAT_YAML_1, SECOND_PATH_FOR_FLAT_YAML_1) == expected_result
