from collections import defaultdict
N, X, Y = [int(i) for i in input().split()]
X, Y = X-1, Y-1

dd = defaultdict(int)
for i in range(N):
    for j in range(N):
        ans = min(abs(j - i),
                  abs(X - i)+1+abs(j-Y),
                  abs(Y - i)+1+abs(j-X))
        dd[ans] += 1

for i in range(1, N):
    print(dd[i] // 2)
