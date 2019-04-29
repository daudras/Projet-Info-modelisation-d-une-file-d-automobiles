from random import randint
from tkinter import*
from copy import deepcopy
from transition import initCellules,nouvLigne,accidentTest
from statistiques import statsLigne, afStatistiques
from IHM_menu import menuIhm
from afCellules import afCellules, efCellules
def main():
    """Lance le programme.
    Définit les variables qui concerveront les données tout au long de l'exécution."""
    tourne=[0]
    memoire={"cellules":[],"afCellules":[],"listeV":[],"listeP":[],"inAfCel":[0,20]}
    ihm=Tk()
    ihm.resizable(width=None, height=None)
    hCanvas=700
    kCanvas=1.6
    drawing=Canvas(ihm,width=hCanvas*kCanvas,height=hCanvas+15)
    menu=Frame(ihm,bd=2,relief=RIDGE)
    affInt=StringVar()
    statMenu=[]
    for i in range (9):
        statMenu.append(IntVar())
    temps=IntVar()
    nbCel=IntVar()
    tempsHist=IntVar()
    ihm.resizable(False,False)
    ihm.title("Évolution d’une file de voiture en fonction du comportement des automobilistes")
    def scrollH():
        """scroll vers le haut, déplace les céllules vers le bas et fait apparaître
         la cellule précédente en haut de l'écran.
         Actualise les statistiques par rapport à la dernière cellule affichée."""
        tempsAfCel0=temps.get()-memoire["inAfCel"][0]
        if tempsAfCel0 < 0: return
        if memoire["inAfCel"][0] >= memoire["inAfCel"][1]:
            efCellules(memoire["afCellules"][memoire["inAfCel"][1]-1])
            stats_i=statsLigne(deepcopy(memoire["cellules"][tempsAfCel0+memoire["inAfCel"][1]-1]))
            afStatistiques(stats_i, memoire["listeV"][:tempsAfCel0+memoire["inAfCel"][1]],
                 memoire["listeP"][:tempsAfCel0+memoire["inAfCel"][1]], statMenu)
            tempsHist.set(tempsAfCel0+memoire["inAfCel"][1]-1)
        else:
            memoire["afCellules"].append(0)
            tempsHist.set(temps.get())
        n=len(memoire["afCellules"])
        for i in range(1,n):
            efCellules(memoire["afCellules"][n-i-1])
            memoire["afCellules"][n-i]=afCellules(drawing,deepcopy(
                memoire["cellules"][tempsAfCel0+n-i]), n-i,round(hCanvas/memoire["inAfCel"][1],1),kCanvas)
        memoire["afCellules"][0]=afCellules(drawing,deepcopy(
            memoire["cellules"][tempsAfCel0]), 0,round(hCanvas/memoire["inAfCel"][1],1),kCanvas)
        memoire["inAfCel"][0]+=1

    def scrollB():
        """scroll vers le bas, déplace les céllules vers le haut et fait apparaître
         la cellule suivante en haut de l'écran.
         Actualise les statistiques par rapport à la dernière cellule affichée."""
        tempsAfCel0=temps.get()-memoire["inAfCel"][0]
        if memoire["inAfCel"][0] == 0: return
        efCellules(memoire["afCellules"][0])
        for i in range(1,len(memoire["afCellules"])):
            efCellules(memoire["afCellules"][i])
            memoire["afCellules"][i-1]=afCellules(drawing,deepcopy(
                memoire["cellules"][tempsAfCel0+i+1]), i-1,round(hCanvas/memoire["inAfCel"][1],1),kCanvas)
        tempsAfCelMax=temps.get()-memoire["inAfCel"][0]+memoire["inAfCel"][1]+1
        if tempsAfCelMax > temps.get():
            memoire["afCellules"].pop()
            tempsHist.set(temps.get())
        else:
            memoire["afCellules"][memoire["inAfCel"][1]-1]=afCellules(drawing,deepcopy(
                memoire["cellules"][tempsAfCelMax]), memoire["inAfCel"][1]-1,round(hCanvas/memoire["inAfCel"][1],1),kCanvas)
            stats_i=statsLigne(deepcopy(memoire["cellules"][tempsAfCelMax]))
            afStatistiques(stats_i, memoire["listeV"][:tempsAfCelMax+1], memoire["listeP"][:tempsAfCelMax+1], statMenu)
            tempsHist.set(tempsAfCelMax)
        memoire["inAfCel"][0]-=1
    def zoomP():
        """zoom plus, augmente la taille des céllules pour en faire disparaître la ligne du haut
         La ligne du bas reste en place."""
        tempsAfCel0=temps.get()-memoire["inAfCel"][0]
        if memoire["inAfCel"][1]<10 or memoire["inAfCel"][0]<2 : return
        memoire["inAfCel"][0]-=1
        memoire["inAfCel"][1]-=1
        efCellules(memoire["afCellules"][0])
        for i in range(1,len(memoire["afCellules"])):
            efCellules(memoire["afCellules"][i])
            memoire["afCellules"][i]=afCellules(drawing,deepcopy(
                memoire["cellules"][tempsAfCel0+1+i]), i-1,round(hCanvas/memoire["inAfCel"][1],1),kCanvas)
            memoire["afCellules"][i-1]=memoire["afCellules"][i]
        memoire["afCellules"].pop()
    def zoomM():
        """zoom moins, diminue la taille des céllules pour en faire apparaître
         une ligne supplémentaire en bas. La ligne du haut reste en place.
         Actualise les statistiques par rapport à la dernière cellule affichée."""
        tempsAfCel0=temps.get()-memoire["inAfCel"][0]
        tempsAfCelMax=temps.get()-memoire["inAfCel"][0]+memoire["inAfCel"][1]+1
        memoire["inAfCel"][1]+=1
        for i in range(len(memoire["afCellules"])):
            efCellules(memoire["afCellules"][i])
            memoire["afCellules"][i]=afCellules(drawing,deepcopy(
                memoire["cellules"][tempsAfCel0+1+i]), i,round(hCanvas/memoire["inAfCel"][1],1),kCanvas)
        if tempsAfCelMax <= temps.get():
            memoire["afCellules"].append(afCellules(drawing,deepcopy(
                memoire["cellules"][tempsAfCelMax]), memoire["inAfCel"][1]-1,round(hCanvas/memoire["inAfCel"][1],1),kCanvas))
            stats_i=statsLigne(deepcopy(memoire["cellules"][tempsAfCelMax]))
            afStatistiques(stats_i, memoire["listeV"][:tempsAfCelMax+1],
                 memoire["listeP"][:tempsAfCelMax+1], statMenu)
            tempsHist.set(tempsAfCelMax)
    def fenInterupt(e):
        """e : string correspond à une interruption de la boucle.
        Affiche l'interruption.
        retourne True pour signaler une interruption """
        if e=="accident": affInt.set("Il s'est produit un accident !")
        if e=="temps": affInt.set("Le temps est écoulé")
        return True
    def iterer(probas,accident,tMax):
        """probas : listes de float, accident : booléen, tMax : int pour temps max.
        mets à jour la matrice cellules, les statistiques, le temps, le graphisme et
        s'appelle à nouveau sauf interruption.
        retourne False pour aucune interruption."""
        t=temps.get()
        if t==-1: memoire["cellules"].append(initCellules(nbCel.get(),probas))
        else:
            memoire["cellules"].append(nouvLigne(deepcopy(memoire["cellules"][t]),probas,accident))
        temps.set(t+1)
        t=temps.get()
        tempsHist.set(t)
        nbCel.set(len(memoire["cellules"][t]))
        while nbCel.get() >= memoire["inAfCel"][1]-2: zoomM()
        stats_i=statsLigne(deepcopy(memoire["cellules"][t]))
        memoire["listeV"].append(stats_i[0])
        memoire["listeP"].append(stats_i[2])
        afStatistiques(stats_i, memoire["listeV"][:], memoire["listeP"][:], statMenu)
        while memoire["inAfCel"][0] >= memoire["inAfCel"][1]: scrollB()
        memoire["afCellules"].append(afCellules(drawing,deepcopy(memoire["cellules"][t]),
                memoire["inAfCel"][0],round(hCanvas/memoire["inAfCel"][1],1),kCanvas))
        memoire["inAfCel"][0]+=1
        if accidentTest(deepcopy(memoire["cellules"][t])) & accident: return fenInterupt("accident")
        if t==tMax:
            return fenInterupt("temps")
        tourne[0]=ihm.after(100*3,iterer,probas,accident,tMax)
        return False
    def init():
        """initialise les variables en relation avec le bouton recommencer"""
        memoire["cellules"]=[]
        memoire["listeV"]=[]
        memoire["listeP"]=[]
        memoire["inAfCel"]=[0,20]
        for i in range(len(memoire["afCellules"])):
            efCellules(memoire["afCellules"][i])
        memoire["afCellules"]=[]
        for i in range(9): statMenu[i].set(0)
        temps.set(-1)
        nbCel.set(20)
        affInt.set("")
    init()
    menuIhm(tourne,iterer,ihm,menu,drawing,affInt,statMenu,temps,nbCel,tempsHist,init,
        scrollH,scrollB,zoomP,zoomM)
    ihm.mainloop()


if __name__ == '__main__':
    main()

