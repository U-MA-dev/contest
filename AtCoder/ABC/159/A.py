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


N, M = [int(i) for i in input().split()]
ans = cmb(N, 2) + cmb(M, 2)

print(ans)
