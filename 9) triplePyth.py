import math
for i in range(0,10001):
    for j in range(0,10001):
        add = (i**2 + j**2)
        c= math.sqrt(add)
        if (i + j + c) == 1000:
            print(i,j,c)
