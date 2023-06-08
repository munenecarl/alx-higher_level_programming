#!/usr/bin/python3

import string

def print_uppercase_chars(chars):
    if len(chars) == 0:
        print()
        return
    print(chars[0], end='')
    print_uppercase_chars(chars[1:])
uppercase_chars = string.ascii_uppercase
print_uppercase_chars(uppercase_chars)
