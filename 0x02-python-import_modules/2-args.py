#!/usr/bin/python3

import sys

if __name__ == "__main__":
    le = len(sys.argv)

    if le == 1:
        print("{:d} arguments.".format(le - 1))
    elif le == 2:
        print("{:d} argument:".format(le - 1))
    else:
        print("{:d} arguments:".format(le - 1))
    for i in range(1, le):
        print("{:d}: {:s}".format(i, sys.argv[i]))
