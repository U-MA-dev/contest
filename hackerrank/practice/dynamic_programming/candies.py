#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.


def candies(n, arr):
    dp = [0 for _ in range(n + 1)]

    for i, score in enumerate(arr):
        if i != 1:
            if score <= arr[i - 1]:
                dp[i + 1] = min(0, dp[i] - 1)
            else:
                dp[i + 1] = dp[i] + 1

    border = min(dp)
    ans = sum(dp) + (1 - border) * n
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
