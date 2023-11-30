#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    for q in sys.argv:
        if q != sys.argv[0]:
            sum += int(q)
    print("{}".format(sum))
