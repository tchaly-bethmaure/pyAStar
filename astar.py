#!/usr/bin/env python
# -*- coding: utf-8 -*-
from grille import Grille, Case
from heapq import heappush, heappop
import random

def AEtoile(grille, noeud_source, noeud_arrive):
	parent_de_noeud = {} # dictionnaire noeud parent du noeud
	liste_ouverte = [] # noeuds étudiés
	liste_fermee = [] # noeuds appartiennent potentiellement à la solution

	parent_de_noeud[noeud_source.get_hash()] = None
	noeud_courant = noeud_source
	dessiner_grille_AEtoile(grille, liste_ouverte, liste_fermee, noeud_source, noeud_arrive)
	while(noeud_courant != noeud_arrive):
		if noeud_courant == noeud_arrive:
			break
		if(not noeud_courant in liste_fermee and noeud_courant.cout == 1):	
			noeud_a_considerer = [noeud_courant] + noeud_courant.voisins
			for noeud in noeud_a_considerer:
				ajouter_noeud_a_liste_ouverte(noeud, liste_ouverte, heuristique(grille, noeud, source, arrivee))
			liste_fermee.append(noeud_courant)	
		if len(liste_ouverte) != 0:
			priorite_meilleur_noeud, meilleur_noeud = heappop(liste_ouverte)		
			noeud_precedant = noeud_courant
			noeud_courant = meilleur_noeud
			parent_de_noeud[noeud_courant.get_hash()] = noeud_precedant
		else:
			return False
		dessiner_grille_AEtoile(grille, liste_ouverte, liste_fermee, noeud_source, noeud_arrive)
		raw_input()
	return True

def afficher_liste_ouverte(liste_ouverte):
	print "Liste ouverte : "
	for priorite, case in liste_ouverte:
		print case.cout, case

def afficher_liste_fermee(liste_fermee):
	print "Liste fermée"
	for case in liste_fermee:
		print case

def heuristique(grille, noeud, noeud_source, noeud_arrivee):
	return noeud.cout + grille.distance(noeud, noeud_source) + grille.distance(noeud, noeud_arrivee)

def ajouter_noeud_a_liste_ouverte(noeud_a_ajouter, liste_ouverte, cout_noeud_a_ajouter):
	dans_liste = False
	noeud_dans_liste = None	
	priorite_noeud_dans_liste = None
	for priorite,noeud in liste_ouverte:
			if noeud == noeud_a_ajouter:
				noeud_dans_liste = noeud
				priorite_noeud_dans_liste = priorite
				dans_liste = True
				break
	if(dans_liste):
		if(cout_noeud_a_ajouter < priorite_noeud_dans_liste):
			liste_ouverte.remove((priorite_noeud_dans_liste, noeud_dans_liste))
			heappush(liste_ouverte, (cout_noeud_a_ajouter, noeud_a_ajouter))
	else:
		heappush(liste_ouverte, (cout_noeud_a_ajouter, noeud_a_ajouter))
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
	nb_case = len(g.cases)
	case = source
	while 1==1:
		if case.cout == 1 and case != source:
			arrivee = case
			break
		case = g.cases[random.randint(0, nb_case - 1)]


	print AEtoile(g, source, arrivee)