#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.


def maxSubsetSum(arr):
    dp = [0 for _ in range(len(arr))]
    for i, num in enumerate(arr):
        if i < 2:
            dp[i] = max(dp[i], num)
        elif i == 2:
            dp[i] = max(dp[i], num, dp[i-2] + max(num, 0))
        else:
            dp[i] = max(dp[i], num, dp[i-2] + max(num, 0),
                        dp[i-3] + max(num, 0))
    return max(dp[-1], dp[-2])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
