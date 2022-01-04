#this doesn't fucking work
'''
M = [0] * 100000
i, found = 1, False
while not found:
    #print(i, max(M))
    rep = i
    while i < len(M):
        M[i]+=rep*10
        i+=rep
    if 33100000 in M:
        found = True
    i = rep + 1
print(M[index(33100000)])'''

#this is also shitty 
'''
def getDivisors(x):
    l = []
    for i in range(1,x//2+1):
        if x%i ==0:
            l.append(i)
    l.append(x)
    return l
i, found = 10000000, False
while found == False:
    r = sum(getDivisors(i))
    print(i,r)
    if r == 3310000:
        found = True
        print(i)
    i+=1
'''
def getPrimeDivisors(x):
    x_passed = x
    l = [1]
    repeats = 1
    while x%2 == 0:
        x//=2
        l.append(2**repeats)
        repeats+=1
    i = 3    
    while i < x_passed**.5+1:
        repeats = 1
        while x%i == 0:
            l.append(i**repeats)
            x//=i
            repeats+=1
        i+=2
    if l[len(l)-1] != x_passed:
        l.append(x_passed)
    if x not in l:
        l.append(x)
    #print(l)
    return sum(l)

#also didn't fucking work
'''
i, found = 3310000//2,False
while found == False:
    if getPrimeDivisors(i) >= 3310000:
        found = True
        print(i)
    i+=1
'''
import math

def GetDivisors(n):
    small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors

target = 33100000
part_one, part_two = None, None
i = 0
while not part_one or not part_two:
    i += 1
    divisors = GetDivisors(i)
    if not part_one:
        if sum(divisors) * 10 >= target:
            part_one = i
    if not part_two:
        if sum(d for d in divisors if i / d <= 50) * 11 >= target:
            part_two = i
print(part_one, part_two)


    