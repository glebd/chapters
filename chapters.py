import argparse

if __name__ == '__main__':
    print('Chapters: convert YouTube chapters to Audacity labels')
    print("Copyright (C) 2023 Gleb Dolgich. All rights reserved.")
    print("Usage: chapters.py youtube.txt [-o audacity.txt]")

    parser = argparse.ArgumentParser(prog='Chapters', description='Converts YouTube markers to Audacity labels')
    parser.add_argument('input', help='Input file containing YouTube chapter markers')
    parser.add_argument('-o', '--output', help='Output file name (uses standard output if none)')

    args = parser.parse_args()

    print(f"Input file: {args.input}")
    if args.output is None:
        print("Output: stdout")
    else:
        print(f"Output file: {args.output}")
