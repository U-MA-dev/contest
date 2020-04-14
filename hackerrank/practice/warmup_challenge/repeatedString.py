#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    retVal = 0
    a = 0
    for i in range(len(s)):
        if s[i] == "a":
            a += 1
            if i <= (n % len(s)) - 1:
                retVal += 1
    retVal += (n // len(s)) * a
    return retVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
