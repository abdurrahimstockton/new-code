"""
My manager asked me to work on some String formation.
The short goal is for input 'A' and 'C'; expected output is 'T' and 'G' and vice versa.
Please suggest if the following code is doable. Please suggest for efficiency.
"""


def char_strand(chars):
    new_string = ''
    letters = ['A', 'C', 'T', 'G']
    for s in chars:
        if s in letters:
            if s == 'A':
                new_string += 'T'
            elif s == 'C':
                new_string += 'G'
            elif s == 'T':
                new_string += 'A'
            elif s == 'G':
                new_string += 'C'
    return new_string


char_strand("GTAT")
char_strand("AAAA")
char_strand("ATTGC")


"""Code suggestions from my Ghost_Master"""


def strand(chars):
    # Create a dictionary to store complementary nucleotides
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Initialize an empty string to store the complementary DNA strand
    complementary_strand = ""

    # Iterate over each character in the input DNA string
    for nucleotide in chars:
        # Look up the complementary nucleotide and append it to the complementary strand
        complementary_strand += complements[nucleotide]

    return complementary_strand

