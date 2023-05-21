import argparse
import re

# '00:00 Intro' -> '00:00 Intro', '00', '00', 'Intro'
youtube_line_regex = re.compile(r"^(\d+):(\d+)\s+(.*)$")


def convert(lines, fmt):
    """
    Converts YouTube-style chapter lines into other formats
    :param lines: All lines from the input file in YouTube chapter format (MM:SS Title)
    :param fmt: Output format: audacity, csv
    :return: Converted chapter lines
    """
    out_lines = []
    for line in lines:
        match = youtube_line_regex.match(line)
        if match is None:
            print(f"Invalid input line: '{line}'")
            exit(-1)
        mins = match[1]
        secs = match[2]
        minutes = float(mins)
        seconds = float(secs)
        timestamp = minutes*60 + seconds
        label = match[3]
        if fmt == 'audacity':
            out_line = f"{timestamp:.6f}\t{timestamp:.6f}\t{label}\n"
        elif fmt == 'csv':
            out_line = f"{label},{mins}:{secs}\n"
        else:
            print(f"Unknown output format: {fmt}")
            exit(-2)
        out_lines.append(out_line)
    return out_lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='chapters',
                                     description='Converts YouTube markers to other formats',
                                     epilog='Copyright (C) 2023 Gleb Dolgich. All rights reserved.')
    parser.add_argument('input', help='Input file containing YouTube chapter markers')
    parser.add_argument('-f', '--format', help='Target format: audacity, csv (default)', default='csv')
    parser.add_argument('-o', '--output', help='Output file name (otherwise uses standard output)')

    args = parser.parse_args()

    with open(args.input) as f:
        all_lines = f.readlines()
        converted_lines = convert(all_lines, args.format)
    for line in converted_lines:
        print(line, end='')
