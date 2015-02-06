# SVL CTD4

import unittest
from mockito import *
from deviner_un_nombre import *

# cas nominaux
#  - trouver le secret en moins de 5 coups
#  - le joueur ne trouve pas la réponse
# cas d'exception
#  - entrée du joueur incorrecte

class TestJeu(unittest.TestCase):
	
	def test_le_joueur_gagne_en_un_coup(self):
		A_DEVINER = 5

		generateur = mock()
		when(generateur).alea().thenReturn(A_DEVINER)

		lecteur = mock()
		when(lecteur).lire().thenReturn(A_DEVINER)

		afficheur = mock()

		jeu = Jeu(generateur, lecteur, afficheur)

		jeu.jouer()

		verify(afficheur).affiche_invite()
		verify(afficheur).affiche_gagne()
		verify(lecteur).lire()
		
	def test_le_joueur_gagne_en_3_coups(self):
		A_DEVINER = 5
		TROP_GRAND = 6
		TROP_PETIT = 4

		generateur = mock()
		when(generateur).alea().thenReturn(A_DEVINER)

		lecteur = mock()
		when(lecteur).lire().thenReturn(TROP_GRAND).thenReturn(TROP_PETIT).thenReturn(A_DEVINER)

		afficheur = mock()

		jeu = Jeu(generateur, lecteur, afficheur)

		jeu.jouer()

		verify(lecteur, times = 3).lire()
		inorder.verify(afficheur, times = 3).affiche_invite()
		inorder.verify(afficheur).affiche_trop_grand()
		inorder.verify(afficheur, times = 3).affiche_invite()
		inorder.verify(afficheur).affiche_trop_petit()
		inorder.verify(afficheur, times = 3).affiche_invite()
		inorder.verify(afficheur).affiche_gagne()

	def test_le_joueur_perd(self):
		A_DEVINER = 3
		TROP_GRAND = 5

		generateur = mock()
		when(generateur).alea().thenReturn(A_DEVINER)

		lecteur = mock()
		when(lecteur).lire().thenReturn(TROP_GRAND)

		afficheur = mock()

		jeu = Jeu(generateur, lecteur, afficheur)

		jeu.jouer()

		verify(afficheur, times=5).affiche_trop_grand()
		verify(afficheur).affiche_perd()

	#def test_le_joueur_gagne_en_exacement_5_tentatives(self):

from io import StringIO 

class TestLecteur(unittest.TestCase):

	def test_lecture_entree_correcte(self):
		flot_entree = StringIO("5\n")
		lecteur = Lecteur(flot_entree)
		self.assertEqual(lecteur.lire(), 5)