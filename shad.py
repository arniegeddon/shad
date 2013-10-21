#!/usr/bin/python
# _*_ coding: utf-8 -*-

import sqlite3
import sys
import re
import curses

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

def curseRaceMenu():
x = 0
while x != ord(str(listRace[-1])):
	screen = curses.initscr()
	screen.clear()
	screen.border(0)
	screen.addstr(2,2, "Please choose a race..")
	screen.addstr(4,4,  listRace[1])
	screen.addstr(5,4,  listRace[2])
	screen.addstr(6,4,  listRace[3])
	screen.addstr(7,4,  listRace[4])
	screen.refresh()

	curses.endwin()


listRace = [ ]
listRace= ['EmptyRace', 'Human', 'Elf', 'Dwarf', 'Mutant']

"""
# mychar = character(input('Enter a name for your character: '))
# mychar.setrace(input('Enter your race: '))

print('Welcome ' + mychar.printname() + ' the ' + mychar.printrace() + '.....')
print('....welcome to the Evil Wood')
print()
showChapter(1)
print()
"""


con.close()
