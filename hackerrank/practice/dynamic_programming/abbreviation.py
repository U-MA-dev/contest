#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the abbreviation function below.


def abbreviation(a, b):
    dp = [[False for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    dp[0][0] = True
    flag = True
    for ai in range(len(a)):
        if a[ai].islower() and flag:
            dp[ai + 1][0] = True
        else:
            flag = False

    for bi in range(len(b)):
        for ai in range(len(a)):
            if a[ai].isupper():
                if a[ai] == b[bi] and dp[ai][bi]:
                    dp[ai + 1][bi + 1] = True
            else:
                if a[ai].upper() == b[bi] and dp[ai][bi]:
                    dp[ai + 1][bi + 1] = True
                else:
                    dp[ai + 1][bi + 1] = dp[ai][bi + 1]

    ans = "YES" if dp[-1][-1] else "NO"
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
