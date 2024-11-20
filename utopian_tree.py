t = int(input())
    
for i in range(t):
    n = int(input())
    
    height = 1
    for j in range(1, n+1):
        if (j%2!=0):
            height = (2*height)
        elif (j%2==0):
            height = height + 1
            
    print(height)
