#!/usr/bin/python3
"""Script that takes two string
first arguement is the name of the markdownfile
scond arguement is the output of the file name
"""


import sys
import os
import markdown

def main(args):
    if len(args) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_filename = args[0]
    output_filename = args[1]

    if not os.path.exists(input_filename):
        print(f"Missing {input_filename}", file=sys.stderr)
        sys.exit(1)

    with open(input_filename, 'r') as md_file:
        html = markdown.markdown(md_file.read())

    with open(output_filename, 'w') as html_file:
        html_file.write(html)

if __name__ == "__main__":
    main(sys.argv[1:])