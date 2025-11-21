def collatz(u0, n):
    assert u0 > 0 and n >0
    u = u0
    for i in range(n):
        if u % 2 == 0:
            u = u // 2
        else :
            u = 3 * u + 1
    return u

def collatz_series(u0,  n):
    liste = []
    for i in range(0, n):
        liste.append(collatz(u0, i))
    return liste

def collatz_lifetime(u0):
    n = 0
    val = 0
    while val != 1:
        n += 1
        val = collatz(u0, n)
    return n

def collatz_altitude(u0):
    liste=[]
    n = 1
    while 1 not in liste:
        liste.append(collatz(u0, n))
        n+=1
    liste.sort()
    return liste[len(liste)-1]

if __name__ == "__main__":
    print("Suite de collatz")
    seed = 135

    for i in range(1,42):
        print(f"   u_{i} = {collatz(seed, i)}")
    pass