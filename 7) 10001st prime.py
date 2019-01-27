num = 0

for m in range (2,100000):
    
    if all((m % i) != 0 for j in range (2,m)):
        num = num +1
    
        if num == 10001:
            print('num', m)

        
