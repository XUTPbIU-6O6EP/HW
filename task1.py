print ('Введите min и max значение и я посчитаю для \nВас сумму цифр между ними включая min и max')
a=input()
b=input()
S=0
i=int(a)
while i<int(b):
    i=i+1
    S=S+i
S=S+int(a)
print ('Сумма чисел =', S)



