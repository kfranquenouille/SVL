import unittest
from mockito import *
from jeu import *


class TestJeu(unittest.TestCase):

	def setUp(self):
		self.j1 = mock()
		self.j2 = mock()
		self.boite = mock()

		self.jeu = Jeu(self.boite, self.j1, self.j2)


	def test_jeu_est_termine_par_clapets(self):
		when(self.boite).est_totalement_fermee().thenReturn(True)

		self.assertTrue(self.jeu.est_termine())


	def test_jeu_est_non_termine_par_clapets(self):
		when(self.boite).est_totalement_fermee().thenReturn(False)

		self.assertFalse(self.jeu.est_termine())





class TestJoueur(unittest.TestCase):
	
	def test_lancer_un_de(self):
		joueur = Joueur()
		resultat = joueur.lancer_un_de()

		self.assertTrue(resultat >= 1 and resultat <= 6)


	def test_lancer_deux_des(self):
		joueur = Joueur()
		resultat = joueur.lancer_deux_des()

		self.assertTrue(resultat >= 2 and resultat <= 12)





class TestBoite(unittest.TestCase):

	def setUp(self):
		self.boite = Boite()


	def test_clapet_se_ferme_correctement(self):
		numero_clapet = 5
		self.boite.fermer_clapet(numero_clapet)
		self.assertEqual(self.boite.clapet_est_ferme(numero_clapet), 0)


	def test_boite_est_totalement_fermee(self):
		for num_clapet in range(9):
			self.boite.fermer_clapet(num_clapet)

		self.assertTrue(self.boite.est_totalement_fermee())
