from tkinter import*


def menuIhm(tourne,iterer,ihm,menu,drawing,affInt,statMenu,temps,nbCel,lancement,
        init,scrollH,scrollB,zoomP,zoomM):
    """tourne est un tableau d'une case contenant l'id créer par after pour relancer itere
    itere : fonction qui crèe la boucle avec after
    ihm est une instance Tk de la fenêtre,
    menu est un frame de ihm pour y placer le menu
    drawing est le canvas placé à côté du menu
    affInt : StringVar pour le texte en cas d'interruption
    statMenu est une liste de IntVar qui reçoie les paramètres statistiques
    temps : intVar pour le temps courant
    nbCel : intVar pour le nombre de cellules de départ et dans la ligne courante
    lancement, init, scrollH, scrollB, zoomP, zoomM sont les fonctions correspondantes aux boutons.
    Cette fonction se charge de toute la partie graphique du menu"""
    # ** la fenêtre **
    drawing.grid(row=0,column=0)
    menu.grid(row=0,column=1,sticky=N)
    # ** le menu des variables **
    menuV=Frame(menu)
    menuV.grid(row=0,column=1)
    Label(menuV,text="Réglage des probabilités en %",width=30
        ).grid(row=0,column=0,columnspan=2)
    probaNom=["p_c1", "p_c2", "p_an", "p_ds", "p_e", "p_eS", "p_r", "p_rS"]
    probaMenu=[]
    entree=[]
    for i in range (8): probaMenu.append(IntVar())
    for i in range (8):
        Label(menuV,text=probaNom[i],width=3).grid(row=i+1,column=0)
        entree.append(Entry(menuV,textvariable=probaMenu[i],width=3))
        entree[i].grid(row=i+1,column=1,sticky=W)
    accident= IntVar()
    accident.set(0)
    Checkbutton(menuV,text="Autoriser un accident",variable=accident).grid(row=2,column=1,sticky=E)
    Label(menuV,text="nombres de cellules").grid(row=4,column=1,sticky=E)
    E_nbCel=Entry(menuV,textvariable=nbCel,width=3)
    E_nbCel.grid(row=4,column=2,sticky=W)
    L_nbCel=Label(menuV,text="",width=3)
    L_nbCel.grid(row=4,column=2,sticky=W)
    L_nbCel.grid_remove()
    tMax=IntVar()
    Label(menuV,text="temps max").grid(row=5,column=1,sticky=E)
    Entry(menuV,textvariable=tMax,width=3).grid(row=5,column=2,sticky=W)
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
    Button(menuV,command=aide,text='Aide').grid(row=7,column=1,sticky=E)
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
    def initVarMenu():
        affInt.set("")
        tMax.set(20)
        accident.set(0)
        choixScenario.set("normal")
        choixEntreeSortie.set("normal")
        scenario("normal")
        entreeSortieFct("normal")
    initVarMenu()
    def formatProbas():
        """formate les données pour une utilisation par l'algorithme de transition"""
        probas=[probaMenu[i].get()/100 for i in range(8)]
        probas=[[probas[0],probas[1],round(1-probas[0]-probas[1],2)],
        [probas[2],round(1-probas[2],2)],[probas[3],round(1-probas[3],2)],
        [probas[i+4] for i in range(4)]]
        return probas
    def lancer():
        boutonActiver.config(text='Pause',command=pause)
        boutonFinir.grid(row=13,column=0,sticky=W)
        E_nbCel.grid_remove()
        L_nbCel.config(text=nbCel.get())
        L_nbCel.grid()
        probas=formatProbas()
        lancement(nbCel.get(),probas,accident.get(),tMax.get())
    boutonActiver=Button(menuC,command=lancer,text='lancer la simulation')
    boutonActiver.grid(row=13,column=0,columnspan=2)
    def pause():
        ihm.after_cancel(tourne[0])
        boutonActiver.config(text='poursuivre la simulation',command=poursuivre)
    def poursuivre():
        boutonActiver.config(text='Pause',command=pause)
        if iterer(formatProbas(),accident.get(),tMax.get()): finir()
    def finir():
        ihm.after_cancel(tourne[0])
        boutonActiver.grid_remove()
        boutonFinir.config(text='recommencer',command=recommencer)
    boutonFinir=Button(menuC,command=finir,text='Finir')
    def recommencer():
        initVarMenu()
        L_nbCel.grid_remove()
        E_nbCel.grid()
        boutonActiver.config(command=lancer,text='lancer la simulation')
        boutonActiver.grid()
        boutonFinir.config(command=finir,text='Finir')
        boutonFinir.grid_forget()
        init()

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
    menuS=Frame(menu,bd=2)
    menuS.grid(row=4,column=1)
    Label(menuS,text="Statistiques",width=30
        ).grid(row=0,column=0,columnspan=2)
    # ** Sous-menu statistiques : tableau**
    menuST=Frame(menuS,bd=2,relief=GROOVE)
    menuST.grid(row=1,column=0,sticky=E,columnspan=2)
    statNom=["v_i","v_iVar","v","vVar","pol_i","pol_iVar","pol","polVar"]
    for i in range(0,8,2):
        for j in range(2):
            Label(menuST,text=statNom[i+j]+" : ").grid(row=i,column=0+2*j)
            Label(menuST,textvariable=statMenu[i+j],width=5).grid(row=i,column=1+2*j,sticky=W)
    def infoStat():
        texteInfoStat="""
        v_i est la vitesse moyenne des cellules dans la ligne courante, on peut parler
        de vitesse instantanée de la file de voitures.
        v_iVar est la variance correspondante à v_i
        v est la vitesse moyenne de la file depuis le début de la simulation.
        vVar est la variance correspondante à v.
        pol signifie niveau de polution engendré par le freinage et l'accélération,
        il correspond à la somme des carrés du paramètre accélération des cellules.
        pol_i, pol_iVar, pol, polVar ont la même signification que précédemment avec
        pol à la place de v.
        """
        try :
            ihm.nametowidget('messageInfoStat').destroy()
        except KeyError:
            Message(ihm,text=texteInfoStat, width=600,bg='white',name='messageInfoStat').grid(row=0,column=0)
    Label(menuS,text="cumule de pollution : "+str()).grid(row=2,column=0,sticky=E)
    Label(menuS,textvariable=statMenu[8]).grid(row=2,column=1,sticky=W)
    Label(menuS,text="temps : ").grid(row=3,column=0,sticky=E)
    Label(menuS,textvariable=temps).grid(row=3,column=1,sticky=W)
    Label(menuS,text="nombres de cellules : ").grid(row=4,column=0,sticky=E)
    Label(menuS,textvariable=nbCel,width=3).grid(row=4,column=1,sticky=W)
    Button(menuS,command=infoStat,text='Info').grid(row=4,column=1,sticky=E)
    Label(menu,textvariable=affInt).grid(row=5,column=0,columnspan=3)
