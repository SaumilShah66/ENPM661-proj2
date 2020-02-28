import numpy as np 
from obstacle import Obstructions

obs = Obstructions(200,100)
obs.showMap()

class PathFinder():
	def __init__(self, start, end):
		self.allNodes = []
		self.mainData = []

	def actionSet(self):
		self.actionset = [[],
						  [],
						  [],
						  [],
						  [],
						  [],
						  [],
						  []]