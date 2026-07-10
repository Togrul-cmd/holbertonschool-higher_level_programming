#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string.isalpha() or roman_string is None:
        return 0
    romans = {'I' : 1, 'IV' : 4, 'V' : 5, 'IX' : 9, 'X' : 10, 'XL' : 40, 'L' : 50, 'XC' : 90, 'C' : 100, 'CD' : 400, 'D' : 500, 'CM' : 900, 'M' : 1000}
    index = 0
    num = 0
    while index < len(roman_string):
        str = roman_string[index]
        while str in romans and index < len(roman_string):
            index += 1
            if index < len(roman_string):
                str += roman_string[index]
        if len(str) > 1 and not str in romans:    
            num += romans[str[:-1]]
        else:
            num += romans[str]
    return num
        
