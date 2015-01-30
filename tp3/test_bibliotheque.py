import unittest
from mockito import *
from bibliotheque import *

class TesterUnEmprunt(unittest.TestCase):

	def setUp(self):
		self.stockageEmprunt = mock()
		self.livre = mock()
		self.carte = mock()
		self.service = ServiceEmprunt(self.stockageEmprunt)

	def tester_cas_nominal_enprunt_reussi(self):
		when(self.livre).est_empruntable().thenReturn(True)

		# emprunt = mock()
		# when (stockageEmprunt).ajouterEmprunt(livre, carte).thenReturn(emprunt)

		resultat = self.service.emprunter(self.livre, self.carte)

		verify(self.stockageEmprunt).ajouterEmprunt(self.livre, self.carte)

        # assert_equal(resultat, emprunt)


	def tester_emprunt_echoue_car_livre_non_empruntable(self):
		when(self.livre).est_empruntable().thenReturn(False)

		self.assertRaises(LivreNonEmpruntableError, self.service.emprunter, self.livre, self.carte)
