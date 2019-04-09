import random
import json


def num_vowels(item):#define a function
    vowel=0 #set up the initial value of variable vowel
    for i in item: #start a for loop
        if i in ["a", "e", "i", "o", "u"]: #if the character is vowel
            vowel += 1 #vowel is added up by 1
    if vowels >= 2:
        return True

