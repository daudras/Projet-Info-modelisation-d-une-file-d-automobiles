from tkinter import *



class Application(Tk):
	def __init__(self, i=30):
		Tk.__init__(self)        # constructeur de la classe parente
		self.i = i
		self.can =Canvas(self, width =1200, height =600, bg ="white")
		self.can.pack(side =TOP, padx =5, pady =5)
		Button(self, text ="file suivante de voiture", command =self.dessine).pack(side =LEFT)

		Button(self, text ="Coloriage des cellules", command =self.coloriage).pack(side =LEFT)

	def dessine(self):
		"instanciation de 19 cellules dans le canevas"
		self.c1 = Cellule(self.can, 10, self.i, 30, 60, 1, 1, 1)
		self.c2 = Cellule(self.can, 130, self.i)
		self.c3 = Cellule(self.can, 250, self.i)
		self.c4 = Cellule(self.can, 370, self.i)
		self.c5 = Cellule(self.can, 490, self.i)
		self.c6 = Cellule(self.can, 610, self.i)
		self.c7 = Cellule(self.can, 730, self.i)
		self.c8 = Cellule(self.can, 850, self.i)
		self.c9 = Cellule(self.can, 970, self.i)
		self.c10 = Cellule(self.can, 1090, self.i)
		self.i += 65


	def coloriage(self):
		"coloriage d'une cellule et ses fenetres selon les valeurs de c, an, ds, a, v, d"
		self.c1.colorer()
		self.c2.colorer()
		self.c3.colorer()
		self.c4.colorer()
		self.c5.colorer()
		self.c6.colorer()
		self.c7.colorer()
		self.c8.colorer()
		self.c9.colorer()
		self.c10.colorer()


class Cellule :
	def __init__(self, canev, x=0, y=0, l = 90, h = 60, c = 1, an = 0, ds = 0, a = -2, v = 2, d = 4, coul = 'navy'):
		"dessin d'une Cellule en <x,y> dans le canevas <canev>"
		# mÃƒÂ©morisation des paramÃƒÂ¨tres dans des variables d'instance :
		self.canev = canev
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
		#self.cote =
		# rectangle de base : lxh pixels :
		self.item = canev.create_rectangle(x, y, x+l, y+h, fill =coul)

		# 3 fenÃƒÂªtres de Self.xf x self.yf pixels, ÃƒÂ©cartÃƒÂ©es de 2 pixels :

		self.fen =[]    # pour mÃƒÂ©moriser les rÃƒÂ©f. des fenÃƒÂªtres
		#parametrisation des dimensions de la fenetre de facon a creer trois fenetres bans chaque cellule aux dimensions dependantes de celle de la Cellule
		self.xf = x + 2
		self.yf = y+2
		self.cote = l/3 - 2
		self.hf = h - 10
		for i in range(1, 4, 1):

			self.fen.append(self.canev.create_rectangle(self.xf, self.yf,
								self.xf+ self.cote , self.yf + self.hf, fill ='white'))
			self.xf += self.cote+2


	def colorer(self):
		"dÃƒÂ©clencher le coloriage d'une cellule et ses fenetres selon les valeurs de c, an, ds, a, v, d"

		if (self.c == 1):
			if(self.an==1):
				if(self.ds==1):
								self.canev.itemconfigure(self.item, fill ='light green')
				else : self.canev.itemconfigure(self.item, fill ='green')
			elif (self.ds==1):
							self.canev.itemconfigure(self.item, fill ='turquoise')
			else: self.canev.itemconfigure(self.item, fill ='cyan')
		elif (self.c == 2):
			if (self.an == 1):
				if (self.ds == 1): self.canev.itemconfigure(self.item, fill ='indigo')
				else: self.canev.itemconfigure(self.item, fill ='purple')
			elif(self.ds == 1): self.canev.itemconfigure(self.item, fill ='purple')
			else: self.canev.itemconfigure(self.item, fill ='magenta')
		else:
			if(self.an==1):
				if(self.ds==1):
								self.canev.itemconfigure(self.item, fill ='orange+red')
				else : self.canev.itemconfigure(self.item, fill ='orange')
			elif (self.ds == 1): self.canev.itemconfigure(self.item, fill ='yellow + orange')
			else: self.canev.itemconfigure(self.item, fill ='yellow')
		if self.a == -3: self.canev.itemconfigure(self.fen[0], fill ='yellow')
		if self.a == -2: self.canev.itemconfigure(self.fen[0], fill ='yellow+orange')
		if self.a == -1: self.canev.itemconfigure(self.fen[0], fill ='orange')
		if self.a == 0: self.canev.itemconfigure(self.fen[0], fill ='white')
		if self.a == 1: self.canev.itemconfigure(self.fen[0], fill ='red+orange')
		if self.a == 2: self.canev.itemconfigure(self.fen[0], fill ='magenta')
		if self.a == 3: self.canev.itemconfigure(self.fen[0], fill ='purple')
		if self.v == 0: self.canev.itemconfigure(self.fen[1], fill ='white')
		if self.v == 1: self.canev.itemconfigure(self.fen[1], fill ='turquoise')
		if self.v == 2: self.canev.itemconfigure(self.fen[1], fill ='cyan')
		if self.v == 3: self.canev.itemconfigure(self.fen[1], fill ='indigo')
		if self.d == 0: self.canev.itemconfigure(self.fen[2], fill ='black')
		if self.d == 1: self.canev.itemconfigure(self.fen[2], fill ='red+orange')
		if self.d == 2: self.canev.itemconfigure(self.fen[2], fill ='magenta')
		if self.d == 3: self.canev.itemconfigure(self.fen[2], fill ='purple')
		if self.d == 4: self.canev.itemconfigure(self.fen[2], fill ='purple')
		if self.d == 5: self.canev.itemconfigure(self.fen[2], fill ='indigo')
		if self.d == 6: self.canev.itemconfigure(self.fen[2], fill ='cyan')
		if self.d == 7: self.canev.itemconfigure(self.fen[2], fill ='turquoise')
		if (self.c == 0 and self.an == 0 and self.ds == 0 and self.a == -1 and self.v==0 and self.d==-1):
																	self.canev.itemconfigure(self.fen[0], fill ='red')
																	self.canev.itemconfigure(self.fen[1], fill ='red')
																	self.canev.itemconfigure(self.fen[2], fill ='red')

		if (self.c == 0 and self.an == 0 and self.ds == 0 and self.a == -1 and self.v == 1 and self.d == -1):
																		self.canev.itemconfigure(self.fen[0], fill ='black')
																		self.canev.itemconfigure(self.fen[1], fill ='black')
																		self.canev.itemconfigure(self.fen[2], fill ='black')

Application().mainloop()