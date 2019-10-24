print ('Vvedite kol-vo drobinok, ih uron: \nv vide dorbi, sna4ala 4islitel, \npotom snamematel')
Z=int(input())
i=0
chis=[]
znam=[]
while i<Z:
    x=int(input())
    y=int(input())
    chis.append(x)
    znam.append(y)
    i+=1
maximum=max(znam)
a=False
i=0
znam1=maximum
while a==False:
    b=True
    for i in znam:
        if znam1%i!=0:
            b=False
    if b==True:
        a=True
    else:
        znam1+=maximum
chis1=[]
for i in range (len(chis)):
    chis1.append(int(znam1/znam[i]*chis[i]))
chis2=sum(chis1)
minimum=min(znam1,chis2)
a=True
while a:
  for i in range(minimum,1,-1):
    b=False
    if znam1%i==0 and chis2%i==0:
      znam1/=i
      chis2/=i
      b=True
    a=b
print(str(int(chis2))+"/"+str(int(znam1)))
