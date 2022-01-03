raw="vzbxkghb"
test="aabbccdef"
#raw=test
P = [ord(c)-96 for c in raw]

def increment(p):
    p[len(p)-1]+=1
    i = len(p)-1
    while i > 0 and p[i] > 26:
        p[i] = 1
        p[i-1]+=1
        i-=1
    return(p)
    
def check_One(p):
    i = 0
    while i < len(p)-2:
        if p[i] == p[i+1]-1 == p[i+2]-2:
            return True
        else:
            i+=1
    return False

def check_Two(p):
    if ord('i')-96 in p or ord('o')-96 in p or ord('l')-96 in p:
        return False
    return True

def check_Three(p):
    i, l = 0, []
    while i < len(p)-1:
        if p[i] == p[i+1]:
            l.append(p[i])
            i+=1
        else:
            i+=1
    return(len(set(l)))

found = 0
while found < 2:
    P = increment(P)
    if check_One(P) == True and check_Two(P) == True and check_Three(P) >=2:
        A = [chr(c+96) for c in P]
        print("".join(A))
        found +=1 
    

            