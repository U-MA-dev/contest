#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):
    retVal = 0
    h = 0
    for i in range(n):
        if s[i] == "U":
            if h == -1:
                retVal += 1
            h += 1
        else:
            h -= 1
    return retVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
