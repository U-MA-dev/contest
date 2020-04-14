from collections import defaultdict


def cmb(n, r):
    if n < r:
        return 0
    a = 1
    for i in range(n, n - r, -1):
        a *= i
    b = 1
    for i in range(1, r + 1):
        b *= i
    return int(a / b)


N = int(input())
AList = [int(i) for i in input().split()]

aDict = defaultdict(int)
for a in AList:
    aDict[a] += 1

ans = 0
for key in aDict:
    ans += cmb(aDict[key], 2)

for a in AList:
    print(ans - aDict[a] + 1)
