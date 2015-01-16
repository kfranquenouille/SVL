import unittest
from banque import Compte
from banque import CreditNegatifOuNulError
from banque import DebitNegatifOuNulError
from banque import SoldeInsuffisantError

class TestCreationCompte(unittest.TestCase):

	def test_un_compte_est_cree_avec_un_solde_nul(self):
		compte = Compte()
		self.assertEqual(compte.getSolde(), 0.0)

class TestUnCompteEstCredite(unittest.TestCase):
	
	def setUp(self):
		self.compte = Compte()

	def test_crediter_un_compte_affecte_son_solde(self):
		self.compte.crediter(50.0)
		self.assertEqual(self.compte.getSolde(), 50.0)

	def test_on_ne_peut_pas_crediter_un_montant_negatif(self):
		# Une maniere de faire
		# self.assertRaises(compte.crediter, -20.0, CreditNegatifError)
		
		try :
			self.compte.crediter(-20.0)
			self.fail("crediter doit lever une exception CreditNegatifError")
		except CreditNegatifOuNulError :
			pass

	def test_crediter_avec_montant_nul(self):
		# Renvoie une exception avec crediter(0.0)
		self.assertRaises(CreditNegatifOuNulError, self.compte.crediter, 0.0)

class TestUnCompteEstDebite(unittest.TestCase):

	def setUp(self):
		self.compte = Compte()

	def test_un_compte_est_debite(self):
		self.compte.crediter(50.0)
		self.compte.debiter(10.0)
		self.assertEqual(self.compte.getSolde(), 40.0)

	def test_un_compte_estdebite_avec_montant_negatif(self):
		self.assertRaises(DebitNegatifOuNulError, self.compte.debiter, -10.0)

	def test_un_compte_est_debite_avec_montant_nul(self):
		self.assertRaises(DebitNegatifOuNulError, self.compte.debiter, 0.0)		

	def test_un_compte_a_solde_insuffisant_pour_debit(self):
		self.assertRaises(SoldeInsuffisantError, self.compte.debiter, 60.0)
