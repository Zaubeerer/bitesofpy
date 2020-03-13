from itertools import cycle
from string import ascii_letters


def sequence_generator():

    char_list = []
    for i, letter in enumerate(ascii_letters):
        char_list.append(i+1)
        char_list.append(letter.upper())

    return cycle(char_list.copy())
