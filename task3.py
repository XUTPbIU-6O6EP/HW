print ('Введите высоту пирамиды')
a=input()
c=str('@@')
b=str('@')
m=int(a)
i=0
while i<int(a):
    print (int(m)*str(' '),b)
    m=int(m)-1
    b=b+str(c)
    i=i+1
