from IHM_update_clear_function import Cellule

def afCellules(drawing,ligne,i,h,k):
    """drawing:canvas Tkinter, i:n°de la ligne à afficher, h:hauteur d'une cellule
    k=l/h est la proportion d'une cellule.
    retourne la ligne d'objets cellules correspondante et l'affiche."""
    l=h*k
    ligneCel=[]
    for j in range(len(ligne)):
        ligneCel.append(Cellule(drawing, j*(l+1), i*(h+1), l, h, *ligne[j]))
        ligneCel[j].colorer()
    return ligneCel
def efCellules(ligneCel):
    """efface la ligne d'objets cellules, contenues dans la liste ligneCel, du canvas associé. """
    for i in range(len(ligneCel)):
        ligneCel[i].clear()




