#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Albina Tileubergen-Thomas help from Daniel(instructor), Cheria Artis"

import random
import sys


def create_mimic_dict(filename):

    mimic_dict = {}
    f = open(filename, 'r')
    text = f.read()
    words = text.split()
    prev_word = ''
    for word in words:
        if prev_word not in mimic_dict:
            mimic_dict[prev_word] = [word]
        else:
            mimic_dict[prev_word].append(word)
        prev_word = word
    # print(mimic_dict)
    return mimic_dict


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    word = start_word
    for _ in range(200):
        print(word, end=' ')
        next_word_list = mimic_dict.get(word)
        if not next_word_list:
            next_word_list = mimic_dict[start_word]
        word = random.choice(next_word_list)


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
