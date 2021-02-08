def largestAltitude(gain) -> int:
    a = 0 
    newa = [] 
    for i in gain:
        a += i 
        newa.append(a) 
    if max(newa) < 0: 
        return 0
    else:
        return max(newa)
print(largestAltitude([-4,-3,-2,-1,4,3,2]))