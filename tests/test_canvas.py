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


def test_try_draw_line_outside_canvas(base_canvas):
    expected_str = (
        '----------------------\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '----------------------'
    )
    base_canvas.draw_line(1, 2, 21, 2)  # vertical line
    assert str(base_canvas) == expected_str
    base_canvas.draw_line(6, 3, 6, 5)  # horizontal line
    assert str(base_canvas) == expected_str


def test_try_draw_rectangle_outside_canvas(base_canvas):
    expected_str = (
        '----------------------\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '----------------------'
    )
    base_canvas.draw_rectangle(16, 1, 20, 6)
    assert str(base_canvas) == expected_str
    base_canvas.draw_rectangle(16, 1, 21, 3)
    assert str(base_canvas) == expected_str
    base_canvas.draw_rectangle(16, 1, 21, 6)
    assert str(base_canvas) == expected_str


def test_bucket_fill(base_canvas):
    expected_str = (
        '----------------------\n'
        '|oooooooooooooooxxxxx|\n'
        '|xxxxxxooooooooox   x|\n'
        '|     xoooooooooxxxxx|\n'
        '|     xoooooooooooooo|\n'
        '----------------------'
    )
    base_canvas.draw_line(1, 2, 6, 2)
    base_canvas.draw_line(6, 3, 6, 4)
    base_canvas.draw_rectangle(16, 1, 20, 3)

    base_canvas.bucket_fill(10, 3, colour='o')
    assert str(base_canvas) == expected_str


def test_change_fill_colour(base_canvas):
    expected_str = (
        '----------------------\n'
        '|oooooooooooooooxxxxx|\n'
        '|xxxxxxooooooooox   x|\n'
        '|     xoooooooooxxxxx|\n'
        '|     xoooooooooooooo|\n'
        '----------------------'
    )
    base_canvas.draw_line(1, 2, 6, 2)
    base_canvas.draw_line(6, 3, 6, 4)
    base_canvas.draw_rectangle(16, 1, 20, 3)

    base_canvas.bucket_fill(10, 3, colour='o')
    assert str(base_canvas) == expected_str

    expected_str = (
        '----------------------\n'
        '|...............xxxxx|\n'
        '|xxxxxx.........x   x|\n'
        '|     x.........xxxxx|\n'
        '|     x..............|\n'
        '----------------------'
    )
    # change colour to '.'
    base_canvas.bucket_fill(10, 3, colour='.')
    assert str(base_canvas) == expected_str
