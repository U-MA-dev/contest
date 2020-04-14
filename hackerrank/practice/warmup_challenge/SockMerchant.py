#!/bin/python3

import os
from collections import defaultdict

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    retVal = 0
    dd = defaultdict(int)
    for socket in ar:
        dd[socket] += 1
        if dd[socket] % 2 == 0:
            dd[socket] %= 2
            retVal += 1
    return retVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
