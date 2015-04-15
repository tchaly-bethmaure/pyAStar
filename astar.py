class AEtoileNoeud(Noeud):
	def __init__(self,label,cost):
		# super init
		self.marque=False
		self.cout=cout

def AEtoile(grille, noeud_source, noeud_arrive):
	parent_de_noeud = {} # dictionnaire noeud parent du noeud
	liste_ouverte = [] # noeuds étudiés
	liste_fermee = [] # noeuds appartiennent potentiellement à la solution

	parent_de_noeud[noeud_source] = None
	noeud_courant = noeud_source
	while(noeud_courant != noeud_arrive):	
		if(not noeud_courant in liste_fermee):
			# heuristique = d(source, noeud) + d(arrivée, noeud)
			noeud_courant.cout = grille.distance(noeud_courant, noeud_source) + grille.distance(noeud_courant, noeud_arrive)
			if(noeud_courant in liste_ouverte):
				noeud_dans_liste = None	
				priorite_dans_liste = None	
				for priorite,noeud in liste_ouverte:
					if noeud == noeud_courant:
						noeud_dans_liste = noeud
				if(noeud_courant.cout < noeud_dans_liste.cout):
					liste_ouverte.remove((noeud_dans_liste.cout, noeud_dans_liste))
			heappush(liste_ouverte, (noeud_courant.cout, noeud_courant))	

		if(len(liste_ouverte) != 0):
			priorite_meilleur_noeud, meilleur_noeud = heappop(liste_ouverte)
			liste_ouverte.remove((meilleur_noeud.cout, meilleur_noeud))
			liste_fermee.append(meilleur_noeud)
			noeud_precedant = noeud_courant
			noeud_courant = meilleur_noeud
			parent_de_noeud[noeud_courant] = noeud_precedant
		else:
			return False
	return True
