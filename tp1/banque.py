# demo CTD1 SVL 2014-2015

"""
Representation d'un compte bancaire.

On peut creer un compte au solde nul.

>>> compte = Compte()
>>> compte.getSolde()
0.0

On peut crediter un compte, ce qui affecte son solde.

>>> compte.crediter(50.0)
>>> compte.getSolde()
50.0

On ne peut pas crediter negativement un compte.

>>> compte.crediter(-20.0)
Traceback (most recent call last):
...
banque.CreditNegatifOuNulError

>>> compte.crediter(0.0)
Traceback (most recent call last):
...
banque.CreditNegatifOuNulError

>>> compte.debiter(10.0)
>>> compte.getSolde()
40.0

>>> compte.debiter(-10.0)
Traceback (most recent call last):
...
banque.DebitNegatifOuNulError

>>> compte.debiter(0.0)
Traceback (most recent call last):
...
banque.DebitNegatifOuNulError

>>> compte.debiter(60.0)
Traceback (most recent call last):
...
banque.SoldeInsuffisantError
"""

class Compte:

	def __init__(self):
		self.solde = [0.0]

	def getSolde(self):
		sommeOperations = 0.0
		for operation in self.solde:
			sommeOperations += operation
		return sommeOperations

	def crediter(self, somme):
		"""
		Credite le compte de la somme passee en parametre

		>>> compte = Compte()
		>>> compte.crediter(50.0)
		>>> compte.getSolde()
		50.0
		"""
		if somme <= 0.0 :
			raise CreditNegatifOuNulError()
		self.solde.append(somme)

	def debiter(self, somme):
		"""
		Debite le compte de la somme passee en parametre
		
		>>> compte = Compte()
		>>> compte.crediter(50.0)
		>>> compte.debiter(10.0)
		>>> compte.getSolde()
		40.0
		"""
		if somme > self.getSolde():
			raise SoldeInsuffisantError()
		if somme <= 0:
			raise DebitNegatifOuNulError()
		self.solde.append(-somme)

class CreditNegatifOuNulError(Exception):
	pass
		
class DebitNegatifOuNulError(Exception):
	pass

class SoldeInsuffisantError(Exception):
	pass

