n,k = map(int, input().split())
bill = list(map(int, input().split()))
b = int(input())

bill.pop(k)

total = 0
for i in bill:
    total = total + i

x = int(total/2)

if b==x:
    print('Bon Appetit')
elif b!=x:
    print(b-x)
