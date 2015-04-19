#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grille import Grille, Case
from heapq import heappush, heappop

def AEtoile(grille, noeud_source, noeud_arrive):
	parent_de_noeud = {} # dictionnaire noeud parent du noeud
	liste_ouverte = [] # noeuds étudiés
	liste_fermee = [] # noeuds appartiennent potentiellement à la solution
	print noeud_source, noeud_arrive
	parent_de_noeud[noeud_source.get_hash()] = None
	noeud_courant = noeud_source
	while(noeud_courant != noeud_arrive):
		if noeud_courant == noeud_arrive:
			break

		if(not noeud_courant in liste_fermee):
			# heuristique = d(source, noeud) + d(arrivée, noeud)
			noeud_courant.cout = grille.distance(noeud_courant, noeud_source) + grille.distance(noeud_courant, noeud_arrive)
			ajouter_noeud_a_liste_ouverte(noeud_courant, liste_ouverte)
			for noeud_voisin in noeud_courant.voisins:
				ajouter_noeud_a_liste_ouverte(noeud_voisin, liste_ouverte)
			# faire même chose pour voisin de noeud coourant
		if len(liste_ouverte) != 0:
			priorite_meilleur_noeud, meilleur_noeud = heappop(liste_ouverte)
			liste_fermee.append(meilleur_noeud)
			print "Liste ouvert : ", liste_ouverte
			print "Liste fermée : ", liste_fermee
			print "Noeud courant : ", noeud_courant
			noeud_precedant = noeud_courant
			noeud_courant = meilleur_noeud
			parent_de_noeud[noeud_courant.get_hash()] = noeud_precedant
		else:
			return False
		dessiner_grille_AEtoile(grille, liste_ouverte, liste_fermee, noeud_source, noeud_arrive)
		raw_input()
	return True

def ajouter_noeud_a_liste_ouverte(noeud_a_ajouter, liste_ouverte):
	dans_liste = False
	noeud_dans_liste = None	
	for priorite,noeud in liste_ouverte:
			if noeud == noeud_a_ajouter:
				noeud_dans_liste = noeud
				dans_liste = True
	if(dans_liste):		
		if(noeud_a_ajouter.cout < noeud_dans_liste.cout):
			liste_ouverte.remove((noeud_dans_liste.cout, noeud_dans_liste))
			heappush(liste_ouverte, (noeud_a_ajouter.cout, noeud_a_ajouter))
	else:
		heappush(liste_ouverte, (noeud_a_ajouter.cout, noeud_a_ajouter))
	return liste_ouverte

def dessiner_grille_AEtoile(grille, liste_ouverte, case_etudiees, source, arrivee):
	compte = 0
	dessin = ""
	case_a_etudier = []

	# on construit la liste des cases étudiées à partir de la liste ouverte
	for priorite, case in liste_ouverte:
		case_a_etudier.append(case)

	for case in grille.cases:
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

		if compte%grille.largeur == grille.largeur-1:
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

	print AEtoile(g, source, arrivee)