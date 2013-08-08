from Town import Town
from costMatrix import CostMatrix
from salesMan import SalesMan
import random
#import matplotlib.pyplot as plt

#initial variable for Genetic Algorithm
MAX_ITERATION = 1000
MAX_POPULATION = 20
PC = 0.8
PM = 0.05

#create list of object town
townList = list()
townData = open("town.txt", 'r')
while townData:
	line = townData.readline().split()
	if (line == []):
		break;
	townList.append(Town(line[0], line[1], line[2]))

#createCostMatrix
costMatrixDict = CostMatrix(townList).createCostMatrix()

#create population
populationList = list()
for i in range(20):
	populationList.append(SalesMan())
	populationList[i].randomFirstPath(townList)
	populationList[i].calculateFitness(costMatrixDict, townList)

#start iteration
iteration = 1
while iteration <= MAX_ITERATION:
	#roulette selection
	#sort populationList
	populationList = sorted(populationList, key=lambda population: population.fitness)
	#end sort populationList
	sumFitness = 0
	for population in populationList:
		sumFitness = sumFitness + population.getFitness()
	probability = 0
	sumProbabilities = 0
	for population in populationList:
		population.setProbability(sumProbabilities + ((float(population.getFitness()) / float(sumFitness))))
		sumProbabilities += population.getProbability() - sumProbabilities
		population.setProbability(1 - population.getProbability())
		#print "fitness: " + str(population.getFitness())
		#print "prob: " + str(population.getProbability())
	#selection phase
	populationList = populationList[::-1]
	populationIndex = 0
	populationIndexSelectionList = list()
	#/2
	while (len(populationIndexSelectionList) != MAX_POPULATION):
		randNumber = random.uniform(0, 1)
		for population in populationList:
			if randNumber < population.getProbability():
				populationIndexSelectionList.append(populationIndex)
				break
				#if populationIndex not in populationIndexSelectionList:
				#	populationIndexSelectionList.append(populationIndex)
				#	break
			populationIndex = populationIndex + 1
		populationIndex = 0
	populationSelectionList = list()
	#/2
	for i in range(MAX_POPULATION):
		populationSelectionList.append(populationList[populationIndexSelectionList[i]])
	#print "SelectionList: " + str(populationIndexSelectionList)
	#end selection phase
	#crossover phase
	crossoverCount = 0
	while crossoverCount < (MAX_POPULATION):
		parent1 = populationSelectionList[crossoverCount]
		parent2 = populationSelectionList[crossoverCount+1]
		#occur crossover
		if random.uniform(0, 1) < PC:
			child1 = SalesMan()
			child2 = SalesMan()
			#child1
			child1.setPath(parent1.getPath()[:100])
			while len(child1.getPath()) != len(townList):
				parent2Path = parent2.getPath()
				for town in parent2Path:
					if town not in child1.getPath():
						child1.getPath().append(town)
			#child2
			child2.setPath(parent2.getPath()[:100])
			while len(child2.getPath()) != len(townList):
				parent1Path = parent1.getPath()
				for town in parent1Path:
					if town not in child2.getPath():
						child2.getPath().append(town)
			populationList.append(child1)
			populationList.append(child2)
		#not occur crossover then copy parent to child
		else:
			child1 = SalesMan()
			child2 = SalesMan()
			child1.setPath(parent1.getPath())
			child1.setFitness(parent1.getFitness())
			child2.setPath(parent2.getPath())
			child2.setFitness(parent2.getFitness())
			populationList.append(child1)
			populationList.append(child2)
		crossoverCount = crossoverCount + 2
	#print "========================================================================="
	#print child1.getPath()
	child1.calculateFitness(costMatrixDict, townList)
	#print child1.getFitness()
 	#end crossover phase
	#end roulette selection
	#print "len of populationList: " + str(len(populationList))
	calculateFitnessCount = 20
	while calculateFitnessCount < len(populationList):
		populationList[calculateFitnessCount].calculateFitness(costMatrixDict, townList)
		calculateFitnessCount = calculateFitnessCount + 1
	mutationIndex = 0
	for population in populationList:
		if mutationIndex >= 20:
			pathIndex = 0
			pathIndexList = list()
			for path in population.getPath():
				if random.uniform(0, 1) < PM:
					pathIndexList.append(pathIndex)
					if len(pathIndexList) == 2:
						temp = population.getPath()[pathIndexList[0]]
						population.getPath()[pathIndexList[0]] = population.getPath()[pathIndexList[1]]
						population.getPath()[pathIndexList[1]] = temp
						pathIndexList = list()
				pathIndex = pathIndex + 1
		mutationIndex = mutationIndex + 1
	#sort populationList
	populationList = sorted(populationList, key=lambda population: population.fitness)
	#end sort populationList
	#for population in populationList:
	#	print population.getFitness()
	delIndex = 20
	while delIndex < len(populationList):
		del populationList[delIndex]
	iteration = iteration + 1 
#end iteration
print populationList[0].getPath()
print "Total distance: " + str(populationList[0].getFitness())

#return Answer