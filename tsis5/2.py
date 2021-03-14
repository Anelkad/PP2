f=open('input.txt','r')
n=int(input())
k=0
for i in f:
    print(i)
    k+=1
    if k>=n:
        break