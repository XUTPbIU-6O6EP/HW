print ('Введите субсидии и количество голов скота')
subsidii=int(input())
golovi=int(input())
for a in range(1, subsidii//20):          
    for b in range((subsidii-a*20)//10):  
        c=golovi-a-b                      
        if a*20+b*10+c*5==subsidii:
            print(a, b, c)

