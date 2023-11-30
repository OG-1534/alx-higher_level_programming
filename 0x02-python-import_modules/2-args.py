#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv) - 1
    if arg_len == 0:
        print("{} arguments.".format(arg_len))
    elif arg_len == 1:
        print("{} argument:".format(arg_len))
    else:
        print("{} arguments:".format(arg_len))
    for q in range(arg_len):
        print("{}: {}".format(q + 1, sys.argv[q + 1]))
