import sys

def input_number_from_kb(prompt: str='Saisir un nombre entier :')-> int:
    try:
        return int(input(prompt))
    except ValueError:
        print("veuillez saisir un nombre")

def input_nums_from_cli()-> list[int]:
    try:
        liste:list[int] = []
        somme = 0
        data:str
        if sys.argv[1] == '--sum':
            args = sys.argv[2:]
            for arg in args:
                somme +=int(arg)
            return [somme]
        elif sys.argv[1] == '--help':
            return """ usage: python -m tp0.inout [--help] [--sum] [NOMBRE...]\n Collecte les nombres passés en ligne de commande\n arguments:\n  NOMBRE\t serie de nombres à collecter\n\noptions:\n--help\t affiche ce message d'aide et termine\n--sum\t réalise la somme des nombres
                    """
        elif sys.argv[1].startswith('--file='):
            nom_fichier = str(sys.argv[1].split('=')[1])
            with open(nom_fichier,'r') as input_file:
                l=[int(e) for e in input_file]
                return l
        else:
            args = sys.argv[1:]
            for arg in args:
                liste.append(int(arg))
            return liste        
    except ValueError:
        print("les arguments doivent etre des entiers!")


if __name__ == '__main__':
    #print("la valeur saisie est : " + str(input_number_from_kb()))
    print(str(input_nums_from_cli()))