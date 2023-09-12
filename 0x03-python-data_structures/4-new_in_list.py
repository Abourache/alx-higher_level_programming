#!/usr/bin/python3
def new_in_list(my_list, idx, element):
        len_index = len(my_list) - 1
        cp = my_list.copy()
        if idx < 0:
            return None
        elif idx > (len_index):
            return None
        cp[idx] = element
        return (cp)
