from drawingtool.canvas import Canvas


def test_canvas_str():
    expected_str = (
        '----------------------\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '|                    |\n'
        '----------------------'
    )
    canvas = Canvas(width=20, height=4)
    assert str(canvas) == expected_str


def test_draw_horizontal_line():
    expected_str = (
        '----------------------\n'
        '|                    |\n'
        '|xxxxxx              |\n'
        '|                    |\n'
        '|                    |\n'
        '----------------------'
    )
    canvas = Canvas(width=20, height=4)
    canvas.draw_line(1, 2, 6, 2)
    assert str(canvas) == expected_str


def test_draw_vertical_line():
    expected_str = (
        '----------------------\n'
        '|                    |\n'
        '|                    |\n'
        '|     x              |\n'
        '|     x              |\n'
        '----------------------'
    )
    canvas = Canvas(width=20, height=4)
    canvas.draw_line(6, 3, 6, 4)
    assert str(canvas) == expected_str


def test_draw_rectangle():
    expected_str = (
        '----------------------\n'
        '|               xxxxx|\n'
        '|               x   x|\n'
        '|               xxxxx|\n'
        '|                    |\n'
        '----------------------'
    )
    canvas = Canvas(width=20, height=4)
    canvas.draw_rectangle(16, 1, 20, 3)
    assert str(canvas) == expected_str
