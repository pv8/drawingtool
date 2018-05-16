#!/usr/bin/env python3


class Canvas(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._area = []
        for _ in range(height):
            self._area.append([c for c in ' ' * width])

    def _inside_canvas(self, x, y):
        return 0 < x <= self.width and 0 < y <= self.height

    def draw_line(self, x1, y1, x2, y2):
        if self._inside_canvas(x1, y1) and self._inside_canvas(x2, y2):
            if x1 == x2:  # vertical line
                for i in range(y1 - 1, y2):
                    self._area[i][x1 - 1] = 'x'
            elif y1 == y2:  # horizontal line
                for i in range(x1 - 1, x2):
                    self._area[y1 - 1][i] = 'x'

    def draw_rectangle(self, x1, y1, x2, y2):
        if self._inside_canvas(x1, y1) and self._inside_canvas(x2, y2):
            self.draw_line(x1, y1, x1, y2)
            self.draw_line(x1, y1, x2, y1)
            self.draw_line(x2, y1, x2, y2)
            self.draw_line(x1, y2, x2, y2)

    def _change_fill_colour(self, x, y, new_colour, old_colour):
        if self._inside_canvas(x, y):
            if self._area[y - 1][x - 1] == old_colour:
                self._area[y - 1][x - 1] = new_colour

                # recursively apply colour on surrounding points
                self._change_fill_colour(x, y + 1, new_colour, old_colour)
                self._change_fill_colour(x + 1, y, new_colour, old_colour)
                self._change_fill_colour(x, y - 1, new_colour, old_colour)
                self._change_fill_colour(x - 1, y, new_colour, old_colour)

    def bucket_fill(self, x, y, colour):
        if self._inside_canvas(x, y):
            existing_colour = self._area[y - 1][x - 1]
            if existing_colour != colour:
                self._change_fill_colour(x, y, colour, existing_colour)

    def __str__(self):
        canvas_str = '-' * (self.width + 2) + '\n'
        for line in self._area:
            canvas_str += '|' + ''.join(line) + '|\n'
        canvas_str += '-' * (self.width + 2)
        return canvas_str
