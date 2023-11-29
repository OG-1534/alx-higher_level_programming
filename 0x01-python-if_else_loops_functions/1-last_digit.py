#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdigit = abs(number) % 10
if number < 0:
    lstdigit = -(lstdigit)
string = "Last digit of {} is {}".format(number, lstdigit)
if lstdigit > 5:
    print(f"{string} and is greater than 5")
elif lstdigit == 0:
    print(f"{string} and is 0")
elif lstdigit < 6:
    print(f"{string} and is less than 6 and not 0")
