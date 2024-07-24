import argparse
import sys

location = ""
parser = argparse.ArgumentParser(
    description='Coding Challenge Word Count program')
parser.add_argument(
    '-l', '--lines', help='print the newline count', action='store_true')
parser.add_argument(
    '-w', '--words', help='print the word count', action='store_true')
parser.add_argument(
    '-c', '--bytes', help='print the byte count', action='store_true')
parser.add_argument(
    '-m', '--chars', help='print the character count', action='store_true')
parser.add_argument('-L', '--max-line-length',
                    help='print the maximum display width', action='store_true')
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'),
                    default=(None if sys.stdin.isatty() else sys.stdin))
argslist = parser.parse_args()

raw_text = None
output = {}


def countLines():
    if argslist.lines:
        num_lines = 0
        if len(raw_text) > 0:
            num_lines = 1
        for i in raw_text:
            if i == '\n':
                num_lines += 1
        output.update({"lines": num_lines})


def countWords():
    if argslist.words:
        num_characters = 0
        previous = None
        for i in raw_text:
            if i != ' ' and i != '\n':
                if previous == ' ' or previous == '\n' or previous == None:
                    num_characters += 1
            previous = i
        output.update({"words": num_characters})


def countBytes():
    if argslist.bytes:
        num_characters = 0
        for i in raw_text:
            num_characters += len(i.encode("utf8"))
        output.update({"bytes": num_characters})


def countChars():
    if argslist.chars:
        num_characters = 0
        for i in raw_text:
            num_characters += 1
        output.update({"chars": len(raw_text)})


if argslist.infile:
    raw_text = argslist.infile.read()
    countLines()
    countWords()
    countBytes()
    countChars()
    print(output)
else:
    print("You have not supplied a file to read.")
