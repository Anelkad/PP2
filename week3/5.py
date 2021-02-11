a = input().split()
k = int(input())
k = k%len(a)
if k<0:
    k = abs(k)
    print(*a[k:])
    print(*a[0:k])
    exit()
 
if k>=0:
    k = abs(k)
    print(*a[-k:])
    print(*a[0:-k])