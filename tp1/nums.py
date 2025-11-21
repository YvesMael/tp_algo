def count_digits_drole(n:int, base:int=10)->int:
    chaine = str(n)
    return len(chaine)

def count_digits(n:int, base:int=10)->int:
    if n//base == 0:
        return 1
    return 1 + count_digits(n//base, base)

def convert(n:int, base:int)->str:
    chaine = ''
    def temp(chaine, n, base):
        if n//base == 0:
            return chaine+str(n)
        chaine+= str(n%base)
        return temp(chaine, n//base, base)
    return temp(chaine, n, base)[::-1]