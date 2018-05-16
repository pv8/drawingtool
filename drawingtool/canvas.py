#!/usr/bin/env python3


class Canvas(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._area = []
        for _ in range(height):
            self._area.append([c for c in ' ' * width])

    def draw_line(self, x1, y1, x2, y2):
        if x1 == x2:  # vertical line
            for i in range(y1 - 1, y2):
                self._area[i][x1 - 1] = 'x'
        elif y1 == y2:  # horizontal line
            for i in range(x1 - 1, x2):
                self._area[y1 - 1][i] = 'x'

    def draw_rectangle(self, x1, y1, x2, y2):
        self.draw_line(x1, y1, x1, y2)
        self.draw_line(x1, y1, x2, y1)
        self.draw_line(x2, y1, x2, y2)
        self.draw_line(x1, y2, x2, y2)

    def __str__(self):
        canvas_str = '-' * (self.width + 2) + '\n'
        for line in self._area:
            canvas_str += '|' + ''.join(line) + '|\n'
        canvas_str += '-' * (self.width + 2)
        return canvas_str
