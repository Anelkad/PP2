#https://www.hackerrank.com/challenges/hex-color-code/problem
import re
for i in range(int(input())):
    s = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if s: print(*s, sep = "\n")