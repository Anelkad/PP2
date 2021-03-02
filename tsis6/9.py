a = int(input())
print(sum([a%i==0 for i in range(2,int(a**0.5)+1)])==0 and a!=1)