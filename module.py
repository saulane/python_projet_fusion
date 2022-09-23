import sys, re

def build(l0):
    """
    Cette fonction construit la liste correspondant à sa représentation chaine de caractère fourni en argument.
    """
    def _build():
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1                 
                if i!=1:             # pour la première sous-liste, on ne fait rien
                    l.append(_build())    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))   
                i+=1
    i = 0
    res = _build()
    return res


def gen_list():
    nb_arg = len(sys.argv)
    L = []
    if (nb_arg == 1):
        while True:
            line = input("? ").rstrip("\n").strip()
            if line=="":
                break
            lline = re.split(r' +',line.rstrip("\n"))
            i=0
            l = build(lline)                      # récupération de la liste
            L.append(l)
    elif nb_arg == 2:
        #f = open(sys.argv[1], "r")

        with open(sys.argv[1], "r") as f:
            for line in f:
                lline = re.split(r' +',line.rstrip("\n"))
                L.append(build(lline))
    else:
        l_str = sys.argv[1:]
        L.append(build(l_str))
    return L