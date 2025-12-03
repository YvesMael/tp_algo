def mergesort(seq:list[int])->list[int]:
    liste:list[int]
    def fusiontableau(d1:int, f1:int, liste1:list[int], d2:int, f2:int, liste2:list[int])->list[int]:
        i, j = d1, d2
        k=0
        while i<=f1 or j<=f2:
            if i<=f1 and j<=f2:
                if liste1[i] <= liste2[j]:
                    liste[k] = liste1[i]
                    i+=1
                else:
                    liste[k] = liste2[j]
                    j+=1
            elif i<=f1:
                liste[k] = liste1[i]
                i+=1
            elif j<=f2:
                liste[k] = liste2[j]
                j+=1
            k+=1
        return liste
    
    def rec(d:int,f:int,seq:list[int])->list[int]:
        if f-d == 1:
            if seq[f]<seq[d]:
                seq[f], seq[d] = seq[d], seq[f]
                return seq
        if f-d>1:
            rec(d,(f+d)//2,seq)
            rec((f+d)//2+1,f,seq)
            return fusiontableau(d,(f+d)//2,seq,(f+d)//2+1,f,seq)
        return seq
    
    return rec(0,len(seq)-1,seq)
    