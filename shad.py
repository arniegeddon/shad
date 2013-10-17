#!/usr/bin/python2

class character:
	def __init__(self, name):
		self.name = name

	def setname(self):
		self.name = name

	def printname(self):
		print(self.name)

	def setrace(self, race):
		self.race = race

	def printrace(self):
		return self.race
#		print(self.race)


class characterMove:
	pass

mychar = character(raw_input('Enter a name for your character: '))
mychar.setrace(raw_input('Entr your race: '))

print 'Welcome ' 

