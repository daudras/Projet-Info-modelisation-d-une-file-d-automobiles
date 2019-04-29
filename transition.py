#Algorithme de génération et de transition.
#
#liste des probabilités pour la génération de nouvelles cellules :
#probas=[[ p_c1, p_c2,1-p_c1-p_c2],[p_an,1-p_an],[p_ds,1-p_ds],
#[p_e, p_eS,p_r,p_rS]]

from random import randint, random
from copy import deepcopy
def ecc(liste):
    """renvoie la liste des effectifs cumulés croissant
    de la liste fournit en entrée."""
    l=[liste[0]]
    for i in range(len(liste)-1):
        l.append(l[i]+liste[i+1])
    return l
def testEcc(): print(ecc([1,2,3]))
def choix(liste):
    """renvoie un entier i au hasard entre 0 et la longueur de liste-1
    avec la probabilité liste[i]"""
    n=random()
    l=ecc(liste)
    for i in range(len(liste)):
        if (n<l[i]):break
    return i
def testChoix1():
    sum0,sum1,n=0,0,50
    for i in range(n) :
        c=choix([0.3,0.5,0.2])
        if c==0:sum0+=1
        elif c==1: sum1+=1
        print(c,end= " ; ")
    print("\n frequence 0 : ",sum0/n," ; frequence 1 : ",sum1/n," ; frequence 2 : ",(n-sum0-sum1)/n)
def testChoix2():
    sum0,n=0,50
    for i in range(n) :
        c=choix([0.3,0.7])
        if c==0:sum0+=1
        print(c,end= " ; ")
    print("\n frequence 0 : ",sum0/n," ; frequence 1 : ",(n-sum0)/n)

def initCellules(n,probas):
    """renvoie une matrices de listes à 6 éléments comportant 1 ligne de n colonnes,
    représentant une file de n cellules au temps t=0
    probas est la liste des probabilités pour définir le comportement :
    probas=[[ p_c1, p_c2,1-p_c1-p_c2],[p_an,1-p_an],[p_ds,1-p_ds],[p_e, p_eS,p_r,p_rS]]"""
    ligne=[]
    nbCol=n
    for j in range(nbCol):
        ligne.append([choix(probas[0])+1,choix(probas[1]),choix(probas[2]),
        randint(-1,1),randint(2,3),randint(2,4)])
    return ligne
def testInitCellules():
    print(initCellules(8,probas))


def reglesTrans(e,e1,e2):
    """prends en entrée les états de trois cellules consécutive e, e1 et e2 dans
    l'ordre de la file de cellules de gauche à droite avec e=(c,an,ds,a,v,d).
    an dans {0,1}, ds dans {0,1}, -4<a<4, 0<d<8.
    Renvoie en sortie le coefficient 1, 0 ou -1 déterminé par les règles de transitions.
    """
    c,an,ds,a,v,d=tuple(e)
    a1,a2=e1[3],e2[3]
    if (d>2): return 1
    if (d==2) & (a1>0) & ((not an) | (a2>=0)) : return 1
    if (d==2) & (a1>0) & an & (a2<0) : return 0
    if (d==2) & (a1==0) & ((not an) | (a2>=0)) & ds : return 0
    if (d==2) & (a1==0) & ((not an) | (a2>=0)) & (not ds) : return 1
    if (d==2) & (a1==0) & an & (a2<0) & ds : return -1
    if (d==2) & (a1==0) & an & (a2<0) & (not ds) : return 0
    if (d==2) & (a1==-3) : return -1
    if (d==2) & ((a1==-2) | (a1==-1)) & ds : return -1
    if (d==2) & ((a1==-2) | (a1==-1)) & (not ds) : return 0
    if (d==1) & (a1==0) & ((not an) | (a2>=0)) & ds : return -1
    if (d==1) & (a1==0) & ((not an) | (a2>=0)) & (not ds) : return 0
    if (d==1) & (a1==0) & an & (a2<0) :return -1
    if (d==1) & (a1>0) & ds : return 0
    if (d==1) & (a1>0) & (not ds) : return 1
    if (d==1) & (a1<0) : return -1
def testReglesTrans():
    """vérifions qu'aucun cas n'a été oublié et que toutes les parenthèses
    soient bien présentes."""
    for d in range(3):
        for a1 in range(4):
            for an in range (2):
                for a2 in range (2):
                    for ds in range (2):
                        e=[0,[0,1][an],[0,1][ds],0,0,[3,2,1][d]]
                        e1=[0,0,0,[1,0,-1,-3][a1],0,0]
                        e2=[0,0,0,[0,-1][a2],0,0]
                        print(reglesTrans(e,e1,e2)," avec d=",e[5]," a1=",e1[3]
                            ," an=",e[1]," a2=",e2[3]," ds=",e[2])

def conditionAccident(e,e1):
    """prends en entrée les états de deux cellules consécutive e et e1 dans
    l'ordre de la file de cellules de gauche à droite.
    Détermine si la situation entraine un accident et renvoie un booléen"""
    c,an,ds,a,v,d=tuple(e)
    c1,a1,an1=e1[0],e1[3],e1[1]
    if (d==1) & (a1==-3) & (v>=2) : return True
    return False
def testConditionAccident():
    print("false ",conditionAccident([1,0,0,1,1,1],[1,0,0,1,1,1])," ; true :",
        conditionAccident([1,0,0,1,2,1],[1,0,0,-3,1,1]),"; true :",
        conditionAccident([1,0,0,1,2,1],[0,0,0,0,1,1]))
def bridageAcVi(v,coef):
    """v est la vitesse dans l'état d'un cellule et coef est le coefficient
    renvoyé par la fonction reglesTrans(), ce sont deux entiers.
    Une voiture au max ne peux pas accélérer et ne peux pas freiner à l'arrêt.
    Renvoie le coef ou 0."""
    if ((v==3) & (coef==1)) | ((v==0) & (coef==-1)): return 0
    return coef
def testBridageAcVi():
    print(bridageAcVi(3,1),bridageAcVi(0,-1),bridageAcVi(2,7))

def transition1Cel(e,e1,e2,accident):
    """prends en entrée les états de trois cellules consécutive e, e1 et e2 dans
    l'ordre de la file de cellules de gauche à droite et un bouléen a qui autorise
    ou non la prise en compte d'un accident.
    Renvoie l'état t(e) image de e par les règles de transitions pour une cellule
    normale ou e pour une cellule spéciale (c=0) ou e avec d=0 si les conditions
    d'un accident sont réunies. Si e1 est spéciale il faut réduire la vitesse."""
    c,an,ds,a,v,d=tuple(e)
    if c==0: return e
    c1,v1=e1[0],e1[4]
    if conditionAccident(e,e1) and accident : return [c,an,ds,a,v,0]
    a=bridageAcVi(v,reglesTrans(e,e1,e2))*c
    if a<-3: a=-3
    if a>3: a=3
    if (c1==0) & (v>1) & (d==1): a=-3
    v=v+a
    if v<0: v=0
    if v>3: v=3
    d=d+v1-v
    if (d<1) & (ds==0): d=1
    if (d<2) & (ds==1): d=2
    if d>7: d=7
    return [c,an,ds,a,v,d]
def testTransition1Cel():
    probas=[[0.2,0.7,0.1],[0.3,0.7],[0.6,0.4],[0.5,0.2,0.5,0.5]]
    cellules=[]
    cellules.append(initCellules(8,probas))
    print(cellules[0][0],cellules[0][1],cellules[0][2])
    print(transition1Cel(cellules[0][0],cellules[0][1],cellules[0][2],True))
    print(transition1Cel([0,0,0,-2,0,0],cellules[0][1],cellules[0][2],True))
    print(transition1Cel([3,0,0,3,3,1],[1,0,0,-3,0,0],cellules[0][2],True))


def transitionFile(ligne,accident):
    """prends en argument la dernière ligne du tableau cellules
    Renvoie une nouvelle ligne issue de l'application des règles de transitions.
    La file est considérée comme circulaire, toute cellule a donc deux suivantes.
    """
    nouvLigne=[]
    long=len(ligne)
    for i in range(long):
        e,e1,e2=ligne[i],ligne[(i+1)%long],ligne[(i+2)%long]
        nouvLigne.append(transition1Cel(e,e1,e2,accident))
    return nouvLigne
def testTransitionFile():
    probas=[[0.2,0.7,0.1],[0.3,0.7],[0.6,0.4],[0.5,0.2,0.5,0.5]]
    cellules=[]
    cellules.append(initCellules(8,probas))
    print(transitionFile(cellules[0]),True)

def entree(ligne,num,cel):
    """prends en entrée la dernière ligne du tableau de cellules et le numéro num
    de la cellules après laquelle on place la nouvelle cellule cel, 0<=num<len(ligne).
    La distance d de l'état de la cellule ligne[num] doit être supérieure ou égale à 2.
    Renvoie une nouvelle ligne en insérant cel à l'indice num+1 et en diminuant la distance
    d de 1 si cel est normale.
    """
    nouvLigne=deepcopy(ligne)
    if (cel[0]>0): nouvLigne[num][5]-=1
    long=len(nouvLigne)
    nouvLigne.append([])
    for i in range(long-num-1):
        nouvLigne[long-i]=nouvLigne[long-i-1]
    nouvLigne[num+1]=cel
    return nouvLigne
def testEntree():
    probas=[[0.2,0.7,0.1],[0.3,0.7],[0.6,0.4],[0.5,0.2,0.5,0.5]]
    cellules=[]
    cellules.append(initCellules(8,probas))
    print(cellules[0],len(cellules[0]))
    print(entree(cellules[0],len(cellules[0])-1,[0,0,0,0,0,0]))
    print(entree(cellules[0],2,[0,0,0,0,0,0]))
    print(entree(cellules[0],0,[0,0,0,0,0,0]))
    print(cellules[0],len(cellules[0]))


def sortie(ligne,num):
    """prends en entrée la dernière ligne du tableau de cellules et le numéro num
    de la cellules à retirer.
    On appelle d la distance de l'état de la cellule ligne[num-1],
    Renvoie une nouvelle ligne en retirant ligne[num] et en augmentant d de 1.
    La liste est circulaire donc la cellules à gauche de la première est la dernière.
    """
    nouvLigne=deepcopy(ligne)
    if (nouvLigne[num-1][0]>0): nouvLigne[num-1][5]+=1
    long=len(nouvLigne)
    for i in range(long-num-1):
        nouvLigne[num+i]=nouvLigne[num+i+1]
    nouvLigne.pop()
    return nouvLigne
def testSortie():
    probas=[[0.2,0.7,0.1],[0.3,0.7],[0.6,0.4],[0.5,0.2,0.5,0.5]]
    cellules=[]
    cellules.append(initCellules(8,probas))
    print(cellules[0])
    print(sortie(cellules[0],len(cellules[0])-1))
    print(sortie(cellules[0],2))
    print(sortie(cellules[0],0))
    print(cellules[0])

def choixHasardListe(liste):
    """En paramètre une liste non vide d'éléments. Renvoie un élément au hasard."""
    return liste[randint(0,len(liste)-1)]
def testChoixHasardListe():
    for i in range(10): print(choixHasardListe([0,1,5,8]),end=" ; ")
    print(choixHasardListe([2]))

def filtreDsup2(liste):
    """renvoie la liste des indices des cellules de liste tel que d>=2"""
    l=[]
    for i in range(len(liste)):
        if liste[i][5]>=2: l.append(i)
    return l
def testFiltreDsup2():
    probas=[[0.2,0.7,0.1],[0.3,0.7],[0.6,0.4],[0.5,0.2,0.5,0.5]]
    cellules=[]
    cellules.append(initCellules(8,probas))
    print(cellules[0])
    print(filtreDsup2(cellules[0]))
def filtreNormales(liste):
    """renvoie la liste des indices des cellules de liste tel que c!=0"""
    l=[]
    for i in range(len(liste)):
        if liste[i][0]!=0: l.append(i)
    return l
def filtreSpeciales(liste):
    """renvoie la liste des indices des cellules de liste tel que c==0"""
    l=[]
    for i in range(len(liste)):
        if liste[i][0]==0: l.append(i)
    return l
def creationCelluleEntreeNormale(probas):
    """probas=[[ p_c1, p_c2,1-p_c1-p_c2],[p_an,1-p_an],[p_ds,1-p_ds],
    [p_e, p_eS,p_r,p_rS]]
    Renvoie une cellule pour une entrée dans la file."""
    return [choix(probas[0])+1,choix(probas[1]),choix(probas[2]),2,1,4]
def creationCelluleEntreeSpeciale():
    """Renvoie une cellule spéciale, feu ou rond point au hasard pour
    une entrée dans la file."""
    if randint(0,1): return [0,0,0,-1,0,-1]
    else: return [0,0,0,-1,1,-1]
def testCreationCelluleEntreeNormaleSpeciale():
    probas=[[0.2,0.7,0.1],[0.3,0.7],[0.6,0.4],[0.5,0.2,0.5,0.5]]
    for i in range(5):
        print(creationCelluleEntreeNormale(probas),end=";")
        print(creationCelluleEntreeSpeciale(),end=";")
def testFiltreNormalesSpeciales():
    probas=[[0.2,0.7,0.1],[0.3,0.7],[0.6,0.4],[0.5,0.2,0.5,0.5]]
    cellules=[]
    cellules.append(initCellules(8,probas))
    ligne=cellules[0]+[creationCelluleEntreeSpeciale()]
    print(ligne)
    print(filtreNormales(ligne))
    print(filtreSpeciales(ligne))

def mouvementFile(ligne,probas):
    """probas=[[ p_c1, p_c2,1-p_c1-p_c2],[p_an,1-p_an],[p_ds,1-p_ds]
    ,[p_e, p_eS,p_r,p_rS]]
    Renvoie une nouvelle ligne après les sorties et entrées de cellules selon
    les probabilités p_e, p_eS, p_r, p_rS."""
    p_e, p_eS,p_r,p_rS=probas[3][0],probas[3][1],probas[3][2],probas[3][3]
    nouvLigne=deepcopy(ligne)
    normales=filtreNormales(nouvLigne)
    if choix([1-p_r,p_r]) & (normales!=[]):
        nouvLigne=sortie(nouvLigne,choixHasardListe(normales))
    speciales=filtreSpeciales(nouvLigne)
    if choix([1-p_rS,p_rS]) & (speciales!=[]):
        nouvLigne=sortie(nouvLigne,choixHasardListe(speciales))
    dSup2=filtreDsup2(nouvLigne)
    if choix([1-p_e,p_e]) & (dSup2!=[]):
        nouvLigne=entree(nouvLigne,choixHasardListe(dSup2),creationCelluleEntreeNormale(probas))
    dSup2=filtreDsup2(nouvLigne)
    if choix([1-p_eS,p_eS]) & (dSup2!=[]):
        nouvLigne=entree(nouvLigne,choixHasardListe(dSup2),creationCelluleEntreeSpeciale())
    return nouvLigne
def testmouvementFile():
    probas=[[0.2,0.7,0.1],[0.3,0.7],[0.6,0.4],[0.5,0.2,0.5,0.5]]
    cellules=[]
    cellules.append(initCellules(8,probas))
    print(cellules[0],len(cellules[0]))
    for i in range(50):
        ligne=mouvementFile(cellules[0],probas)
        print(ligne,len(ligne))
    print(cellules[0],len(cellules[0]))
def accidentTest(ligne):
    """ligne est la dernière ligne de cellule. Renvoie True pour un accident
    et False sinon. Accident si d=0."""
    for i in range(len(ligne)):
        if (ligne[i][5]==0) : return True
    return False
def nouvLigne(ligne,probas,accident):
    return transitionFile(mouvementFile(ligne,probas),accident)
def testSimulation(duree,probas):
    """probas=[[ p_c1, p_c2,1-p_c1-p_c2],[p_an,1-p_an],[p_ds,1-p_ds]
    ,[p_e, p_eS,p_r,p_rS]].
    Duree est le nombre d'itération maximale de la simulation.
    Test la simulation avant de l'intégrer à une interface graphique."""
    cellules=[]
    cellules.append(initCellules(8,probas))
    print(cellules)
    for i in range(duree):
        ligne=transitionFile(mouvementFile(cellules[i],probas),True)
        print(ligne,len(ligne))
        cellules.append(ligne)
        if accidentTest(ligne) : return print("accident",i)








