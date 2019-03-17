from random import randint
from tkinter import*
from statistics import mean,pvariance
from transition import initCellules,nouvLigne,accidentTest
from statistiques import statVA
from IHM_menu import menuIhm
#from IHM_update_2Modif import Application

def scrollH():
    print("scroll haut")
def scrollB():
    print("scroll bas")
def zoomP():
    print("zoom plus")
def zoomM():
    print("zoom moins")
def fenInterupt(e):
    """e : string correspond à une interruption de la boucle.
    Affiche l'interruption.
    retourne True pour signaler une interruption """
    if e=="accident": affInt.set("Il s'est produit un accident !")
    if e=="temps": affInt.set("Le temps est écoulé")
    return True
def lancement(nbCel,probas,accident,tMax):
    initTransition(nbCel,probas)
    iterer(probas,accident,tMax)
def initTransition(n,probas):
    """crèe une première ligne de n cellules pour démarrer l'algorithme de transition."""
    cellules.append(initCellules(n,probas))
def iterer(probas,accident,tMax):
    """probas : listes de float, accident : booléen, tMax : int pour temps max.
    mets à jour la matrice cellules, les statistiques, le temps, le graphisme et
    s'appelle à nouveau sauf interruption.
    retourne False pour aucune interruption."""
    i=temps.get()
    print(cellules[i])
    statistique(i)
    #afCellules.append(Application(drawing,cellules[i],i))
    #afCellules[i].dessine()
    nbCel.set(len(cellules[i]))
    if accidentTest(cellules[i]) & accident: return fenInterupt("accident")
    if i>=tMax: return fenInterupt("temps")
    cellules.append(nouvLigne(cellules[i],probas,accident))
    temps.set(i+1)
    tourne[0]=ihm.after(100*2,iterer,probas,accident,tMax)
    return False
def statistique(i):
    """récupère les statistiques de la ligne i des tableaux cellules et listesVA
     et les places dans les objets correspondants pour affichage."""
    varStat=statVA(i,listesVA,cellules[i])
    for i in range(9): statMenu[i].set(varStat[i])
def init():
    """initialise les variables en relation avec le bouton recommencer"""
    global cellules, afCellules
    for i in range(2): listesVA[i]=[]
    cellules=[]
    afCellules=[]
    for i in range(9): statMenu[i].set(0)
    temps.set(0)
    nbCel.set(15)
    affInt.set("")


if __name__ == '__main__':
    tourne=[0]
    #listesVA est ["v":[],"pol":[]]
    listesVA=[[],[]]
    ihm=Tk()
    drawing=Canvas(ihm,width=1000,height=700)
    menu=Frame(ihm,bd=2,relief=RIDGE)
    affInt=StringVar()
    statMenu=[]
    for i in range (9): statMenu.append(IntVar())
    temps=IntVar()
    nbCel=IntVar()
    init()
    ihm.resizable(False,False)
    ihm.title("Évolution d’une file de voiture en fonction du comportement des automobilistes")
    menuIhm(tourne,iterer,ihm,menu,drawing,affInt,statMenu,temps,nbCel,lancement,
        init,scrollH,scrollB,zoomP,zoomM)
    ihm.mainloop()

