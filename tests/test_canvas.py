import pytest

from drawingtool.canvas import Canvas


@pytest.fixture(scope='function')
def base_canvas():
    return Canvas(width=20, height=4)


def test_canvas_str(base_canvas):
    expected_str = (
        '----------------------\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '----------------------'
    )
    assert str(base_canvas) == expected_str


def test_draw_horizontal_line(base_canvas):
    expected_str = (
        '----------------------\n'
        '|                    |\n'
        '|xxxxxx              |\n'
        '|                    |\n'
        '|                    |\n'
        '----------------------'
    )
    base_canvas.draw_line(1, 2, 6, 2)
    assert str(base_canvas) == expected_str


def test_draw_vertical_line(base_canvas):
    expected_str = (
        '----------------------\n'
        '|                    |\n'
        '|                    |\n'
        '|     x              |\n'
        '|     x              |\n'
        '----------------------'
    )
    base_canvas.draw_line(6, 3, 6, 4)
    assert str(base_canvas) == expected_str


def test_draw_rectangle(base_canvas):
    expected_str = (
        '----------------------\n'
        '|               xxxxx|\n'
        '|               x   x|\n'
        '|               xxxxx|\n'
        '|                    |\n'
        '----------------------'
    )
    base_canvas.draw_rectangle(16, 1, 20, 3)
    assert str(base_canvas) == expected_str
