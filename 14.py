raw='''Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds.'''
raw = raw.splitlines()
D = {}
for r in raw:
    r =r.split()
    D[r[0]] = [int(r[3]),int(r[6]),int(r[13]),0,0]
print(D)
def distCalc(l,t):
    reps = t//(l[1]+l[2])
    rem = t%(l[1]+l[2]) 
    return l[0]*l[1]*reps + (min(rem,l[1])*l[0])
furthest = 0
for d in D.keys():
    temp = distCalc(D[d],2503)
    if temp > furthest:
        print(d, temp)
        furthest = temp

for i in range(1,2504):
    furthest = 0
    for d in D.keys():
        D[d][4] = distCalc(D[d],i)
        if D[d][4] >= furthest:
            furthest = D[d][4]
    for d in D.keys():
         if D[d][4] == furthest:
             D[d][3]+=1
print(D)
    



    