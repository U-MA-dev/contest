from collections import defaultdict

N = int(input())
S = input()

dd = defaultdict(int)
rList = [0]
gList = [0]
bList = [0]
for i in range(N):
    if S[i] == "R":
        rList.append(rList[-1] + 1)
        gList.append(gList[-1])
        bList.append(bList[-1])
    elif S[i] == "G":
        rList.append(rList[-1])
        gList.append(gList[-1] + 1)
        bList.append(bList[-1])
    else:
        rList.append(rList[-1])
        gList.append(gList[-1])
        bList.append(bList[-1] + 1)

ans = 0
for i in range(N):
    for j in range(i, N):
        if S[i] == S[j]:
            continue
        tl = ["R", "G", "B"]
        tl.remove(S[i])
        tl.remove(S[j])
        target = tl[0]
        if target == "R":
            ans += rList[-1] - rList[j + 1]
        elif target == "G":
            ans += gList[-1] - gList[j + 1]
        else:
            ans += bList[-1] - bList[j + 1]

        diff = abs(i - j)
        if j + diff <= N - 1 and S[j + diff] == target:
            ans -= 1

print(ans)
