from datetime import datetime

from io import StringIO

import os

from unittest import mock
import pytest

from drawingtool import cli


TIMESTAMP = datetime.now().strftime('%Y%m%d%H%M%S')

TEST_INPUT_FILE_NAME = f'test_input_{TIMESTAMP}.txt'
TEST_OUTPUT_FILE_NAME = f'test_input_{TIMESTAMP}.txt'


def remove_if_exists(filename):
    try:
        os.remove(filename)
    except OSError:
        pass


@pytest.fixture(scope="function")
def input_file():
    with open(TEST_INPUT_FILE_NAME, 'w') as f:
        f.write(
            'C 20 4\n'
            'L 1 2 6 2\n'
            'L 6 3 6 4\n'
            'R 16 1 20 3\n'
            'B 10 3 o\n'
        )
    yield f
    remove_if_exists(TEST_INPUT_FILE_NAME)
    remove_if_exists(TEST_OUTPUT_FILE_NAME)


def test_cli_default(input_file):
    expected_output = (
        '----------------------\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '----------------------\n'
        '----------------------\n'
        '|                    |\n'
        '|xxxxxx              |\n'
        '|                    |\n'
        '|                    |\n'
        '----------------------\n'
        '----------------------\n'
        '|                    |\n'
        '|xxxxxx              |\n'
        '|     x              |\n'
        '|     x              |\n'
        '----------------------\n'
        '----------------------\n'
        '|               xxxxx|\n'
        '|xxxxxx         x   x|\n'
        '|     x         xxxxx|\n'
        '|     x              |\n'
        '----------------------\n'
        '----------------------\n'
        '|oooooooooooooooxxxxx|\n'
        '|xxxxxxooooooooox   x|\n'
        '|     xoooooooooxxxxx|\n'
        '|     xoooooooooooooo|\n'
        '----------------------\n'
    )
    cli.run_tool(input_file.name, TEST_OUTPUT_FILE_NAME)
    with open(TEST_OUTPUT_FILE_NAME) as f:
        content = f.read()
        assert content == expected_output


def test_cli_stdout(input_file):
    expected_output = (
        '----------------------\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '----------------------\n'
        '----------------------\n'
        '|                    |\n'
        '|xxxxxx              |\n'
        '|                    |\n'
        '|                    |\n'
        '----------------------\n'
        '----------------------\n'
        '|                    |\n'
        '|xxxxxx              |\n'
        '|     x              |\n'
        '|     x              |\n'
        '----------------------\n'
        '----------------------\n'
        '|               xxxxx|\n'
        '|xxxxxx         x   x|\n'
        '|     x         xxxxx|\n'
        '|     x              |\n'
        '----------------------\n'
        '----------------------\n'
        '|oooooooooooooooxxxxx|\n'
        '|xxxxxxooooooooox   x|\n'
        '|     xoooooooooxxxxx|\n'
        '|     xoooooooooooooo|\n'
        '----------------------\n'
    )

    class MockStdout(StringIO):
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return None

    with mock.patch('drawingtool.cli.sys.stdout', new_callable=MockStdout) as mock_stdout:
        cli.run_tool(input_file.name)
        assert mock_stdout.getvalue() == expected_output


def test_cli_invalid_input():
    expected_output = 'First command should be [C] for creating the Canvas!\n'

    with open(TEST_INPUT_FILE_NAME, 'w') as invalid_input_file:
        invalid_input_file.write('X 0 1 2\n')

    class MockStdout(StringIO):
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return None

    with mock.patch('drawingtool.cli.sys.stdout', new_callable=MockStdout) as mock_stdout:
        cli.run_tool(invalid_input_file.name)
        assert mock_stdout.getvalue() == expected_output

    # remove test file
    remove_if_exists(TEST_INPUT_FILE_NAME)
