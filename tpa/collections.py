import math

Point = tuple[float, float]

# renvoyer la distance entre deux points et le milieu de ces deux points
def distance_et_barycentre(A: Point, B:Point) -> tuple[float, Point] :
    # calcul de la distance et de l'isobarycentre
    distance = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    milieu:tuple[float, float] = ((A[0]+B[0])/2, (A[1]+B[1])/2)
    return (distance, milieu)

# renvoi un dictionnaire dont les valeurs sont les carres des cles
def dict_carres():
    dico: dict[int, int] = {}
    for n in range(100):
        dico[n] = n**2

    # ou simplement 
    dico = {k:k**2 for k in range(100)}
# construit un dictionnaire a partir d'une liste de cles et d'une liste de valeurs
def list_to_dict(cles, valeurs):
    dictionnaire: dict = {}
    taille = len(cles) if len(cles) < len(valeurs) else len(valeurs)
    for i in range(taille):
        dictionnaire[cles[i]] = valeurs[i]

    # ou encore
    dictionnaire = {k:v for k,v in zip(cles, valeurs)}

# calcul la moyenne des valeurs d'un dictionnaire
def moyenne(dico: dict[str, int])-> float:
    return (sum(dico.values())/len(dico))

# trier et afficher les cles d'un dictionnaire par ordre dec des valeurs
def trier_dict(dico):
    liste:list = list(dico.items())
    #liste.sort(key=)
    pass