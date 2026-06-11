#!/usr/bin/python3
def rev(a):
    return a // 10 + a % 10 * 10

for i in range(100):
    if i % 10 == 0 or rev(i) < i or i % 11 == 0:
        continue
    elif i == 89:
        print(i)
    else:
        print('{:02d}'.format(i), end=', ')
