def subtractProductAndSum(n: int) -> int:
    su, mu = 0,1
    for i in list(map(int,str(n))):
        su+=int(i)
        mu*=int(i)
    return mu-su
print(subtractProductAndSum(234))  