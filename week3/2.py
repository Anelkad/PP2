a = input().split()
b = []
for i in a:
    i=int(i)
    if i>0:
        b.append(i)
print(min(b))