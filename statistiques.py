from statistics import mean,pvariance


def statsLigne(ligne):
    """ligne : une ligne de la matrice cellules.
    en sortie : vitesse moyenne v_i et variance associée v_iVar,
    cumule de pollution pol_i et variance associée pol_iVar."""
    if ligne==[] :
        return 0,0,0,0
    v,p=[],[]
    for i in range(len(ligne)):
        if ligne[i][5]!=-1:
            v.append(ligne[i][4])
            p.append(ligne[i][3]**2)
    return round(mean(v),3),round(pvariance(v),3),round(sum(p),3),round(pvariance(p),3)

def afStatistiques(stats_i,listeV,listeP,statMenu):
        """stats_i: [v_i,v_iVar,pol_i,pol_iVar]
        listeV,listeP: liste des vitesses moyennes et pollutions cumulées
        statMenu: liste des objets IntVar qui affichent les valeurs des statistiques.
        """
        polMoy=mean(listeP)
        statMenu[0].set(stats_i[0])
        statMenu[1].set(stats_i[1])
        statMenu[2].set(round(mean(listeV),3))
        statMenu[3].set(round(pvariance(listeV),3))
        statMenu[4].set(stats_i[2])
        statMenu[5].set(stats_i[3])
        statMenu[6].set(round(polMoy,3))
        statMenu[7].set(round(pvariance(listeP),3))
        statMenu[8].set(round(polMoy*(len(listeP)),0))



def test():
    cellules=[[[2, 0, 1, 1, 0, 0], [2, 1, 0, 1, 1, 6], [2, 0, 1, -2, 0, 4], [2, 0, 1, -1, 0, 7], [2, 0, 1, -2, 3, 3], [1, 1, 1, -1, 2, 1], [2, 0, 0, 1, 2, 4],
     [2, 1, 1, -1, 3, 2], [3, 0, 0, -2, 3, 5], [3, 1, 1, -2, 0, 0], [2, 1, 0, 2, 1, 7], [3, 1, 0, 2, 1, 5], [2, 0, 1, -2, 0, 4], [2, 0, 1, -2, 3, 1], [2, 1, 1, -2, 2, 0],
      [2, 1, 1, 2, 1, 5], [1, 0, 1, 3, 1, 7], [3, 1, 1, -2, 1, 4]], [[2, 0, 1, 1, 0, 0], [2, 1, 0, 1, 1, 6], [2, 0, 1, -2, 0, 4], [2, 0, 1, -1, 0, 7], [2, 0, 1, -2, 3, 3],
       [1, 1, 1, -1, 2, 1], [2, 0, 0, 1, 2, 4], [2, 1, 1, -1, 3, 2], [3, 0, 0, -2, 3, 5], [3, 1, 1, -2, 0, 0], [2, 1, 0, 2, 1, 7], [3, 1, 0, 2, 1, 5], [2, 0, 1, -2, 0, 4],
        [2, 0, 1, -2, 3, 1], [2, 1, 1, -2, 2, 0], [2, 1, 1, 2, 1, 5], [1, 0, 1, 3, 1, 7], [3, 1, 1, -2, 1, 4]], [[2, 0, 1, 1, 0, 0], [2, 1, 0, 1, 1, 6], [2, 0, 1, -2, 0, 4],
         [2, 0, 1, -1, 0, 7], [2, 0, 1, -2, 3, 3], [1, 1, 1, -1, 2, 1], [2, 0, 0, 1, 2, 4], [2, 1, 1, -1, 3, 2], [3, 0, 0, -2, 3, 5], [3, 1, 1, -2, 0, 0], [2, 1, 0, 2, 1, 7],
          [3, 1, 0, 2, 1, 5], [2, 0, 1, -2, 0, 4], [2, 0, 1, -2, 3, 1], [2, 1, 1, -2, 2, 0], [2, 1, 1, 2, 1, 5], [1, 0, 1, 3, 1, 7], [3, 1, 1, -2, 1, 4]],
          [[2, 1, 1, 0, 3, 5], [2, 1, 1, 0, 3, 4], [1, 1, 1, 0, 3, 3], [3, 1, 0, 0, 3, 1], [1, 0, 0, 0, 3, 3], [2, 0, 0, 0, 3, 1], [3, 0, 0, 0, 3, 1],
           [1, 0, 0, 0, 3, 6], [2, 1, 1, 0, 3, 2], [2, 1, 0, 0, 3, 3], [1, 0, 0, 0, 3, 1], [1, 0, 0, 0, 3, 1], [2, 1, 1, 0, 3, 3], [2, 1, 0, 0, 3, 1]]]
    def statVA(i,listeV, listeP,ligne):
        """i : indice correspondant au temps
        listeV, listeP : liste des vitesses moyennes
         et des cumules de pollution
        ligne : liste de cellules[i]
        renvoie les statistiques v_i, v_iVar, v, vVar et pol_i, pol_iVar, pol, polVar
        et pollution cumulée."""
        polMoy=mean(listeP[:i+1])
        v_iVar=statsLigne(ligne)[1]
        pol_iVar=statsLigne(ligne)[3]
        return (listeV[i],v_iVar,
            round(mean(listeV[:i+1]),3),round(pvariance(listeV[:i+1]),3),
            listeP[i],pol_iVar,
            round(polMoy,3),round(pvariance(listeP[:i+1]),3),round(polMoy*(i+1),0))
    def nouvLigneStat(ligne):
        v_i, v_iVar, pol_i, pol_iVar=statsLigne(ligne)
        return v_i,pol_i
    listeV,listeP=[],[]
    for i in range(3):
        v,p=nouvLigneStat(cellules[i])
        listeV.append(v)
        listeP.append(p)
    print(listeV,listeP)
    print(statVA(2,listeV,listeP,cellules[2]))