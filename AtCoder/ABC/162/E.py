from collections import defaultdict

N, K = [int(i) for i in input().split()]
mod = 10 ** 9 + 7
dd = defaultdict(int)

ans = 0
for i in range(K, 0, -1):
    dd[i] = pow(K // i, N, mod)
    for temp in range(i * 2, K + 1, i):
        dd[i] -= dd[temp]
    ans += dd[i] * i
    ans %= mod
print(ans)
