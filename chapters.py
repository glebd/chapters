import argparse


def convert(a_line):
    """
    Converts YouTube-style chapter line into Audacity-style label line
    :param a_line: YouTube-style chapter line
    :return: Audacity-style label line
    """
    return a_line


if __name__ == '__main__':
    print('Chapters: convert YouTube chapters to Audacity labels')
    print("Copyright (C) 2023 Gleb Dolgich. All rights reserved.")
    print("Usage: chapters.py youtube.txt [-o audacity.txt]")

    parser = argparse.ArgumentParser(prog='Chapters', description='Converts YouTube markers to Audacity labels')
    parser.add_argument('input', help='Input file containing YouTube chapter markers')
    parser.add_argument('-o', '--output', help='Output file name (uses standard output if none)')

    args = parser.parse_args()

    print(f"Input file: {args.input}")
    if args.output is not None:
        print(f"Output file: {args.output}")

    with open(args.input) as input_file:
        for youtube_line in input_file:
            audacity_line = convert(youtube_line)
            print(audacity_line, end='')
