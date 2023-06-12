#!/usr/bin/python3

def element_at(my_list, idx):
    length_of_list = len(my_list)
    if (idx > length_of_list):
        return None
    elif (idx < 0):
        return None
    else:
        return my_list[idx]