#!/usr/bin/python3
for frst_num in range(0, 10):
    for sec_num in range(frst_num + 1, 10):
        if frst_num == 8 and sec_num == 9:
            print("{}{}".format(frst_num, sec_num))
        else:
            print("{}{}, ".format(frst_num, sec_num, end=''))
