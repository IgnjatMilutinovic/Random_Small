lista1=[2,1,4,5,7,3,2,1,4,6,7,9]
lista2=[]
x=0
y=1
m=0
if lista1[-1]<0:
    lista1.append(lista1[-1] - 1)
else:
    lista1.append(0)
while y!=len(lista1):
    if lista1[x]<lista1[y]:
        x+=1
        y+=1
    else:
        lista2.append(lista1[m:y])
        m=x+1
        x+=1
        y+=1
print(lista2)
a=lista2[0]
for e in range(len(lista2)):
    if len(lista2[e])>len(a):
        a=lista2[e]
print("Najduzi podniz rastucih elemenata je : ", a)
input("Pritisnite ENTER da izadjete")
