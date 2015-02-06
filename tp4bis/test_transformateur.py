import unittest
from mockito import *
from io import StringIO 
from transformateur import *

class TestTransformerLog():

	def setUp(self):
		lecteur = mock()
		transformateur = Transformateur()

	def test_lire_message_d_une_log_correcte(self):
		log = StringIO("2010-02-25, 5, error in database\n")

		self.assertEqual(self.transformateur.getMessage(log), "error in database")


	def test_lire_message_d_une_log_incorrecte(self):
		log = StringIO("2010-02-25\n")

		self.assertRaises(FormatLogIncorrectError,
						self.transformateur.getMessage(),
						log)



	def test_transformer_log_correcte_avec_prio_superieure_a_5(self):
		log = StringIO("2010-02-25, 5, error in database\n")
		
		when(self.lecteur).lire().thenReturn(log)

		self.assertEqual(self.transformateur.transformer(log), log);
	


	def test_transformer_log_correcte_avec_prio_inferieure_a_5(self):
		log = StringIO("2010-02-26, 2, error\n")
		
		when(self.lecteur).lire().thenReturn(log)

		self.assertEqual(self.transformateur.transformer(log), "");
		


	def test_transformer_log_incorrecte(self):
		log = StringIO("2010-02-26\n")
		
		when(self.lecteur).lire().thenReturn(log)

		self.assertRaises(FormatLogIncorrectError,
						self.transformateur.transformer(), 
						log);

