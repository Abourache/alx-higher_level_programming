#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len_index = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > (len_index):
        return None
    my_list[idx] = element
    return (my_list)
