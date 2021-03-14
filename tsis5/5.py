f=open("input.txt","r")
l=list()
for x in f:
    l.extend(x.split())
la=sorted(l,key=lambda x:len(x),reverse= True)
print(la[0])