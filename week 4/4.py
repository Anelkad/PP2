import re
n = int(input())
for i in range(n):
    x = re.match("^[7|8|9]\d{9}$", input())
    if x:
        print("YES")
    else:
        print("NO")