 #!/usr/bin/python
# -*-coding:UTF-8 -*

#Circulation automobile d'une file de voiture 
#Il est question de creer 10 cellules ayant chacune en elle trois fenetres, avec possibilite de modifier individuellement les couleurs des fenetres et cellules en faisant appel aux fonctions selon le besoin : couleur_fenetre, tte(), changecolor


from tkinter import *
 

class Application(Tk):
	
	#---definition des fonctions gestionnaires des evenements, et creation du widget principal

	def __init__(self):
		Tk.__init__(self)        # constructeur de la classe parente
		
		self.can =Canvas(self, width =1200, height =600, bg ="white")			

		self.can.pack(side =TOP, padx =5, pady =5)
		Button(self, text ="File de voiture", command=self.dessine).pack(side =LEFT)
	
	
	def dessine(self):
		
		"instanciation de 10 cellules dans le canevas"
		
		self.c1 = Cellule(self.can, 10, 30)
		self.c2 = Cellule(self.can, 130, 30, 'dark green')
		self.c3 = Cellule(self.can, 250, 30, 'maroon')
		self.c4 = Cellule(self.can, 370, 30, 'purple')
		self.c5 = Cellule(self.can, 490, 30, 'gray')
		self.c6 = Cellule(self.can, 610, 30, 'white')
		self.c7 = Cellule(self.can, 730, 30, 'blue')
		self.c8 = Cellule(self.can, 850, 30, 'red')
		self.c9 = Cellule(self.can, 970, 30)
		self.c10 = Cellule(self.can, 1090, 30)
		
	
				
 
	def couleur_fenetre(self):
		"appel de la modification des couleur effectue en tte() dans la classe Cellule"
		self.c3.tte()
		self.c4.tte()

#Construction de chaque cellule avec en elle trois fenetres et fonctions agissant sur cette classe eventuellement pour la modification des couleurs
class Cellule:
	def __init__(self, cane, x, y, coul ='navy'):
		"dessin d'une cellule en <x,y> dans le canevas <canev>"
		# mémorisation des paramètres dans des variables d'instance :
		self.cane, self.x, self.y = cane, x, y
		# rectangle de base : 95x60 pixels :
		cane.create_rectangle(x, y, x+95, y+60, fill =coul)
		# 3 fenêtres de 25x55 pixels, écartées de 5 pixels :
		self.fen =[]    # pour mémoriser les réf. des fenêtres 
		
		def changecolor():
			"Pour determiner la couleur de chaque fenetre"
			couleur = "white"
			
			
		for xf in range(x +5, x +90, 30):
			self.fen.append(cane.create_rectangle(xf, y+5,
								xf+25, y+55, fill =changecolor()))
								
	def tte(self):
			"modifier la couleur de toutes les fenetres d'une cellule"
			for f in self.fen:
				self.cane.itemconfigure(f, fill ='yellow')		 
 
Application().mainloop()