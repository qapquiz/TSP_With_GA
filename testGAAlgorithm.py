import random
class population:
    def __init__(self):
        self.sumDistance = 0
        self.path = list()
    
    def getPath(self):
        return self.path

townList = ['a', 'b', 'c', 'd', 'e', 'f']
count = 0
MAX_POPULATION = 2
populationList = list()
checkList = list()
while count < MAX_POPULATION:
    populationList.append(population())
    while len(populationList[count].getPath()) != len(townList):
        randTownNumber = random.randint(0, len(townList)-1)
        if randTownNumber not in checkList:
            checkList.append(randTownNumber)
            populationList[count].getPath().append(townList[randTownNumber])
    checkList = list()
    count = count + 1
    
for population in populationList:
    print population.getPath()            