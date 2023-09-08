#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sn = sys.argv[0]
    args = sys.argv[1:]
    enum = enumerate(args, 1)
    if len(args) == 1:
        print("{} argument:".format(len(args)))
        for count, files in enum:
            print("{}: {}".format(count, files))
    else:
        print("{} arguments:".format(len(args)))
        for count, files in enum:
            print("{}: {}".format(count, files))
