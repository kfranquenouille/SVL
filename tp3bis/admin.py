class Admin():

	def __init__(self, base):
		self.base = base

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
			longueur = len(login)-1
			login = prenom[0].lower() + login[:longueur]
			if self.base.loginExisteEnBase(login):
				raise CreationLoginAutomatiqueError()

		return login



class NomPrenomVideError(Exception):
	pass



class CreationLoginAutomatiqueError(Exception):
	pass

