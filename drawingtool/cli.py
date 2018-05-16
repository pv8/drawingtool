#!/usr/bin/env python3
import fileinput
import sys
from argparse import ArgumentParser

from .canvas import Canvas


DEFAULT_OUTPUT_FILE = 'output.txt'


def create_parser():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', metavar='FILE', nargs='?', required=True,
                        help='input file. If empty, stdin will be used.')
    parser.add_argument('--stdout', action='store_true',
                        help='output results in stdout instead of a file.')
    parser.add_argument('-o', '--output', default=DEFAULT_OUTPUT_FILE,
                        help='output file name. Default: {}'.format(DEFAULT_OUTPUT_FILE))

    return parser


def run_tool(input_file, output_file=None):
    fi = fileinput.input(input_file)
    canvas_data = fi.readline().split()
    if canvas_data[0] != 'C':
        print('First command should be [C] for creating the Canvas!')
        return

    if output_file:
        output_to = open(output_file, 'w')
    else:
        output_to = sys.stdout

    with output_to as output:
        canvas = Canvas(int(canvas_data[1]), int(canvas_data[2]))
        print(canvas, file=output)
        for line in fi:
            command_data = line.split()
            command = command_data[0]
            if command in ['L', 'R']:
                x1 = int(command_data[1])
                x2 = int(command_data[2])
                y1 = int(command_data[3])
                y2 = int(command_data[4])
                if command == 'L':
                    canvas.draw_line(x1, x2, y1, y2)
                else:
                    canvas.draw_rectangle(x1, x2, y1, y2)
            elif command == 'B':
                x = int(command_data[1])
                y = int(command_data[2])
                color = command_data[3]
                canvas.bucket_fill(x, y, color)

            print(canvas, file=output)


def main():
    parser = create_parser()
    args = parser.parse_args()
    output = args.stdout or args.output
    run_tool(args.input, output)


if __name__ == '__main__':
    main()
