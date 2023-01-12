"""
generate_scales.py

todo:
Define all scales in a single file?
Right a few more manually and extract commonalities.
Start with C major left and right hands.
Generate all scales, arepggios and broken chords in Trinity book.
Use interval pattern, apply to given keys.
    And/or exploit Lilypond transpose command.
Permute the letters starting on given root.
Add fingering.
"""

from enum import Enum

Hands = Enum('Hands', ['LEFT', 'RIGHT', 'BOTH'])
letters = list('abcdefg')

def main():
    scale = 'C major'
    letter = scale[0].lower()

    for letter in letters:
        x = get_letters_starting_on(letter)
        print(x)

def generate_scale(hand, octaves=1):
    pass

def get_letters_starting_on(letter):
    i = letters.index(letter)
    return letters[i:] + letters[:i]

if __name__ == '__main__':
    main()
