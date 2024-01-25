''' Question No. 62 (Practise set-3) '''
from functools import reduce

li=[(2, 7), (2, 6), (1, 8), (4, 9)]
t=[]
for i in li:
    t.append((reduce(lambda x,y:x*y,i)))

print(tuple([max(t),min(t)]))
