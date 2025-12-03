def quicksort(seq:list[int])->list[int]:
    def rec(d:int, f:int, seq:list[int])->list[int]:
        if f-d >0:
            k = d+1
            for i in range(d+1,f):
                if seq[i]<=seq[d]:
                    seq[k],seq[i] = seq[i], seq[k]
                    k+=1
            seq[k-1], seq[d] = seq[d], seq[k-1]
            rec(d,k-1,seq)
            rec(k,f,seq)
        return seq
    return rec(0,len(seq),seq)