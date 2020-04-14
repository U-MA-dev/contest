N, K = [int(i) for i in input().split()]

ans = min(N % K, K - (N % K))
print(ans)
