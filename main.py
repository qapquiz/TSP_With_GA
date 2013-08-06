from Town import Town
from costMatrix import CostMatrix
from salesMan import SalesMan
#import matplotlib.pyplot as plt

#initial variable for Genetic Algorithm
MAX_ITERATION = 1000
MAX_POPULATION = 20
PC = 0.7
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

#crossover population

#mutation population

#get rid of chromosome has lower fitness than the other

#end iteration

#return Answer