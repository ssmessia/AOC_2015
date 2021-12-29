raw='''Faerun to Norrath = 129
Faerun to Tristram = 58
Faerun to AlphaCentauri = 13
Faerun to Arbre = 24
Faerun to Snowdin = 60
Faerun to Tambi = 71
Faerun to Straylight = 67
Norrath to Tristram = 142
Norrath to AlphaCentauri = 15
Norrath to Arbre = 135
Norrath to Snowdin = 75
Norrath to Tambi = 82
Norrath to Straylight = 54
Tristram to AlphaCentauri = 118
Tristram to Arbre = 122
Tristram to Snowdin = 103
Tristram to Tambi = 49
Tristram to Straylight = 97
AlphaCentauri to Arbre = 116
AlphaCentauri to Snowdin = 12
AlphaCentauri to Tambi = 18
AlphaCentauri to Straylight = 91
Arbre to Snowdin = 129
Arbre to Tambi = 53
Arbre to Straylight = 40
Snowdin to Tambi = 15
Snowdin to Straylight = 99
Tambi to Straylight = 70'''
import itertools
raw = [r.split(' = ')for r in raw.splitlines()]
C, D = [],{}
for r in raw:
    cities = r[0].split(' to ')
    if cities[0] not in C:
        C.append(cities[0])
    if cities[1] not in C:
        C.append(cities[1])
    if cities[0]+cities[1] not in D.keys():
        D[cities[0]+cities[1]] = int(r[1])
        D[cities[1]+cities[0]] = int(r[1])
        
print(D)
print(C)
R =  [list(p) for p in itertools.permutations(C)]
shortest, longest = 10000000,0
s,l = [],[]
for p in R:
    distance = 0
    for i in range(1,len(p)):
        distance+=D[p[i-1]+p[i]]
    if distance < shortest:
        shortest = distance
        s.append(p)
    if distance > longest:
        longest = distance
        l.append(p)
print(shortest, s.pop(), longest, l.pop())
        




