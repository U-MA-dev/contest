K, N = [int(i) for i in input().split()]
AList = sorted([int(i) for i in input().split()])

ans = float("inf")
for i in range(N):
    if i == 0:
        ans = min(ans, K - abs(K + AList[i] - AList[N-1]),
                  K - abs(AList[i] - AList[i + 1]))
    elif i == N - 1:
        ans = min(ans, K - abs(AList[i] - AList[i - 1]),
                  AList[0] + AList[i])
    else:
        ans = min(ans, K - abs(AList[i] - AList[i - 1]),
                  K - abs(AList[i] - AList[i + 1]))

print(ans)
