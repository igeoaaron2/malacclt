#! /usr/bin/env python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number",
                    type=int)
parser.add_argument("-word", help="write a word",
                    type=str)
parser.add_argument("-thing", help="thing",
                    type=int)
args = parser.parse_args()
print(args.square**2)
if str(args.word) == "None":
    x = 1
else:
    print("You wrote " + str(args.word))
if str(args.thing) == "None":
    y = 1
else:
    print("Your number + 1 equals " + str(args.thing + 1))