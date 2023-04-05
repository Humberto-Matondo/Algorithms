# PROBLEMA TIRADO NO HackerRanK
# Link:  https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

n = int(input())
student = namedtuple('student', input())
lst = []
s = 0

for i in range(n):
    x = input().split()
    s1 = student(*x)
    lst.append(s1)

for i in range(n):
    s += int(lst[i].MARKS)
print(s/n)
