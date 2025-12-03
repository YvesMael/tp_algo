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
                