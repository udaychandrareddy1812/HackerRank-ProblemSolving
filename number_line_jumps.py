x1, v1, x2, v2 = map(int, input().split())

if (v2-v1)==0:
    print('NO')
    exit()

n = (x1-x2)/(v2-v1)

int_part = int(n)
float_part = n - int_part

if (n>0) and (float_part==0):
    print('YES')
else:
    print('NO')
