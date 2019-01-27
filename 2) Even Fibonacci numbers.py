def fibonacci():
    sum_ = 0
    num1 = -1
    num2 = 1
    add = num1 + num2
    
    while sum_ < 4000000:
        num1 = num2
        num2 = add
        add = num1 + num2

        if (add % 2) == 0:
            sum_ = sum_ + add        
    
    print('sum:',sum_) 
        

fibonacci()
