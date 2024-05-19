n = int(input())

grades = list()

for i in range(n):
    marks = int(input())
    grades.append(marks)

for i in grades:
    if (i == 100):
        print(100)
    elif (i >= 40 and i < 100):
        x = i % 10
        j = int(i / 10)
        y = j % 10
        
        if (x>=0 and x<5):
            multi = (y*10) + (5)
        elif (x>=5 and x<=9):
            multi = (y*10) + (10)
        
        if (multi - i < 3):
            print(multi)
        else:
            print(i)
    elif (i < 40):
        if (i==38 or i==39):
            print(40)
        elif (i < 38):
            print(i)
