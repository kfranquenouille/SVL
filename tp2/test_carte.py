import unittest
from mockito import *
from restaurant_d_entreprise import *

class TestVisualiserSoldePorteMonnaieCarte(unittest.TestCase) :
	"""
	On teste ici le solde de la carte

	>>> carte = Carte()
	>>> carte.soldePorteMonnaie()
	0.0

	"""

	def test_afficher_solde_initial(self):
		carte = Carte()

		self.assertEqual(carte.soldePorteMonnaie(), 0.0)


class TestCrediterSoldePorteMonnaieCarte(unittest.TestCase):
	"""
	On teste le crédit en monnaie de la carte

	>>> carte = Carte()
	>>> carte.soldePorteMonnaie()
	0.0
	>>> carte.crediterPorteMonnaie(20.0)
	>>> carte.soldePorteMonnaie()
	20.0

	"""
	def setUp(self):
		self.carte = Carte()

	def test_crediter_porte_monnaie_avec_un_montant_positif(self):
		self.carte.crediterPorteMonnaie(20.0)

		self.assertEqual(self.carte.soldePorteMonnaie(), 20.0)

	def test_crediter_porte_monnaie_avec_un_montant_nul(self):
		self.assertRaises(CreditPorteMonnaieMontantNegatifOuNul,
							self.carte.crediterPorteMonnaie, 
							0.0)

	def test_crediter_porte_monnaie_avec_un_montant_negatif(self):
		self.assertRaises(CreditPorteMonnaieMontantNegatifOuNul,
							self.carte.crediterPorteMonnaie, 
							-10.0)
		

class TestDebiterSoldePorteMonnaieCarte(unittest.TestCase):
	"""
	On teste le debit en monnaie de la carte 

	>>> carte = Carte()
	>>> carte.soldePorteMonnaie()
	0.0
	>>> carte.crediterPorteMonnaie(20.0)
	>>> carte.debiterPorteMonnaie(15.0)
	>>> carte.soldePorteMonnaie()
	5.0

	"""
	def setUp(self):
		self.carte = Carte()
		self.carte.crediterPorteMonnaie(20.0)

	def test_debiter_porte_monnaie_avec_un_montant_positif(self):
		self.carte.debiterPorteMonnaie(15.0)
		self.assertEqual(self.carte.soldePorteMonnaie(), 5.0)

	def test_debiter_porte_monnaie_avec_un_montant_nul(self):
		self.assertRaises(DebitPorteMonnaieMontantNegatifOuNul, 
							self.carte.debiterPorteMonnaie,
							0.0)

	def test_debiter_porte_monnaie_avec_un_montant_negatif(self):
		self.assertRaises(DebitPorteMonnaieMontantNegatifOuNul, 
							self.carte.debiterPorteMonnaie,
							-10.0)

	def test_debiter_porte_monnaie_avec_un_solde_insuffisant(self):
		self.assertRaises(DebitPorteMonnaieSoldeInsuffisant,
							self.carte.debiterPorteMonnaie,
							25.0)


class TestVisualiserSoldeTicketCarte(unittest.TestCase) :
	"""
	On teste ici le solde en ticket de la carte

	>>> carte = Carte()
	>>> carte.soldeTicket()
	0
	"""

	def setUp(self):
		self.carte = Carte()

	def test_afficher_solde_ticket_initial(self):
		self.assertEqual(self.carte.soldeTicket(), 0)

	def test_afficher_valeur_ticket(self):
		self.assertEqual(self.carte.valeurTicket(), None)
		self.carte.definirValeurTicket(8.5)
		self.assertEqual(self.carte.valeurTicket(), 8.5)


class TestCreditSoldeTicketCarte(unittest.TestCase):
	"""
	On teste le crédit en ticket de la carte

	>>> carte = Carte()
	>>> carte.definirValeurTicket(8.5)
	>>> carte.crediterTicket(2)
	>>> carte.soldeTicket()
	2
	"""

	def setUp(self):
		self.carte = Carte()
		self.carte.definirValeurTicket(8.5)

	def test_crediter_carte_avec_un_nombre_positif_de_tickets(self):
		self.carte.crediterTicket(5)
		self.assertEqual(self.carte.soldeTicket(), 5)

	def test_crediter_carte_avec_un_nombre_nul_de_tickets(self):
		self.assertRaises(CreditTicketMontantNegatifOuNul,
							self.carte.crediterTicket,
							0)

	def test_crediter_carte_avec_un_nombre_negatif_de_tickets(self):
		self.assertRaises(CreditTicketMontantNegatifOuNul,
							self.carte.crediterTicket,
							-5)