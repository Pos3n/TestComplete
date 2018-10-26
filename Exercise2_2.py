#!/usr/bin/python
"""
Let's write a module (a pool of functions) that given a quite large text
(over than 2000 words) counts how frequent each word occurs in the text.
In particular the module should provide the function freqs that given a
filename and a number would return a list of words (with their frequencies)
that occur more than the given number; the list is sorted by frequency with
the higher first.

The text is read from a file and it is a real text with punctuation
(i.e., commas, semicolons, ...) that shouldn't be counted.

Note that words that differ only for the case should be considered the same.
"""

import functools
import sys

def getText(filename):
    with open(filename, encoding="utf-8", mode="r") as file:
        a=[]
        for line in file:
            b=line.split()
            a.extend(b)
    return a

def textAllign(listWord):
    o=[]
    for w in listWord:
        i=w.upper()
        o.append(i)
    return o



if __name__ == "__main__":
    print(textAllign(getText("C:/Users/luca-/Desktop/Cappuccetto_Rosso.txt")))




