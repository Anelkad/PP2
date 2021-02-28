#https://www.hackerrank.com/challenges/re-start-re-end/problem
import re
s = input()
trial = input()
m = re.search(trial, s)
pattern = re.compile(trial)
if not m: print("(-1, -1)")
while m:
    print("(%d, %d)" % (m.start(),m.end()-1))
    m = pattern.search(s, m.start() + 1)
