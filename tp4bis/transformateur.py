class Transformateur:
	"""
	permet de tranformer un log et de le filtrer


	"""
	def __init__(self):
		pass

	def getMessage(self, log):
		pass

	def transformer(self, lecteur):
		pass

	def filtrer(self, log):
		pass



class Lecteur:
	"""
	Classe qui definit un lecteur. 
	La fonction lire, lit une ligne et retourne un objet Log.
	"""
	def __init__(self, flot_entree):
		self.flot = flot_entree

	def lire(self):
		ligne = self.flot.readline()
		mots = ligne.split(",")
		if len(mots) < 3:
			raise FormatLogIncorrectError()
		else
			return Log(mots[0], mots[1], mots[2])


class Log:
	"""
	Classe definissant une log qui est composee de :
		- une date
		- une priorite
		- un message
	"""
	def __init__(self, date, prio, msg)
		self.date = date
		self.priorite = prio
		self.message = msg


class FormatLogIncorrectError(Exception):
	pass