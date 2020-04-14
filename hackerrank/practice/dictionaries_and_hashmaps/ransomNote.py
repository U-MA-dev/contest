#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    ans = "Yes"
    dd = defaultdict(int)

    for word in magazine:
        dd[word] += 1
    for word in note:
        if dd[word] == 0:
            ans = "No"
            break
        else:
            dd[word] -= 1
    print(ans)


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
