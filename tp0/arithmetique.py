def valeur_absolue(n:float)->float:
    return n if n>=0 else -1*n

def parite(n:int)->bool:
    return not n%2==0

def prod_mod(n,p,m):
    return (n*p)%m

def diviseur(n,k):
    return n%k==0