#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    pr = 1
    if b < 0:
        while b:
            pr /= a
            b += 1
    else:
        while b:
            pr *= a
            b -= 1
    return pr
