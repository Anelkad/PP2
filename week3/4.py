a = input().split()
k=0
for i in a:
    i=int(i)
    if i>0:
        print(i)
    if i==0:
        k=k+1
for i in range(0,k):
    print(0)