import unittest
from mockito import *
from admin import *

class TestCalculerLogin(unittest.TestCase):
	
	def setUp(self):
		self.admin = Admin()
		self.base = mock()



	def test_cas_nominal_calcul_login_reussi(self):
		"""
		Le calcul du login est OK avec les lettres du nom.
		"""
		self.assertEqual(self.admin.calculerLogin("Dess", "Pauline"), "dess")
		


	def test_calcul_login_avec_nom_trop_long(self):
		"""
		Le calcul du login est OK avec le nom tronqué à 8.
		"""
		self.assertEqual(self.admin.calculerLogin("Franquenouille", "Kevin"), "franquen")



	def test_calcul_login_existant_premiere_tentative(self):
		"""
		Le login composé des 8 premières lettres du nom existe déjà.
		On fait une autre tentative avec les 7 premières lettres du nom et l'initiale du prénom.
		"""
		loginExistant = "franquen"
		loginOK = "kfranque"
		when(self.base).loginExisteEnBase(loginExistant).thenReturn(True)
		when(self.base).loginExisteEnBase(loginOK).thenReturn(False)

		self.assertEqual(self.admin.calculerLogin("Franquenouille","Kevin"), loginOK)



	def test_calcul_login_echoue_deuxieme_tentative(self):
		"""
		Le login composé des 7 premières lettres du nom et l'initiale du prénom existe déjà.
		Le calcul renvoie alors une exception.
		"""
		
