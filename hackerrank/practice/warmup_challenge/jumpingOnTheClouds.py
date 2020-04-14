#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c):
    retVal = 0
    i = 0
    while (True):
        if i == len(c) - 2:
            retVal += 1
            break
        if i == len(c) - 1:
            break
        i += 2 if c[i + 2] == 0 else 1
        retVal += 1
    return retVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
