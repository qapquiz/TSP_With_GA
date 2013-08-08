import math
import random

class SalesMan():
	def __init__(self):
		#this is fitness
		self.fitness = 0 
		self.path = list()
		self.probability = 0
		
	def randomFirstPath(self, townList):
		usedToGo = list()
		while (len(self.path) != len(townList)):
			nextTown = random.randint(1, 200)
			if nextTown not in usedToGo:
				self.path.append(nextTown)
				usedToGo.append(nextTown)

	def randomStartingPoint(self):
		startingPoint = random.randint(1, 200)
		self.startingPoint = startingPoint

	def calculateDistanceBetweenPoint(self, x1, y1, x2, y2):
		distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1-y2), 2))
		return distance

	def setPath(self, path):
		self.path = path

	def getPath(self):
		return self.path

	def calculateFitness(self, costMatrixDict, townList):
		pathIndex = 0
		while pathIndex <= len(townList) - 2:
			self.fitness = self.fitness + costMatrixDict[int(self.path[pathIndex])][int(self.path[pathIndex+1])]
			pathIndex = pathIndex + 1

	def setFitness(self, fitness):
		self.fitness = fitness

	def getFitness(self):
		return self.fitness

	def getProbability(self): 
		return self.probability

	def setProbability(self, probability):
		self.probability = probability
