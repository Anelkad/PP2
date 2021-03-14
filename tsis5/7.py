f=open("input.txt","r")
l=list()
for x in f:
    l.extend(x.split())
a=dict()
for x in l:
    if x not in a.keys():
        a[x]=1
    else:
        a[x]=a[x]+1
li=list(a.items())
li.sort(key=lambda x: x[0])
li.sort(key=lambda x:(x[0]).lower())
li.sort(key=lambda x:x[1], reverse= True)
f=open("output.txt","w")
b=list()
for x in li:
    b.append(x[0]+": "+str(x[1]))

f.write("\n".join(b))