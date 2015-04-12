#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Graph:
	def __init__(self):
		self.noeuds=[]
		self.arretes=[]		

class Noeud:
	def __init__(self, intitule):
		self.intitule=intitule
		self.voisins=[]
		
	def __eq__(self, other):
		return self.intitule == other.intitule

class Arrete:
	def __init__(self,noeud_a,noeud_b,cout):
		self.premier_noeud=noeud_a
		self.second_noeud=noeud_b
		self.cout=cout

	def __eq__(self, other):
		if(self.premier_noeud == other.premier_noeud 
			and self.second_noeud == other.second_noeud
			and self.cout == other.cout):
			return True
		elif(self.premier_noeud == other.second_noeud 
			and self.second_noeud == other.premier_noeud
			and self.cout == other.cout):
			return True
		else:
			return False

if __name__ == '__main__':
	A = Noeud("A")
	B = Noeud("B")
	AB5 = Arrete(A,B,5)
	BA5 = Arrete(B,A,5)
	AB4 = Arrete(A,B,4)
	print "Noeuds :"
	print "A == A ? "+ str(A==A)
	print "A == B ? "+ str(A==B)
	print "Arrêtes : "
	print "AB5 == AB5 ? "+str(AB5 == AB5)
	print "AB5 == BA5 ? "+str(AB5 == BA5)
	print "AB5 == AB4 ? "+str(AB5 == AB4)

