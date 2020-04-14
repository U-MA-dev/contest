N, M = [int(i) for i in input().split()]
AList = [int(i) for i in input().split()]

sumA = sum(AList)
ansList = list(filter(lambda x: x >= sumA / (4 * M), AList))

ans = "No"
if len(ansList) >= M:
    ans = "Yes"

print(ans)
