#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    q = 0
    for char in str:
        if q != n:
            new += str[q]
        q += 1
    return new
