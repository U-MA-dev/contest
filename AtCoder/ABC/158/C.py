import math

A, B = [int(i) for i in input().split()]
taxA, taxB = [0.08, 0.1]

ans = -1
for i in range(1250):
    if math.floor(i * taxA) == A and math.floor(i * taxB) == B:
        ans = i
        break

print(ans)
