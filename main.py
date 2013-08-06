from Town import Town
from costMatrix import CostMatrix
#import matplotlib.pyplot as plt

townList = list()
townData = open("town.txt", 'r')
while townData:
	line = townData.readline().split()
	if (line == []):
		break;
	townList.append(Town(line[0], line[1], line[2]))

#createCostMatrix
costMatrixDict = CostMatrix().createCostMatrix()
