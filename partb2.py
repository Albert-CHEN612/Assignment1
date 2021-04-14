# Part B Task 2
import re
import os
import sys
import argparse

def preprocessing(text):
    # Remove all non-alphabetic characters
    text = re.sub(r"[^a-zA-Z \n\t]", '', text)
    # Convert all spacing characters such as tabs and newlines to whitespace
    text = text.replace("\t", " ")
    text = text.replace("\n", " ")
    # ensure that only one whitespace character exists between each word
    text = " ".join(text.split())
    # Change all uppercase characters to lower case
    text = text.lower()
    return text

def main():
    parser = argparse.ArgumentParser(description='Process a text file name.')
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    f = open("./cricket/" + args.filename)
    text = f.read()

    print(preprocessing(text))
main()
