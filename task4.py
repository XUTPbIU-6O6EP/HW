print ('Введите число элементов, N')
N=int(input())
i=S=m=0
d=1
a_list=[]
str=''
while i<N:
    a_list.append(S)
    S=d+m
    d=m
    m=S
    i+=1
for i in range (N):
    str+=repr(a_list[i])
    if i<N-1:
         str+=', '
print(str)

