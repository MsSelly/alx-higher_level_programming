#!/usr/bin/python3

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None

    largest = my_list[0]
    for h in range(len(my_list)):
        if my_list[h] > largest:
            largest = my_list[h]

    return largest
