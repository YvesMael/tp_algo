import random

def stupidsort(seq: list[int])->list[int]:
    while True:
        trier = True
        for i in range(len(seq)-1,0,-1):
            j = random.randint(0,i)
            seq[i], seq[j] = seq[j], seq[i]
        for k in range(len(seq)):
            for l in range(k+1,len(seq)):
                if seq[k] > seq[l]:
                    trier = False
        if trier:
            break
    return seq

def insertionsort(seq:list[int])->list[int]:
    for i in range(1,len(seq)):
        k = i-1
        temp = seq[i]
        while temp < seq[k] and k>=0:
            seq[i] = seq[k]
            k-=1
        seq[k+1] = temp
    return seq
                