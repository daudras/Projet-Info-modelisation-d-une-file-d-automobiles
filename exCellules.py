#exemple de matrice de cellules
#nb de colonnes entre 1 et 10
#nb de ligne : li
#les probabilités sont ici uniformes,
#il faudra les pondérer par la suite.

from random import randint
def exCellules(li):
    cellules=[]
    ligne=[]
    for i in range(li):
        nbCol=randint(1,10)
        for j in range(nbCol):
            ligne.append([randint(1,3),randint(0,1),randint(0,1),
            randint(-3,3),randint(0,3),randint(0,7)])
        cellules.append(ligne)
    return cellules