import math
import random

class SalesMan():
	def __init__(self):
		#this is fitness
		self.sumDistanceFitness = 0 
		self.path = list()
		
	def randomFirstPath(self, townList):
		usedToGo = list()
		while (len(self.path) != len(townList)):
			nextTown = random.randint(1, 200)
			if nextTown not in usedToGo:
				self.path.append(nextTown)

	def randomStartingPoint(self):
		startingPoint = random.randint(1, 200)
		self.startingPoint = startingPoint

	def calculateDistanceBetweenPoint(self, x1, y1, x2, y2):
		distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1-y2), 2))
		return distance

	def getPath(self):
		return self.path

	def calculateFitness(self, costMatrixDict, townList):
		pathIndex = 0
		while pathIndex <= len(townList) - 2:
			self.sumDistanceFitness = self.sumDistanceFitness + costMatrixDict[int(self.path[pathIndex])][int(self.path[pathIndex+1])]
			pathIndex = pathIndex + 1

	def getFitness(self):
		return self.sumDistanceFitness