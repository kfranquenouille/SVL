# SVL CTD2

"""
Restaurant d'entreprise.

Caisse, Carte.

Fonctionnalites :
 - Visualiser solde d'une carte
 - Visualiser le nb de ticket
 - Payer avec un ticket repas
 - Payer sans ticket repas
 - Inserer une carte
 - Visualiser la valeur des tickets

"""

class Caisse:
 	"""
 	On ne peut Visualiser le solde d'une carte tant que cette derniere n'a pas ete inseree
 	
	>>> caisse = Caisse()
	>>> caisse.solde()
	Traceback (most recent call last):
	...
	restaurant_d_entreprise.AucuneCarteInsereeError

	Une fois la carte inseree on peut Visualiserson solde.

	>>> carte = Carte()
	>>> carte.crediterPorteMonnaie(20.0)
	>>> caisse.inserer_carte(carte)
	>>> caisse.solde()
	20.0
	
	On peut payer un repas sans utiliser de ticket repas, la carte est débitée.

	>>> caisse.payer_repas(15.0)
	>>> carte.soldePorteMonnaie()
	5.0

	Le paiement est refusé si la carte n'est pas solvable.

	>>> caisse.payer_repas(10.0)
	Traceback (most recent call last):
	...
	restaurant_d_entreprise.DebitPorteMonnaieSoldeInsuffisant

	le paiement est impossible si aucune carte n'est inseree

	>>> autreCaisse = Caisse()
	>>> autreCaisse.payer_repas(15.0)
	Traceback (most recent call last):
	...
	restaurant_d_entreprise.AucuneCarteInsereeError

 	"""
 	def __init__(self) :
 		self.carte = None
		
 	def solde(self):
 		"""
		Retourne le solde de la carte
 		"""
 		if self.carte == None :
 			raise AucuneCarteInsereeError()
 		return self.carte.soldePorteMonnaie()

 	def inserer_carte(self, une_carte):
 		self.carte = une_carte

 	def payer_repas(self, montant_repas):
 		if self.carte == None :
 			raise AucuneCarteInsereeError()
 		self.carte.debiterPorteMonnaie(montant_repas)

 	def payer_repas_en_ticket(self, montant_repas):
 		pass

class AucuneCarteInsereeError(Exception):
	pass

class SoldePorteMonnaieInsuffisantError(Exception):
	pass
		
class Carte():
	"""
	Carte personnelle d'un employé.

	la carte peut faire office de porte-monnaie electronique.

	on peut crediter le porte-monnaie.

	>>> carte = Carte()
	>>> carte.crediterPorteMonnaie(20.0)
	>>> carte.soldePorteMonnaie()
	20.0

	On peut debiter le porte-monnaie.

	>>> carte.debiterPorteMonnaie(5.0)
	>>> carte.soldePorteMonnaie()
	15.0

	le debit est impossible si le solde est insuffisant 

	"""
	def __init__(self):
		self.solde_porte_monnaie = 0.0
		self.valeur_ticket = None
		self.solde_ticket = 0

	def soldePorteMonnaie(self):
		return self.solde_porte_monnaie
	
	def crediterPorteMonnaie(self, montant_credit):
		"""
		On souhaite crediter le porte-monnaie
		On ne peut créditer la carte d'un montant négatif ou nul

		>>> carte = Carte()
		>>> carte.crediterPorteMonnaie(20.0)
		>>> carte.soldePorteMonnaie()
		20.0
		>>> carte.crediterPorteMonnaie(0.0)
		Traceback (most recent call last):
		...
		restaurant_d_entreprise.CreditPorteMonnaieMontantNegatifOuNul

		>>> carte.crediterPorteMonnaie(-10.0)
		Traceback (most recent call last):
		...
		restaurant_d_entreprise.CreditPorteMonnaieMontantNegatifOuNul

		>>> carte.soldePorteMonnaie()
		20.0
		"""
		if montant_credit <= 0.0:
			raise CreditPorteMonnaieMontantNegatifOuNul()
		self.solde_porte_monnaie += montant_credit

	def debiterPorteMonnaie(self, montant_debit):
		"""
		On souhaite debiter le porte-monnaie
		On ne peut debiter la carte d'un montant négatif ou nul
		On ne peut debiter la carte d'un montant supérieur au solde (porte-monnaie) de la carte

		>>> carte = Carte()
		>>> carte.crediterPorteMonnaie(20.0)
		>>> carte.soldePorteMonnaie()
		20.0
		>>> carte.debiterPorteMonnaie(15.0)
		>>> carte.soldePorteMonnaie()
		5.0
		>>> carte.debiterPorteMonnaie(15.0)
		Traceback (most recent call last):
		...
		restaurant_d_entreprise.DebitPorteMonnaieSoldeInsuffisant

		>>> carte.debiterPorteMonnaie(-10.0)
		Traceback (most recent call last):
		...
		restaurant_d_entreprise.DebitPorteMonnaieMontantNegatifOuNul

		>>> carte.debiterPorteMonnaie(0.0)
		Traceback (most recent call last):
		...
		restaurant_d_entreprise.DebitPorteMonnaieMontantNegatifOuNul

		>>> carte.soldePorteMonnaie()
		5.0
		"""
		if montant_debit <= 0.0:
			raise DebitPorteMonnaieMontantNegatifOuNul()
		if montant_debit > self.solde_porte_monnaie:
			raise DebitPorteMonnaieSoldeInsuffisant()
		self.solde_porte_monnaie -= montant_debit


	def definirValeurTicket(self, une_valeur):
		self.valeur_ticket = une_valeur

	def soldeTicket(self):
		return self.solde_ticket

	def valeurTicket(self):
		return self.valeur_ticket

	def crediterTicket(self, tickets_a_crediter):
		if tickets_a_crediter <= 0:
			raise CreditTicketMontantNegatifOuNul()
		self.solde_ticket += tickets_a_crediter

	def debiterTicket(self, tickets_a_debiter):
		pass

class CreditPorteMonnaieMontantNegatifOuNul(Exception):
	pass

class DebitPorteMonnaieMontantNegatifOuNul(Exception):
	pass

class DebitPorteMonnaieSoldeInsuffisant(Exception):
	pass

class CreditTicketMontantNegatifOuNul(Exception):
	pass