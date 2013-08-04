from Town import Town
import matplotlib.pyplot as plt

townList = list()
townData = open("town.txt", 'r')
while townData:
	line = townData.readline().split()
	if (line == []):
		break;
	townList.append(Town(line[0], line[1], line[2]))

plt.plot([1, 2, 3, 4])
