from functools import cache

@cache
def binom(n:int, k:int)->int:
    if k==0 or k==n : return 1
    return binom(n-1, k-1) + binom(n-1, k)

def binom_memo(n:int, k:int)->int:
    dictionnaire: dict[tuple[int, int], int] = {}
    dictionnaire.update({(i,0):1 for i in range(n+1)})
    dictionnaire.update({(i,i):1 for i in range(n+1)})
    def fonct_bin(dic:dict[tuple[int,int], int], n, k)->int:
        if (n,k) in dic.keys():
            return int(dic[(n,k)])
        dic[(n,k)] = int(fonct_bin(dic, n-1, k-1)) + int(fonct_bin(dic, n-1, k))
        return dic[(n,k)]
    return fonct_bin(dictionnaire, n,k)


if __name__ == "__main__":
    val = binom(100,50)
    val2 = binom_memo(100,50)
    print(val)
    print(val2)