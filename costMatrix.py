import math

class CostMatrix:
	def __init__(self, townList):
		self.townDict = dict()
		self.townList = townList
		self.tmpTownList = townList

	def createCostMatrix(self):
		count = 1
		while (count <= len(self.townList)):
			self.townDict[count] = dict()
			count = count + 1
		startingPoint = 1
		count = 0
		while startingPoint <= len(self.townList):
			while count < len(self.townList):
				self.townDict[startingPoint][int(self.townList[count].getTownNumber())] = self.calculateDistanceBetweenPoint(int(self.townList[startingPoint-1].getX()), int(self.townList[startingPoint-1].getY()), int(self.townList[count].getX()), int(self.townList[count].getY()))
				count = count + 1
			count = 0
			startingPoint = startingPoint + 1
		return self.townDict

	def calculateDistanceBetweenPoint(self, x1, y1, x2, y2):
		distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1-y2), 2))
		return distance