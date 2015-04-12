#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Grille:
	type_voisinge = {
		"von_neumann":[(0,1),(0,-1),(1,0),(-1,0)],
		"moore":[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
	}

	def __init__(self, size_x, size_y, t_voisinage):
		self.cases=[]

		# générer les cases de la grille
		for x in range(0, size_x):
			for y in range(0, size_y):
				self.cases.append(Case(x,y,1))

		# voisinages de chaque case
		coord__cases_voisinnes = Grille.type_voisinge[t_voisinage]
		for case in self.cases:
			for x,y in coord__cases_voisinnes:
				if(not case.coord_x + x < 0 
				and not case.coord_x + x > size_x 
				and not case.coord_y + y < 0
				and not case.coord_y + y > size_y):
					voisin = Case(case.coord_x+x,case.coord_y+y,1)
					case.voisins.append(voisin)

	def distance(self, case_a,case_b):
		return abs(case_b.coord_x - case_a.coord_x) + abs(case_b.coord_y + case_a.coord_y)

	def __str__(self):
		string = ""
		for case in self.cases:
			string += ", "+str(case)
		return string

class Case:
	def __init__(self,x,y,cout):
		self.coord_x=x
		self.coord_y=y
		self.cout=cout
		self.voisins=[]

	def __eq__(self,autre):
		if(self.coord_x == autre.coord_x
			and self.coord_y == autre.coord_y
			and self.cout == autre.cout):
			return True
		else:
			return False

	def __str__(self):
		return "("+str(self.coord_x)+", "+str(self.coord_y)+")"

if __name__ == '__main__':
	A = Case(0,1,5)
	B = Case(0,0,5)
	Aprim = Case(0,1,1)

	# test objet case
	print "A == A ? " + str(A == A)
	print "A == B ? " + str(A == B)
	print "A == A' ? " + str(A == Aprim)

	# test objet grille
	## voisinage d'une case
	g = Grille(5,5,"von_neumann")
	print g.cases[3]
	for c in g.cases[3].voisins:
		print c
	## distance
	A = g.cases[15]
	print "A : " + str(A)
	B = g.cases[21]
	print "B : " + str(B)
	print g.distance(A,B)