H, W, K = [int(i) for i in input().split()]
field = [[int(i) for i in input()] for _ in range(H)]


def calcSum(arrs, start, goal):
    ans = 0
    for arr in arrs:
        ans += sum(arr[start:goal+1])
    return ans


ans = float("inf")
for ci in range(2 ** (H - 1)):
    cutList = [(H - 1) - i for i,
               n in enumerate(format(ci, "b").zfill(H - 1)) if n == "1"]
    cutList.append(H)
    cutList.sort()


print(ans)
