class Admin():

	def __init__(self):
		self.base = Base()

	"""
	Un nom et un prénom doivent contenir au minimum une lettre.
	"""
	def calculerLogin(self, nom, prenom):
		login = ""

		if len(prenom)<1 or len(nom)<1:
			raise NomPrenomVideError()

		if len(nom) <= 8:
			login = nom.lower()
		else:
			login = nom[:8].lower()

		if self.base.loginExisteEnBase(login):
			login = prenom[1] + login[:len(login)-1]
			if self.base.loginExisteEnBase(login):
				raise CreationLoginAutomatiqueError()

		return login



class NomPrenomVideError(Exception):
	pass



class CreationLoginAutomatiqueError(Exception):
	pass




class Base():

	def __init__(self):
		self.listeLogins = []

	def loginExisteEnBase(self, login):
		pass

	def insererLogin(self, login):
		pass

	def supprimerLogin(self,login):
		pass