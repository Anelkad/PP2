#https://www.hackerrank.com/challenges/introduction-to-regex/problem
import re
n = int(input())
for i in range(n):
    x = re.match("^[+-]?\d*[.]\d+$", input())
    print(bool(x))