#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.


def countTriplets(arr, r):
    ans = 0
    dd = defaultdict(int)
    for num in arr:
        dd[num] += 1

    for num in sorted(dd.keys()):
        if r == 1:
            ans += int(dd[num] * (dd[num] - 1) *
                       (dd[num] - 2) // 6) if dd[num] >= 3 else 0
        else:
            ans += dd[num] * dd[num * r] * dd[num * r * r]
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(countTriplets(arr, n))

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nr = input().rstrip().split()

    # n = int(nr[0])

    # r = int(nr[1])

    # arr = list(map(int, input().rstrip().split()))

    # ans = countTriplets(arr, r)

    # fptr.write(str(ans) + '\n')

    # fptr.close()
