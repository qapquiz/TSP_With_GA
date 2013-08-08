import random
class population:
    def __init__(self):
        self.sumDistance = 0
        self.path = list()
        self.fitness = random.randint(0, 20)
        self.probability = 0

    def setProbability(self, probability):
        self.probability = probability

    def getProbability(self):
        return self.probability

    def getPath(self):
        return self.path

    def getFitness(self):
        return self.fitness
        
townList = ['a', 'b', 'c', 'd', 'e', 'f']
count = 0
MAX_POPULATION = 4
populationList = list()
checkList = list()

#create parent
while count < MAX_POPULATION:
    populationList.append(population())
    while len(populationList[count].getPath()) != len(townList):
        randTownNumber = random.randint(0, len(townList)-1)
        if randTownNumber not in checkList:
            checkList.append(randTownNumber)
            populationList[count].getPath().append(townList[randTownNumber])
    checkList = list()
    count = count + 1

#roulette selection (Genetic Algorithm) for check crossover
#sort populationList
populationList = sorted(populationList, key=lambda population: population.fitness)
#end sort populationList

sumFitness = 0
for population in populationList:
    #find sum of fitness
    print population.getFitness()
    sumFitness = sumFitness + population.getFitness()

probability = 0
sumProbabilities = 0

for population in populationList:
    population.setProbability(sumProbabilities + (float(population.getFitness()) / float(sumFitness)))
    print "prob: " + str(population.getProbability())
    sumProbabilities += population.getProbability() - sumProbabilities

#selection

populationIndex = 0
populationSelectionList = list()
while len(populationSelectionList) != 2:
    randNumber = random.uniform(0, 1)
    print "randNumber: " + str(randNumber)
    for population in populationList:
        if randNumber < population.getProbability():
            if populationIndex not in populationSelectionList:
                populationSelectionList.append(populationIndex)
                break
        populationIndex = populationIndex + 1
    populationIndex = 0

print populationSelectionList

#end roulette selection (Genetic Algorithm) for check crossover

print "All fitness: " + str(sumFitness)

for population in populationList:
    print population.getPath()            