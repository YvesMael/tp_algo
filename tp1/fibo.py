from tp1.decorators import trace

#ecriture literale de la fonction recurcive de fibo(n)
@trace
def fibo(n:int)->int:
    if n==0: return 0
    if n==1: return 1
    return fibo(n-1) + fibo(n-2)

def fibo_norec(n:int)->int:
    valeur:int = 1
    fib_prec:int=1
    fib_precprec:int=0
    if n==0: return 0
    if n==1: return 1
    for i in range(2,n+1):
        valeur = fib_prec + fib_precprec
        fib_precprec = fib_prec
        fib_prec = valeur
    return valeur

def fibo_term(n:int)->int:
    def term(val,a,n):
        if n==0:
            return val
        return term(a,val+a,n-1)
    return term(0,1,n)


if __name__=="__main__":
    val = fibo_norec(20)
    print("la valeur est: "+str(val))