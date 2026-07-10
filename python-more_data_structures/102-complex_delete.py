#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = [key for key, val in a_dictionary.items() if val == value]
    for i in key_list:
        del a_dictionary[i]
    return a_dictionary
