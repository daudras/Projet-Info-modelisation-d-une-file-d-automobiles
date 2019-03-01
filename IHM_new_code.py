 #!/usr/bin/python
# -*-coding:UTF-8 -*

#Circulation automobile d'une file de voiture 
#Il est question de creer 10 cellules ayant chacune en elle trois fenetres, avec possibilite de modifier individuellement les couleurs des fenetres et cellules en faisant appel aux fonctions selon le besoin : couleur_fenetre, tte(), changecolor


from tkinter import *


class Application(Tk):
	
	#---definition des fonctions gestionnaires des evenements, et creation du widget principal

	def __init__(self, i = 0):
		Tk.__init__(self)        # constructeur de la classe parente
		
		self.i = i
		self.can =Canvas(self, width =1200, height =600, bg ="white")			

		self.can.pack(side =TOP, padx =5, pady =5)
		Button(self, text ="File de voiture", command=self.ligne_suivante).pack(side =LEFT)
	
	
	
		
		self.i = i
	self.l1 = l1
	l1 = Ligne_de_cellules(self.can)
	l1.x = 0
	l1.y = 0
	l1.l = 90
	l1.h = 60
	
    def ligne_suivante(self):
			"instanciation de 10 lignes de cellules dans le canevas"
			if i < 10:
			l1.h += 65
			l1 = Ligne_de_cellules(self.can)
			i += 1					
		
class Cellule:
	def __init__(self, cane, x=0, y=0, l = 90, h = 60, c = 0, an = 0, ds = 0, a = 0, v = 0, d = 0, coul = 'navy'):
	#"dessin d'une cellule en <x,y> a la ligne lidans le canevas <cane>"	
	# mémorisation des paramètres dans des variables d'instance :
		
		self.cane = cane
		self.x = x
		self.y = y
		self.l = l
		self.h = h
		self.c = c
		self.an = an
		self.ds = ds
		self.a = a
		self.v = v
		self.d = d
		self.coul = coul
		
		# rectangle de base : 95x60 pixels :
			
		cane.create_rectangle(x, y, x+l, y+h, fill = coul)
		
		# 3 fenêtres de 25x55 pixels, écartées de 5 pixels :
			
		self.fen =[]    # pour mémoriser les réf. des fenêtres
		
		for xf in range(x + 2, x + l, 30):
			self.fen.append(cane.create_rectangle(xf, y+2,
								xf + cote - 2, y + h - 2, fill =changecolor()))
								
	def changecolor(self):
		"Pour determiner la couleur de la cellule et de chaque fenetre"
		if (c = 0 & an = 0 & ds = 0 & a = -1 & v = 0 & d = -1)
		if (c = 0 & an = 0 & ds = 0 & a = -1 & v = 1 & d = -1)
		if c = 1:
			if(an=1):
				if(ds=1):
					coul = "light green"
					else: coul = "green"
			elif (ds=1):
				coul = "turquoise"
				else: coul = "cyan"
		elif (c = 2):
			if (an = 1):
				if (ds = 1): coul = "indigo"
				else: coul = "purple"
			elif(ds = 1): coul = "purple"
			else: coul = "magenta"
		else:
			if(an=1):
				if(ds=1):
					coul = "orange-red"
					else : coul = "orange"
			elif (ds = 1): coul = "yellow+orange"
			else: coul = "yellow"
	if a = -3: color.self.fen[0]= "yellow"
	if a = -2: color.self.fen[0]= "yellow+orange"
	if a = -1: color.self.fen[0]= "orange"
	if a = 0: color.self.fen[0]= "white"
	if a = 1: color.self.fen[0]= "red+orange"
	if a = 2: color.self.fen[0]= "magenta"
	if a = 3: color.self.fen[0]= "purple"
	if v = 0: color.self.fen[1]= "white"
	if v = 1: color.self.fen[1]= "turquoise"
	if v = 2: color.self.fen[1]= "cyan"
	if v = 3: color.self.fen[1]= "indigo"	
	if d = 0: color.sefl.fen[2]= "black"	
	if d = 1: color.sefl.fen[2]= "red+orange"
	if d = 2: color.sefl.fen[2]= "magenta"
	if d = 3: color.sefl.fen[2]= "purple"
	if d = 4: color.sefl.fen[2]= "purple"
	if d = 5: color.sefl.fen[2]= "indigo"
	if d = 6: color.sefl.fen[2]= "cyan"
	if d = 7: color.sefl.fen[2]= "turquoise"
	
class Ligne_de_cellules(Cellule(cane [, x [, y [, l [, h [, c [, an [, ds [, a [, v [, d [, coul ]]]]]]]]]]]))
		def __init__(self, cane, x, y, l , h, c, an, ds, a, v, d, coul , i = 10)
		Cellule.__inti__(self, cane, x, y, l , h, c, an, ds, a, v, d, coul)
		self.i = i
		#ligne de cellules
		
		self.ligne_de_cellules[]
		
		for xi in range (x, x + 900, 95)
		
				self.ligne_de_cellules.append(Cellule(cane, x, y))
				
				
						Application().mainloop()