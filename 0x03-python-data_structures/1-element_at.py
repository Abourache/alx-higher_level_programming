#!/usr/bin/python3
def element_at(my_list, idx):
        if idx < 0:
                return None
        elif idx > 4:
                return None
        return ("{:d}".format(my_list[idx]))
