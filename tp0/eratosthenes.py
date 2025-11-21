from itertools import compress
# def sieve_of_eratosthenes(N:int)->list[int]:
#     liste = [i for i in range(2,N+1)]
#     for elem in liste:
#         for elem_courant in liste:
#             if elem_courant is not elem and elem_courant%elem==0:
#                 liste.remove(elem_courant)        
#     return liste

def sieve_of_eratosthenes(N:int)->list[int]:
    liste = [i for i in range(2,N+1)]
    liste_bool = [True]*(N-1)
    for elem in enumerate(liste):
        for position, elem_courant in enumerate(liste):
            if elem_courant is not elem and elem_courant%elem==0:
                liste_bool[position] = False  
    return list(compress(liste, liste_bool))
