#!/usr/bin/python3
def remove_char_at(str, n):
    cp = ''
    for i in range(len(str)):
        if i == n:
            continue
        cp += str[i]
    return cp
