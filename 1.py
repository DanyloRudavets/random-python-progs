#matrices multiplication tried -failed
k=[[0,1],[1,1]]
l=[]
c=[]
for i in k:
    for j in i:
        l.append(j)
        c.append(j)
print(l)

for i in range(3):
    c[0]=l[0]*l[0]+l[1]*l[2]
    c[1]=l[0]*l[1]+l[1]*l[3]
    c[2]=l[2]*l[0]+l[3]*l[2]
    c[3]=l[2]*l[1]+l[3]*l[3]
    l=c
print(c)