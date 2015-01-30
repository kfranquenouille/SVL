# SVL 30/01/15
# ex emprunts des livres

"""
Service des emprunts de la bibliothèque

Comportements a tester :
- cas nominal
- cas d'exception : le membre a atteint son quota
- cas d'exception : le livre n'est que consultable
"""
class ServiceEmprunt():
	
	def __init__(self, lesemprunts):
		self.emprunts = lesemprunts

	def emprunter(self, livre, carte):
		if not livre.est_empruntable():
			raise LivreNonEmpruntableError()
		self.emprunts.ajouterEmprunt(livre, carte)

class LivreNonEmpruntableError(Exception):
	print("Le livre n'est pas empruntable")
	