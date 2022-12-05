#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    temp_list = []
    y = 0

    for x in my_list:
        if my_list.index(x) == idx:
            temp_list.append(element)
        else:
            temp_list.append(my_list[y])
        y += 1

    return temp_list
