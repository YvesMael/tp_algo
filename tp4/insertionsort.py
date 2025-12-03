def insertionsort(seq:list[int])->list[int]:
    for i in range(1,len(seq)):
        k = i-1
        temp = seq[i]
        while temp < seq[k] and k>=0:
            seq[k+1] = seq[k]
            k-=1
        seq[k+1] = temp
    return seq