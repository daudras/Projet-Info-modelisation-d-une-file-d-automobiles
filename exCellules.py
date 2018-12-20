#exemple de matrice de cellules
#nb de colonnes entre 1 et 10
#nb de ligne : li
#les probabilités de comportement doivent pouvoir être modifiées
#dans un menu,
#les états sont ici pris au hasard mais ils seront déduit des
#situations et du comportement.

#liste des probabilités dans l'ordre des éléments du 3-uplet
#de comportement.
probas=[[0.2,0.7,0.1],[0.3,0.7],[0.2,0.8]]

from random import randint, random
def ecc(liste):
    """renvoie la liste des effectifs cumulés croissant
    de la liste fournit en entrée."""
    l=[liste[0]]
    for i in range(len(liste)-1):
        l.append(l[i]+liste[i+1])
    return l

def choix(liste):
    """renvoie un entier au hasard entre 0 et la longueur de liste-1
    avec pour coefficients les éléments de la liste."""
    n=random()
    l=ecc(liste)
    for i in range(len(liste)):
        if (n<l[i]):break
    return i

def exCellules(li,coefs):
    """renvoie une matrices de listes à 6 éléments représentant une
    file de cellules et son évolution. Le nombre de colonne est
    un entier entre 1 et 10 et le nombre de ligne est la variable d'entrée li.
    coefs est la liste des probabilités pour le comportement."""
    cellules=[]
    ligne=[]
    for i in range(li):
        nbCol=randint(1,10)
        for j in range(nbCol):
            ligne.append([choix(coefs[0])+1,choix(coefs[1]),choix(coefs[2]),
            randint(-3,3),randint(0,3),randint(0,7)])
        cellules.append(ligne)
    return cellules

print(exCellules(3,probas))