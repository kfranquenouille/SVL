# SVL CTD2

import unittest
from mockito import *
from restaurant_d_entreprise import *

class TestVisualiserSoldeCarte(unittest.TestCase):
	"""docstring for TestVisualiserSoldeCarte"""
	def test_visualiser_le_solde_est_impossible_avant_insertion_de_carte(self):
		caisse = Caisse()
		self.assertRaises(AucuneCarteInsereeError, caisse.solde)
		
	def test_le_solde_de_la_caisse_est_celui_de_la_carte(self):
		caisse = Caisse()
		# carte = MockCarte() # mock a la mano
		carte = mock()
		when(carte).soldePorteMonnaie().thenReturn(20.0) # stubbing
		caisse.inserer_carte(carte)
		self.assertEqual(caisse.solde(), 20.0)


class TestPayerUnRepasSansTicketRepas(unittest.TestCase):
	def test_payer_un_repas_debite_la_carte(self):
		caisse = Caisse()
		carte = mock()
		
		montant_repas = 15.0
		
		caisse.inserer_carte(carte)
		caisse.payer_repas(montant_repas)

		verify(carte).debiterPorteMonnaie(montant_repas)
		# assertEqual(carte.solde(), 5.0) # A NE JAMAIS FAIRE, on verifie que mockito fait son taff

	def test_impossible_de_payer_un_repas_si_carte_insolvable(self):
		caisse = Caisse()
		carte = mock()

		montant_repas = 15.0
		when(carte).debiterPorteMonnaie(montant_repas).thenRaise(SoldePorteMonnaieInsuffisantError())

		caisse.inserer_carte(carte)
		self.assertRaises(SoldePorteMonnaieInsuffisantError, caisse.payer_repas, montant_repas)
		verify(carte).debiterPorteMonnaie(montant_repas)
		
class TestPayerUnRepasAvecTicketRepas(unittest.TestCase):

	def test_payer_un_repas_en_ticket_et_porte_monnaie(self):
		caisse = Caisse()
		carte = mock()
		montant_repas = 18.5
		valeur_ticket = 8.5

		caisse.inserer_carte(carte)
		caisse.payer_repas_en_ticket(montant_repas)

		#verify(carte).debiterTicket(1)
		#verify(carte).debiterPorteMonnaie(montant_repas - valeur_ticket)