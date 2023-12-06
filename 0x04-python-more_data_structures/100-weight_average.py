#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        denominator = 0
        for i in my_list:
            number += (i[0] * i[1])
            denominator += (i[1])
        return (number/denominator)
    return 0
