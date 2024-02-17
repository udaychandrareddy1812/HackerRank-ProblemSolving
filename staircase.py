def stair(n):
    x = list()

    for i in range(1,n+1):
        a = i*'#'
        x.append(a)

    count = n - 1
    for i in x:
        a = (count*' ') + i
        count = count - 1
        print(a)

n = int(input())
stair(n)
