from random import *


class Jeu:
	def __init__(self, boite, joueur1, joueur2):
		self.boite = boite
		self.joueur1 = joueur1
		self.joueur2 = joueur2
		self.score1 = 0
		self.score2 = 0

	def est_termine(self):
		return self.boite.est_totalement_fermee()

	def jouer_un_tour(self):
		pass




class Joueur:
	def __init__(self):
		pass

	def lancer_un_de(self):
		return randint(1,6)

	def lancer_deux_des(self):
		return self.lancer_un_de() + self.lancer_un_de()



class Boite:
	def __init__(self):
		self.clapets = [1,1,1,1,1,1,1,1,1]

	def fermer_clapet(self, numero):
		self.clapets[numero-1] = 0

	def clapet_est_ferme(self, numero):
		return self.clapets[numero-1]

	def est_totalement_fermee(self):
		for clap in self.clapets:
			if clap == 1:
				return 0
		return 1


