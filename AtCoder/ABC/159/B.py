S = input()
N = len(S)
S_1 = S[0:int((N - 1)/2)]
S_2 = S[int((N + 3)/2) - 1:N + 1]

ans = "No"
if S == S[::-1] and S_1 == S_1[::-1] and S_2 == S_2[::-1]:
    ans = "Yes"

print(ans)
