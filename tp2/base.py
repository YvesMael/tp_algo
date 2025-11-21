from tp2.util import StaticArray, alloc, nops, reset_nops

def mode(tab: StaticArray)-> int:
    valMax = 0
    nbreOccMax = 0
    for i in range(len(tab)):
        nbreOcc = 0
        for j in range(len(tab)):
            if tab[i] == tab[j]:
                nbreOcc+=1
        if nbreOcc > nbreOccMax:
            valMax = tab[i]
            nbreOccMax = nbreOcc
    return valMax

def cumulative_sum(tab: StaticArray)-> StaticArray:
    cumul: StaticArray = alloc(len(tab))
    cumul[0] = tab[0]
    for i in range(1,len(tab)):
        cumul[i] = cumul[i-1] + tab[i]
    return cumul

def duplicate_elimination(tab: StaticArray)-> StaticArray:
    nbreRepet =0
    for i in range(len(tab)):
        for j in range(1,len(tab)):
            if (j+i)<len(tab) and tab[i] == tab[j+i]:
                nbreRepet+=1
    tabSansDoublons: StaticArray = alloc(len(tab)-nbreRepet)
    
    # nouveau: StaticArray = alloc(len(tab))
    k = 0
    for i in range(len(tab)):
        j=0
        while j<len(tab) and tab[i]!=tabSansDoublons[j]:
            j+=1
        if (j==len(tabSansDoublons)):
            tabSansDoublons[k] = tab[i]
            k+=1
    return tabSansDoublons

def binary_search(tab: StaticArray, x: int)-> int:
    d, f = 0, len(tab)-1
    milieu = (d+f)//2
    j: int =milieu+1
    k: int =milieu-1
    if tab[milieu] == x: return milieu
    while tab[j]< x: j+=1
    while tab[k]> x: k-=1
    if tab[j] == x : return j
    elif tab[k] == x : return k
    else: return -1


if __name__ == "__main__":
    tableau: StaticArray = alloc(8)
    tableau[0] = 1
    tableau[1] = 8
    tableau[2] = 7
    tableau[3] = 5
    tableau[4] = 9
    tableau[5] = 0
    tableau[6] = 10
    tableau[7] = 2
    maxi = mode(tableau)
    print("le mode est "+str(maxi)+" le cout est "+str(nops(tableau)))
    reset_nops(tableau)

    print("recherche d'un element: "+str(binary_search(tableau,8)))