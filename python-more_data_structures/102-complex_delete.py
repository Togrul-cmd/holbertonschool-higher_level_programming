#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = [key for key in a_dictionary if a_dictionary[key] == value]
    for i in key_list:
        del a_dictionary[i]
    return a_dictionary
