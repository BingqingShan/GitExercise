import random


def num_vowels(item):
    vowel=0
    for i in item:
        if i in ["a", "e", "i", "o", "u"]:
            vowel += 1
    if vowels >= 2:
        return True
