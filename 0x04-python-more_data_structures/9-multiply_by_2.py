#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = dict(a_dictionary)
    for i in a_dictionary:
        dictionary[i] = dictionary[i] * 2
    return dictionary
