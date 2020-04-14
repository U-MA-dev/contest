#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    ans = 0
    dd = defaultdict(int)
    for i in range(len(s)):
        for j in range(i, len(s)):
            word = s[i:j + 1]
            sortedWord = "".join(sorted(word))
            ans += dd[sortedWord]
            dd[sortedWord] += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
