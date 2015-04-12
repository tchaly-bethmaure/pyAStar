class AEtoileNoeud(Noeud):
	def __init__(self,label,cost):
		# super init
		self.marque=False
		self.cout=cout

def AEtoile(graph, noeud_courant, noeud_source,noeud_arrive):
	parent_noeud = {} # dictionnaire noeud parent du noeud
	liste_ouverte = [] # noeuds étudiés
	liste_fermee = [] # noeuds appartiennent potentiellement à la solution

	while(noeud_courant != noeud_arrive):	
		if(not noeud_courant in liste_fermee):

			priorite_noeud_courant = 0 # calculer priorité
			if(noeud_courant in liste_ouverte):
				noeud_dans_liste = None	
				priorite_dans_liste = None	
				for priorite,noeud in liste_ouverte:
					if noeud == noeud_courant:
						noeud_dans_liste = noeud
						priorite_dans_liste = priorite
				if(noeud_courant.cout < noeud_dans_liste.cout):
					liste_ouverte.remove((priorite_dans_liste, noeud_dans_liste))
					pass
			heappush(liste_ouverte, (priorite_noeud_courant, noeud_courant))	

		if(len(liste_ouverte) != 0):
			priorite_meilleur_noeud, meilleur_noeud = heappop(liste_ouverte)
			liste_ouverte.remove((priorite_meilleur_noeud, meilleur_noeud))
			liste_fermee.append(meilleur_noeud)
			noeud_courant = meilleur_noeud
		else:
			return False
	return True
