add = 0
for i in range (1,101):
    sqr = (i)**2
    add = sqr + add
    #print(sqr)
print('Sum of squares: ',add)

result = 0
add2 = 0
for j in range (1,101):
    add2 = j + add2
    result = (add2)**2
    #print(add2)
print('Square of sums: ',result)
    
sub = result - add
print('Difference: ',sub)
