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
    """met à jours les listes de vitesses et d'accélérations au carrées avec une ligne
     de la matrice cellules"""
    if ligne==[]:
        for i in range(2): listesVA[i].append(0)
    else :
        listesVA[0].append(round(mean(listVA(ligne)[0]),3))
        listesVA[1].append(round(sum(listVA(ligne)[1]),3))

def statVA(i,listesVA,ligne):
    """i : indice correspondant au temps
    listesVA : liste des vitesses et des accélérations au carrées
    ligne : liste de cellules[i]
    renvoie les statistiques v_i, v_iVar, v, vVar et pol_i, pol_iVar, pol, polVar
    et polution cumulée."""
    apListeVA(listesVA,ligne)
    polMoy=mean(listesVA[1][:i+1])
    if ligne==[]:
        v_iVar=0
        pol_iVar=0
    else :
        v_iVar=round(pvariance(listVA(ligne)[0]),3)
        pol_iVar=round(pvariance(listVA(ligne)[1]),3)
    return (listesVA[0][i],v_iVar,
        round(mean(listesVA[0][:i+1]),3),round(pvariance(listesVA[0][:i+1]),3),
        listesVA[1][i],pol_iVar,
        round(polMoy,3),round(pvariance(listesVA[1][:i+1]),3),round(polMoy*(i+1),0))

def test():
    cellules=[[[2, 0, 1, 1, 0, 0], [2, 1, 0, 1, 1, 6], [2, 0, 1, -2, 0, 4], [2, 0, 1, -1, 0, 7], [2, 0, 1, -2, 3, 3], [1, 1, 1, -1, 2, 1], [2, 0, 0, 1, 2, 4], [2, 1, 1, -1, 3, 2], [3, 0, 0, -2, 3, 5], [3, 1, 1, -2, 0, 0], [2, 1, 0, 2, 1, 7], [3, 1, 0, 2, 1, 5], [2, 0, 1, -2, 0, 4], [2, 0, 1, -2, 3, 1], [2, 1, 1, -2, 2, 0], [2, 1, 1, 2, 1, 5], [1, 0, 1, 3, 1, 7], [3, 1, 1, -2, 1, 4]], [[2, 0, 1, 1, 0, 0], [2, 1, 0, 1, 1, 6], [2, 0, 1, -2, 0, 4], [2, 0, 1, -1, 0, 7], [2, 0, 1, -2, 3, 3], [1, 1, 1, -1, 2, 1], [2, 0, 0, 1, 2, 4], [2, 1, 1, -1, 3, 2], [3, 0, 0, -2, 3, 5], [3, 1, 1, -2, 0, 0], [2, 1, 0, 2, 1, 7], [3, 1, 0, 2, 1, 5], [2, 0, 1, -2, 0, 4], [2, 0, 1, -2, 3, 1], [2, 1, 1, -2, 2, 0], [2, 1, 1, 2, 1, 5], [1, 0, 1, 3, 1, 7], [3, 1, 1, -2, 1, 4]], [[2, 0, 1, 1, 0, 0], [2, 1, 0, 1, 1, 6], [2, 0, 1, -2, 0, 4], [2, 0, 1, -1, 0, 7], [2, 0, 1, -2, 3, 3], [1, 1, 1, -1, 2, 1], [2, 0, 0, 1, 2, 4], [2, 1, 1, -1, 3, 2], [3, 0, 0, -2, 3, 5], [3, 1, 1, -2, 0, 0], [2, 1, 0, 2, 1, 7], [3, 1, 0, 2, 1, 5], [2, 0, 1, -2, 0, 4], [2, 0, 1, -2, 3, 1], [2, 1, 1, -2, 2, 0], [2, 1, 1, 2, 1, 5], [1, 0, 1, 3, 1, 7], [3, 1, 1, -2, 1, 4]]]
    #listesVA est ["v":[],"pol":[]]
    listesVA=[[],[]]
    apListeVA(listesVA,cellules[0])
    apListeVA(listesVA,cellules[1])
    print(listesVA)
    print(statVA(1,listesVA,cellules[1]))