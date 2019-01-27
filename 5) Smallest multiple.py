counter = False
end = False
 
num = 1  #the smallest +ve number

while counter == False:
    for i in range(2,21):  # i => the numbers between 1 - 20
        if end == False:
            if num % i != 0:
                end = True
            if i == 20:
                counter =True
                print('number: ',num)

        #if num == 2520:
            #counter = True

 
        
    num = num + 1
    if num%1000000 == 0:
        print(num)
    end = False
            
    
    
