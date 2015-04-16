#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grille import Grille, Case
from heapq import heappush, heappop

def AEtoile(grille, noeud_source, noeud_arrive):
	parent_de_noeud = {} # dictionnaire noeud parent du noeud
	liste_ouverte = [] # noeuds étudiés
	liste_fermee = [] # noeuds appartiennent potentiellement à la solution

	parent_de_noeud[noeud_source.get_hash()] = None
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

		if len(liste_ouverte) != 0:
			priorite_meilleur_noeud, meilleur_noeud = heappop(liste_ouverte)
			print liste_ouverte,len(liste_ouverte)
			print meilleur_noeud
			liste_ouverte.remove((meilleur_noeud.cout, meilleur_noeud))
			liste_fermee.append(meilleur_noeud)
			noeud_precedant = noeud_courant
			noeud_courant = meilleur_noeud
			parent_de_noeud[noeud_courant.get_hash()] = noeud_precedant
		else:
			return False
		dessiner_grille_AEtoile(grille, liste_ouverte, liste_fermee, noeud_source, noeud_arrive)
	return True

def dessiner_grille_AEtoile(grille, case_a_etudier, case_etudiees, source, arrivee):
	compte = 0
	dessin = ""
	for case in self.cases:
		if case == source:
			dessin += "S"
		elif case == arrivee:
			dessin +=  "A"
		elif case in case_etudiees:
			dessin += "#"
		elif case in case_a_etudier:
			dessin += "?"
		elif case.cout > 1:
			dessin += "x"
		else:
			dessin += " "

		if compte%self.largeur == self.largeur-1:
			dessin += "\n"
		compte+=1
	print dessin

if __name__ == '__main__':
	g = Grille(10,10,"von_neumann")
	source = None
	arrivee = None
	for case in g.cases:
		if case.cout == 1:
			source = case
			break
	for case in g.cases:
		if case.cout == 1 and case != source:
			arrivee = case
			break

	AEtoile(g, source, arrivee)