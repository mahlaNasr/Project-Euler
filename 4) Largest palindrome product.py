alist = []
new = [] 

for num2 in range (100, 999):
    for num1 in range (100,999):
        n = str(num1*num2)
        #print(str(num1),str(num2),n)
        #alist.append(n)


        if n == n[::-1]:
            #print(n)
            
            alist.append(int(n)) #'''converting the number into integer


print(max(alist))   #'''finds the max integer number 

