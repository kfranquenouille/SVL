import unittest
from mockito import *

class TesterUnEmprunt(unittest.TestCase):

    def tester_cas_nominal_enprunt_reussi(self):
        stockageEmprunt = mock()

        service = ServiceEmprunt(stockageEmprunt)
        service.emprunter(livre, carte)

        verify(stockageEmprunt).ajouterEmprunt(livre, carte)


