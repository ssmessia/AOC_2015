raw='''Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3
Butterscotch: capacity 0, durability 5, flavor -3, texture 0, calories 3
Chocolate: capacity 0, durability 0, flavor 5, texture -1, calories 8
Candy: capacity 0, durability -1, flavor 0, texture 5, calories 8'''
raw = raw.splitlines()
D={}
for r in raw:
    r = r.split()
    D[r[0]] = [int(r[2][:-1]), int(r[4][:-1]), int(r[6][:-1]), int(r[8][:-1]), int(r[10])]
print(D)
V = list(D.values())
print(V)
def getValues(v,idx,i,j,k,l):
    return max(v[0][idx]*i+v[1][idx]*j+v[2][idx]*k+v[3][idx]*l,0)
highest, highest_c = 0, 0
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            for l in range(1,101):
                if i+j+k+l == 100:
                    c = getValues(V,0,i,j,k,l)
                    d = getValues(V,1,i,j,k,l)
                    f = getValues(V,2,i,j,k,l)
                    t = getValues(V,3,i,j,k,l)
                    cal = getValues(V,4,i,j,k,l)
                    total = c*d*f*t
                    if total > highest:
                        highest = total
                    if cal == 500:
                        if total > highest_c:
                            highest_c = total
print(highest, highest_c)