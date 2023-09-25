#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        i = 0
        slic = 0

        for i in range(0, x):
                try:
                        print("{:d}".format(i + 1), end = " ")
                        slic += 1
                        if (i + 1) == x:
                                print(end="\n")
                except:
                        continue

        return slic
