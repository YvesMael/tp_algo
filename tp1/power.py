def power(a:int, n:int)->int:
    if n==0: return 1
    if n==1: return a
    if n%2 == 0: return power(a, n//2)*power(a,n//2)
    return power(a,n//2)*power(a,(n//2+1))

def superpower(a:int, n:int)->int:
    if n==0: return 1
    if n==1: return a
    if n%2 == 0: return superpower(a, n//2)*superpower(a,n//2)
    return superpower(a,n//2)*superpower(a,(n//2+1))

if __name__ == '__main__':
    print(power(2,26))