# PROBLEMA TIRADO NO HackerRanK
# Link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

od = OrderedDict()
for i in range(int(input())):
    k, v = input().rsplit(' ', 1)

    if k in od:
        od[k] = int(od[k]) + int(v)
    else:
        od[k] = v

for k, v in od.items():
    print(k, v)
