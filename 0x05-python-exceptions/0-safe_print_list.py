#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    str_len = 0
    for b in range(x):
        try:
            print("{}".format(my_list[b]), end="")
            str_len += 1
        except IndexError:
            break
    print()
    return str_len
