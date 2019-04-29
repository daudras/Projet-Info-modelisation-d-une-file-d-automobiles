from tkinter import *
from random import randint


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
		self.c1 = Cellule(self.can, 10, self.i, 90, 60, 1, 1, 0, -1, 2, 3)
		self.c2 = Cellule(self.can, 130, self.i, 90, 60, 2, 1, 0, 1, 2, 2)
		self.c3 = Cellule(self.can, 250, self.i, 90, 60, 2, 1, 0, 0, 2, 2)
		self.c4 = Cellule(self.can, 370, self.i, 90, 60, 2, 0, 0, 1, 3, 3)
		self.c5 = Cellule(self.can, 490, self.i, 90, 60, 2, 1, 1, -1, 2, 4)
		self.c6 = Cellule(self.can, 610, self.i, 90, 60, 2, 0, 0, 1, 2, 4)
		self.c7 = Cellule(self.can, 730, self.i, 90, 60, 2, 1, 0, -1, 2, 2)
		self.c8 = Cellule(self.can, 850, self.i, 90, 60, 2, 1, 1, -1, 3, 2)
		self.c9 = Cellule(self.can, 970, self.i, 90, 60, 2, 0, 0, -1, 3, 3)
		self.c10 = Cellule(self.can, 1090, self.i, 90, 60, 1, 1, 0, 1, 2, 4)
		self.i += 65
		self.c1.clear()


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
	def __init__(self, canev, x=0, y=0, l = 90, h = 60, c = 0, an = 0, ds = 0, a = 0, v = 0, d = 0, coul = 'navy'):
		"dessin d'une Cellule en <x,y> dans le canevas <canev>"
		# mÃ©morisation des paramÃ¨tres dans des variables d'instance :
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

		# 3 fenÃªtres de Self.xf x self.yf pixels, Ã©cartÃ©es de 2 pixels :

		self.fen =[]    # pour mÃ©moriser les rÃ©f. des fenÃªtres
		#parametrisation des dimensions de la fenetre de facon a creer trois fenetres bans chaque cellule aux dimensions dependantes de celle de la Cellule
		self.xf = x + 3
		self.yf = y+2
		self.cote = l/3 - 4
		self.hf = h - 4
		for i in range(1, 4, 1):

			self.fen.append(canev.create_rectangle(self.xf, self.yf,
								self.xf+ self.cote , self.yf + self.hf, fill ='white'))
			self.xf += self.cote + 3


	def colorer(self):
		"dÃ©clencher le coloriage d'une cellule et ses fenetres selon les valeurs de c, an, ds, a, v, d"

		if (self.c == 1):
			if(self.an==1):
				if(self.ds==1):
								self.canev.itemconfigure(self.item, fill ='light green')
				else : self.canev.itemconfigure(self.item, fill ='green')
			elif (self.ds==1):
							self.canev.itemconfigure(self.item, fill ='#40E0D0')
			else: self.canev.itemconfigure(self.item, fill ='#00FFFF')
		elif (self.c == 2):
			if (self.an == 1):
				if (self.ds == 1): self.canev.itemconfigure(self.item, fill ='#4b0082')
				else: self.canev.itemconfigure(self.item, fill ='#800080')
			elif(self.ds == 1): self.canev.itemconfigure(self.item, fill ='#8B008B')
			else: self.canev.itemconfigure(self.item, fill ='#FF00FF')
		else:
			if(self.an==1):
				if(self.ds==1):
								self.canev.itemconfigure(self.item, fill ='#FF4500')
				else : self.canev.itemconfigure(self.item, fill ='#FFD700')
			elif (self.ds == 1): self.canev.itemconfigure(self.item, fill ='#ffae42')
			else: self.canev.itemconfigure(self.item, fill ='#FFFF00')
		if self.a == -3: self.canev.itemconfigure(self.fen[0], fill ='#FFFF00')
		if self.a == -2: self.canev.itemconfigure(self.fen[0], fill ='#ffae42')
		if self.a == -1: self.canev.itemconfigure(self.fen[0], fill ='#FFA500')
		if self.a == 0: self.canev.itemconfigure(self.fen[0], fill ='white')
		if self.a == 1: self.canev.itemconfigure(self.fen[0], fill ='#FF4500')
		if self.a == 2: self.canev.itemconfigure(self.fen[0], fill ='#FF00FF')
		if self.a == 3: self.canev.itemconfigure(self.fen[0], fill ='#800080')
		if self.v == 0: self.canev.itemconfigure(self.fen[1], fill ='white')
		if self.v == 1: self.canev.itemconfigure(self.fen[1], fill ='#40E0D0')
		if self.v == 2: self.canev.itemconfigure(self.fen[1], fill ='#00FFFF')
		if self.v == 3: self.canev.itemconfigure(self.fen[1], fill ='#4b0082')
		if self.d == 0: self.canev.itemconfigure(self.fen[2], fill ='black')
		if self.d == 1: self.canev.itemconfigure(self.fen[2], fill ='#FF4500')
		if self.d == 2: self.canev.itemconfigure(self.fen[2], fill ='#FF00FF')
		if self.d == 3: self.canev.itemconfigure(self.fen[2], fill ='#800080')
		if self.d == 4: self.canev.itemconfigure(self.fen[2], fill ='#8B008B')
		if self.d == 5: self.canev.itemconfigure(self.fen[2], fill ='#4B0082')
		if self.d == 6: self.canev.itemconfigure(self.fen[2], fill ='#00FFFF')
		if self.d == 7: self.canev.itemconfigure(self.fen[2], fill ='#40E0D0')
		if (self.c == 0 and self.an == 0 and self.ds == 0 and self.a == -1 and self.v==0 and self.d==-1):
																	self.canev.itemconfigure(self.fen[0], fill ='red')
																	self.canev.itemconfigure(self.fen[1], fill ='red')
																	self.canev.itemconfigure(self.fen[2], fill ='red')

		if (self.c == 0 and self.an == 0 and self.ds == 0 and self.a == -1 and self.v == 1 and self.d == -1):
																		self.canev.itemconfigure(self.fen[0], fill ='black')
																		self.canev.itemconfigure(self.fen[1], fill ='black')
																		self.canev.itemconfigure(self.fen[2], fill ='black')

	def clear (self):
			self.canev.delete(self.item)
			self.canev.delete(self.fen[0])
			self.canev.delete(self.fen[1])
			self.canev.delete(self.fen[2])

#Application().mainloop()