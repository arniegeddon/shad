#!/usr/bin/python
# _*_ coding: utf-8 -*-

import sqlite3
import sys
import re

try:
	con = sqlite3.connect('shad.db')
	cur = con.cursor()

except sqlite3.Error as e:
	print ("Error %s:" % e.args[0])
	sys.exit(1)

def showChapter(chapter):
	cur.execute('SELECT desc FROM areaDescription WHERE ID = %d' % chapter)
	chaptext = str(cur.fetchone())
	print (chaptext)

class character:
	def __init__(self, name):
		self.name = name

	def setname(self):
		self.name = name

	def printname(self):
		return str(self.name)

	def setrace(self, race):
		self.race = race

	def printrace(self):
		return str(self.race)

mychar = character(input('Enter a name for your character: '))
mychar.setrace(input('Enter your race: ')) 

print('Welcome ' + mychar.printname() + ' the ' + mychar.printrace() + '.....')
print('....welcome to the Evil Wood')
print()
showChapter(1)
print()


con.close()
