N, A, B = [int(i) for i in input().split()]

ball = (N // (A + B)) * A
rest = N % (A + B)
ball += min(A, rest)

print(ball)
