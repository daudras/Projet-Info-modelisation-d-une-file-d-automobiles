from random import randint
from tkinter import*
from statistics import mean,pvariance
from transition import initCellules,nouvLigne


def menuIhm():
    # ** la fenêtre **
    drawing=Canvas(ihm,width=1000,height=700)
    drawing.grid(row=0,column=0)
    menu=Frame(ihm,bd=2,relief=RIDGE)
    menu.grid(row=0,column=1,sticky=N)
    # ** le menu des variables **
    menuV=Frame(menu)
    menuV.grid(row=0,column=1)
    Label(menuV,text="Réglage des probabilités en %",width=30
        ).grid(row=0,column=0,columnspan=2)
    probaNom=["p_c1", "p_c2", "p_an", "p_ds", "p_e", "p_eS", "p_r", "p_rS"]
    probaMenu=[]
    entree=[]
    for i in range (8): probaMenu.append(IntVar(menuV))
    for i in range (8):
        Label(menuV,text=probaNom[i],width=3).grid(row=i+1,column=0)
        entree.append(Entry(menuV,textvariable=probaMenu[i],width=3))
        entree[i].grid(row=i+1,column=1,sticky=W)
    accident= IntVar(menuV)
    accident.set(1)
    Checkbutton(menuV,text="Autoriser un accident",variable=accident).grid(row=10,column=1,sticky=W)
    def aide():
        texteAide="""
        p_c1 est la proportion de conducteurs ayant un objectif de diminution de la consommation.
        p_c2 est la proportion de conducteurs standards, dont le seul objectif est de se déplacer.
        p_c3 est la proportion de conducteur nerveux ou aimant jouer avec leur voiture (les autres).
        p_an est la proportion de conducteurs qui commencent à freiner lorsque la voiture qui les précède freine.
        p_ds est la proportion de conducteurs qui respectent les distances de sécurités.
        p_e est la probabilité d’entrée d’une cellule normale (automobile).
        p_eS est la probabilité d’entrée d’une cellule spéciale (feu ou rond-point).
        p_r est la probabilité de retrait d’une cellule normale.
        p_rS est la probabilité de retrait d’une cellule spéciale.
        """
        try :
            ihm.nametowidget('messageAide').destroy()
        except KeyError:
            Message(ihm,text=texteAide, width=600,bg='white',name='messageAide').grid(row=0,column=0)
    Button(menuV,command=aide,text='Aide').grid(row=12,column=1,sticky=E)
    # ** le menu des commandes **
    menuC=Frame(menu)
    menuC.grid(row=2,column=1)
    Label(menuC,text="",width=30).grid(row=0,column=0,columnspan=2)
    def scenario(e):
        for i in range (4):
            probaMenu[i].set(scenarii[e][i])
    scenarii = {'normal':(20,70,30,60),'prudent':(50,40,80,80),
        'nerveux':(10,20,30,10),'eco':(80,10,50,50)}
    scenario("normal")
    choixScenario = StringVar(menuC)
    Label(menuC,text="scenarii :").grid(row=11,column=0,sticky=W)
    choixScenario.set("normal")
    OptionMenu(menuC, choixScenario, *[nom for nom in scenarii.keys()],
        command=scenario).grid(row=11,column=1,sticky=E)
    def entreeSortieFct(e):
        for i in range (4):
            probaMenu[i+4].set(entreeSortie[e][i])
    entreeSortie = {'normal':(50,20,50,50), 'feux':(50,50,50,60),
        'libre':(50,5,50,10), 'mouvements':(70,20,70,50)}
    entreeSortieFct("normal")
    choixEntreeSortie = StringVar()
    Label(menuC,text="entrées sorties :").grid(row=12,column=0,sticky=W)
    choixEntreeSortie.set("normal")
    OptionMenu(menuC, choixEntreeSortie, *[nom for nom in entreeSortie.keys()],
        command=entreeSortieFct).grid(row=12,column=1,sticky=E)
    def formatProbas():
        """formate les données pour une utilisation par l'algorithme de transition"""
        probas=[probaMenu[i].get()/100 for i in range(8)]
        probas=[[probas[0],probas[1],round(1-probas[0]-probas[1],2)],
        [probas[2],round(1-probas[2],2)],[probas[3],round(1-probas[3],2)],
        [probas[i+4] for i in range(4)]]
        return probas
    def lancer():
        boutonActiver.config(text='Pause',command=pause)
        finir.grid(row=13,column=0,sticky=W)
        stat()
        probas=formatProbas()
        initTransition(8,probas)
        iterer(probas,accident.get())
    boutonActiver=Button(menuC,command=lancer,text='lancer la simulation')
    boutonActiver.grid(row=13,column=0,columnspan=2)
    def pause():
        ihm.after_cancel(tourne)
        boutonActiver.config(text='poursuivre la simulation',command=poursuivre)
    def poursuivre():
        boutonActiver.config(text='Pause',command=pause)
        iterer(formatProbas(),accident.get())
    def finir():
        print("stop")
        ihm.after_cancel(tourne)
        boutonActiver.destroy()
        finir.config(text='recommencer',command=recommencer)
    finir=Button(menuC,command=finir,text='Finir')
    def recommencer():
        menu.destroy()
        drawing.destroy()
        menuIhm()
    # ** le menu des commandes spéciales **
    menuSpe=Frame(menu)
    menuSpe.grid(row=3,column=1)
    Label(menuSpe,text="").grid(row=0,column=0)
    Label(menuSpe,text="scroll :").grid(row=1,column=0,sticky=W)
    Button(menuSpe,command=scrollH,text='haut').grid(row=1,column=1)
    Button(menuSpe,command=scrollB,text='bas').grid(row=1,column=2)
    Label(menuSpe,text="zoom :").grid(row=2,column=0,sticky=W)
    Button(menuSpe,command=zoomP,text='+').grid(row=2,column=1)
    Button(menuSpe,command=zoomM,text='-').grid(row=2,column=2)
    Label(menuSpe,text="").grid(row=3,column=0)
    # ** la fenêtre des statistiques **
    menuS=Frame(menu,bd=2,relief=RIDGE)
    menuS.grid(row=4,column=1)
    def stat():
        Label(menuS,text="Statistiques",width=30
            ).grid(row=0,column=0,columnspan=2)
        vitMoy=StringVar(menuS)
        pollution=StringVar(menuS)
        vitMoy=StringVar(menuS)
        pollution=StringVar(menuS)
        varStat=statistique()
        vitMoy.set(varStat[0])
        pollution.set(varStat[1])
        Label(menuS,text="vitesse moyenne : ").grid(row=1,column=0)
        Label(menuS,textvariable=vitMoy ).grid(row=1,column=1)
        Label(menuS,text="niveau de pollution : ").grid(row=2,column=0)
        Label(menuS,textvariable=pollution).grid(row=2,column=1)

def scrollH():
    print("scroll haut")
def scrollB():
    print("scroll bas")
def zoomP():
    print("zoom plus")
def zoomM():
    print("zoom moins")
def initTransition(n,probas):
    """crèe une première ligne de n cellules pour démarrer l'algorithme de transition """
    cellules.append(initCellules(n,probas))
def iterer(probas,accident):
    global tourne,temps
    print(cellules[temps],temps)
    cellules.append(nouvLigne(cellules[temps],probas,accident))
    temps+=1
    tourne=ihm.after(1000*2,iterer,probas,accident)


def listVA(i):
    """i est le numéro de ligne de la matrice cellules.
    en sortie v est une liste des vitesses contenus dans cette ligne
    et a une liste des carrés des accélérations. """
    v,a=[],[]
    for j in range(len(cellules[i])):
        v.append(cellules[i][j][4])
        a.append(cellules[i][j][3]**2)
    return v,a

def apListeVA(i):
    """met à jour les listes des vitesses, variances et
    carrée des accélérations, variances pour l'indice i de la matrice cellules."""
    listesVA["v"].append(mean(listVA(i)[0]))
    listesVA["varV"].append(pvariance(listVA(i)[0]))
    listesVA["a"].append(mean(listVA(i)[1]))
    listesVA["varA"].append(pvariance(listVA(i)[1]))

def statVA(i):
    """renvoie les données statistiques pour un affichage """
    return (listesVA["v"][i],listesVA["varV"][i],
        mean(listesVA["v"]),pvariance(listesVA["v"]),
        listesVA["a"][i],listesVA["varA"][i],
        mean(listesVA["a"]),pvariance(listesVA["a"]))
def statistique():
    return [1,2]


if __name__ == '__main__':
    listesVA={"v":[],"varV":[],"a":[],"varA":[]}
    temps=0
    cellules=[]
    init=True
    ihm=Tk()
    ihm.resizable(False,False)
    ihm.title("Évolution d’une file de voiture en fonction du comportement des automobilistes")
    menuIhm()
    ihm.mainloop()

