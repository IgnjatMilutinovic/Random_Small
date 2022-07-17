a="aezea"
x=""
e=-1
while e!=-len(a)-1:
    x+=a[e]
    e-=1
print(a)
print(x)
if a==x:
    print("Ova rec je palindrom")
else:
    print("Ova rec nije palindrom")
