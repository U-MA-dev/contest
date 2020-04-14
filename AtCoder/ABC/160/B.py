X = int(input())

ans = 0
ans += (X // 500) * 1000
ans += ((X % 500) // 5) * 5

print(ans)
