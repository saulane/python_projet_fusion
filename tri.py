#!/bin/env python3
import sys, re
from module import gen_list

"""
    Soit L le type liste dont les éléments sont soit tous de type int, soit tous de type L.

    Ce programme lit des liste de type L sur l'entrée standard, au format
    [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
    et sort cette liste dans laquelle les sous-listes d'entiers sont triées.  
"""

def tri(l):
    """
    Cette fonction récursive tri la liste passée en argument.
    """
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)

if __name__=="__main__":
    # programme principal
        L = gen_list()
        for l in L:
            tri(l)
            print(f"{l=}")
