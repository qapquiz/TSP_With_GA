import math

class salesMan():
	def __init__(self, numberOfPopulation):
		#this is fitness
		self.sumDistance = 0 
		
	def calculateDistanceBetweenPoint(self, x1, y1, x2, y2):
		distance = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1-y2), 2))
		return distance