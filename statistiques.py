from statistics import mean,pvariance


def listVA(ligne):
    """i est le numéro de ligne de la matrice cellules.
    en sortie v est une liste des vitesses contenus dans cette ligne
    et a une liste des carrés des accélérations. """
    v,a=[],[]
    for i in range(len(ligne)):
        v.append(ligne[i][4])
        a.append(ligne[i][3]**2)
    return v,a

def apListeVA(listesVA,ligne):
    """met à jours les listes de vitesses et d'accélérations avec la ligne
    i de la matrice cellules"""
    if ligne==[]:
        for i in range(2): listesVA[i].append(0)
    else :
        listesVA[0].append(round(mean(listVA(ligne)[0]),3))
        #listesVA[1].append(round(pvariance(listVA(ligne)[0]),3))
        listesVA[1].append(round(sum(listVA(ligne)[1]),3))
        #listesVA[3].append(round(pvariance(listVA(ligne)[1]),3))

def statVA(i,listesVA,ligne):
    """renvoie les statistiques pour le temps i avec listesVA la liste des listes
    de v, vVar et pol et polVar qui doivent être non vide."""
    polMoy=mean(listesVA[1])
    return (listesVA[0][i],round(pvariance(listVA(ligne)[0]),3),
        round(mean(listesVA[0]),3),round(pvariance(listesVA[0]),3),
        listesVA[1][i],round(pvariance(listVA(ligne)[1]),3),
        round(polMoy,3),round(pvariance(listesVA[1]),3),round(polMoy*(i+1),0))

def test():
    cellules=[[[2, 0, 1, 1, 0, 0], [2, 1, 0, 1, 1, 6], [2, 0, 1, -2, 0, 4], [2, 0, 1, -1, 0, 7], [2, 0, 1, -2, 3, 3], [1, 1, 1, -1, 2, 1], [2, 0, 0, 1, 2, 4], [2, 1, 1, -1, 3, 2], [3, 0, 0, -2, 3, 5], [3, 1, 1, -2, 0, 0], [2, 1, 0, 2, 1, 7], [3, 1, 0, 2, 1, 5], [2, 0, 1, -2, 0, 4], [2, 0, 1, -2, 3, 1], [2, 1, 1, -2, 2, 0], [2, 1, 1, 2, 1, 5], [1, 0, 1, 3, 1, 7], [3, 1, 1, -2, 1, 4]], [[2, 0, 1, 1, 0, 0], [2, 1, 0, 1, 1, 6], [2, 0, 1, -2, 0, 4], [2, 0, 1, -1, 0, 7], [2, 0, 1, -2, 3, 3], [1, 1, 1, -1, 2, 1], [2, 0, 0, 1, 2, 4], [2, 1, 1, -1, 3, 2], [3, 0, 0, -2, 3, 5], [3, 1, 1, -2, 0, 0], [2, 1, 0, 2, 1, 7], [3, 1, 0, 2, 1, 5], [2, 0, 1, -2, 0, 4], [2, 0, 1, -2, 3, 1], [2, 1, 1, -2, 2, 0], [2, 1, 1, 2, 1, 5], [1, 0, 1, 3, 1, 7], [3, 1, 1, -2, 1, 4]], [[2, 0, 1, 1, 0, 0], [2, 1, 0, 1, 1, 6], [2, 0, 1, -2, 0, 4], [2, 0, 1, -1, 0, 7], [2, 0, 1, -2, 3, 3], [1, 1, 1, -1, 2, 1], [2, 0, 0, 1, 2, 4], [2, 1, 1, -1, 3, 2], [3, 0, 0, -2, 3, 5], [3, 1, 1, -2, 0, 0], [2, 1, 0, 2, 1, 7], [3, 1, 0, 2, 1, 5], [2, 0, 1, -2, 0, 4], [2, 0, 1, -2, 3, 1], [2, 1, 1, -2, 2, 0], [2, 1, 1, 2, 1, 5], [1, 0, 1, 3, 1, 7], [3, 1, 1, -2, 1, 4]]]
    #listesVA est ["v":[],"vVar":[],"pol":[],"polVar":[]]
    listesVA=[[],[]]
    apListeVA(listesVA,cellules[0])
    apListeVA(listesVA,cellules[1])
    print(listesVA)
    print(statVA(1,listesVA,cellules[1]))