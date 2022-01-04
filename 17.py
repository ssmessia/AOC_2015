raw='''43
3
4
10
21
44
4
6
47
41
34
17
17
44
36
31
46
9
27
38'''
raw = sorted([int(r) for r in raw.splitlines()])
import itertools
total, min_total, fewest = 0,0,len(raw)

for i in range(4,len(raw)):
    C = list(itertools.combinations(raw, i))
    for c in C:
        if sum(c) == 150:
            total+=1
            if len(c) < fewest:
                fewest = len(c)
            if len(c) <= fewest:
                min_total+=1
print(total, min_total)

