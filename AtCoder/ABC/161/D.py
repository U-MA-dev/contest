K = int(input())

dp = [[str(i)] for i in range(1, 10)]
count = 9

ansFlag = False
while (True):
    if K <= 9:
        break
    for i in range(9):
        numList = dp[i]
        newNumList = []
        for n in numList:
            lastNum = n[-1]
            if int(lastNum) >= 1:
                newNum1 = str(n) + str(int(lastNum) - 1)
                count += 1
                newNumList.append(newNum1)
                if count == K:
                    ansFlag = True
                    break

            newNum2 = str(n) + str(int(lastNum))
            count += 1
            newNumList.append(newNum2)
            if count == K:
                ansFlag = True
                break

            if int(lastNum) <= 8:
                newNum3 = str(n) + str(int(lastNum) + 1)
                count += 1
                newNumList.append(newNum3)
                if count == K:
                    ansFlag = True
                    break
        if ansFlag:
            break
        dp[i] = newNumList
    if ansFlag:
        break

ans = K
if K >= 10:
    ans = newNumList[-1]

print(ans)



