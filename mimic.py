
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
