"""
My manager asked me to work on some String formation.
The short goal is for input 'A' and 'C'; expected output is 'T' and 'G' and vice versa.

"""


def char_strand(chars):
    new_string = ''
    letters = ['A', 'C', 'T', 'G']
    for s in chars:
        if s in letters:
            if s == 'A':
                new_string += 'T'
            if s == 'C':
                new_string += 'G'
            if s == 'T':
                new_string += 'A'
            if s == 'G':
                new_string += 'C'
    return new_string


char_strand("GTAT")
char_strand("AAAA")
char_strand("ATTGC")
