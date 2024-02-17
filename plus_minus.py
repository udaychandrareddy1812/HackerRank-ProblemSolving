def plusminus(n, arr):
    pos = 0
    neg = 0
    zero = 0

    for i in arr:
        if i > 0:
            pos = pos + 1
        elif i < 0:
            neg = neg + 1
        elif i == 0:
            zero = zero + 1

    print(round((pos/n),6))
    print(round((neg/n),6))
    print(round((zero/n),6))

n = int(input())
arr = list(map(int, input().split()))

plusminus(n, arr)
