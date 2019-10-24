print ('Vvedite') 
N=int(input()) 
i=1; 
a_list=[] 
while i<=N:
    if N%i==0:
        a_list.append(i)
        i+=1        
    else:
        i+=1
if len(a_list)==2 or len(a_list)==1:
    a_list.append("ACHTUNG")
print(a_list)
