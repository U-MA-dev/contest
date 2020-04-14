from collections import defaultdict

K = int(input())


def calcGcd(a, b):
    large = max(a, b)
    small = min(a, b)
    while (True):
        num = large % small
        large = small
        small = num
        if small == 0:
            return large


ans = 0
dd = defaultdict(int)
for i in range(1, K + 1):
    for j in range(1, K + 1):
        dd[calcGcd(i, j)] += 1

for num in dd.keys():
    for k in range(1, K + 1):
        ans += calcGcd(num, k) * dd[num]

print(ans)
