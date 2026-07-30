#!/usr/bin/env python3
def poly_integral(poly, C=0):
    if not isinstance(poly, list) or len(poly) == 0 or type(C) is not int:
        return None
    for coef in poly:
        if type(coef) not in (int, float):
            return None
    integral = [C]
    for i in range(len(poly)):
        coef = poly[i] / (i + 1)
        if coef.is_integer():
            integral.append(int(coef))
        else:
            integral.append(coef)
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()
    return integral