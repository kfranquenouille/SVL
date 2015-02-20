import unittest
from mockito import *
from jeu import *


# Scénarios à tester pour la classe Jeu
#	le jeu est terminé car la boîte est fermée
# 	le jeu est terminé en comptabilisant le nombre de points de chaque joueur
#	le joueur lance les dés et ne peut fermer aucun clapets
#	le joueur lance les dés et ferme la boîte	

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

	def test_le_joueur_lance_les_des_et_ne_peut_fermer_aucun_clapet(self):
		pass

	def test_le_joueur_lance_les_des_et_ferme_la_boite(self):
		pass




# Scénarios à tester pour la classe Partie
#	la partie 

class TestPartie(unittest.TestCase):
	pass



# Scénarios à tester pour la classe Joueur
#	le joueur lance un dé
#	le joueur lance deux dés
#	le joueur fait une proposition de clapets à fermer


class TestJoueur(unittest.TestCase):
	
	def setUp(self):
		self.joueur = Joueur()

	def test_lancer_un_de(self):
		resultat = self.joueur.lancer_un_de()

		self.assertTrue(resultat >= 1 and resultat <= 6)


	def test_lancer_deux_des(self):
		resultat = self.joueur.lancer_deux_des()

		self.assertTrue(resultat >= 2 and resultat <= 12)

	def test_le_joueur_fait_une_proposition_de_clapets(self):
		boite = mock()
		lancer = 3
		proposition_attendue = [[1,2],[2,1],[3]]

		proposition = self.joueur.proposer_des_clapets_a_fermer(lancer, boite)

		#self.assertEqual(proposition, proposition_attendue)



	def test_le_joueur_est_bloque(self):
		pass




# Scénarios à tester pour la classe Boite
#	la boite est totalement fermée
#	les clapets de la boîte se ferment correctement


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
