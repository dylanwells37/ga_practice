import pandas as pd
from matplotlib import pyplot as plt
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("source", help="Name of source folder from home directory", type=str)
parser.add_argument("script1", help="Name of first script", type=str)
parser.add_argument("script2", help="Name of second script", type=str)
g = parser.parse_args()
#Setting the column names of the csv  
column_names = ["Z", "X", "Y"]
firstCSV = pd.read_csv(g.source+g.script1+".csv", names=column_names)
secondCSV = pd.read_csv(g.source+g.script2+".csv", names=column_names)
#Turning the first column of the CSV into a python list
firstMaxes = firstCSV.Z.to_list()
secondMaxes = secondCSV.Z.to_list()
#Using matplotlib to plot the scatterplot of both data sets
plt.plot([i for i in range(len(firstMaxes))], firstMaxes, ".")
plt.plot([i for i in range(len(secondMaxes))], secondMaxes, ".")
plt.title(g.script1+' vs ' + g.script2 + ' Survivorship')
plt.xlabel('Run #')
plt.ylabel('Max Value')
plt.legend([g.script1, g.script2])
plt.savefig(g.script1+"VS"+g.script2)
plt.show()
#The Analysis portion
#Finding the averages and maxes of the two scripts
firstTot = 0
for num in firstMaxes:
	firstTot = firstTot + num
firstAvg = firstTot / len(firstMaxes)
firstMax = max(firstMaxes)

secondTot = 0
for num in secondMaxes:
	secondTot = secondTot + num
secondAvg = secondTot / len(secondMaxes)
secondMax = max(secondMaxes)

print("1st Script Maximum:", firstMax)
print("1st Script Average:", firstAvg)
print("2nd Script Maximum:", secondMax)
print("2nd Average:", secondAvg)
with open(g.source+"Comparisons/"+g.script1+"VS"+g.script2+".txt", 'w') as f:
	f.write(g.script1+" Maximum: " +str(firstMax)+"\n")
	f.write(g.script1+" Average: " +str(firstAvg)+"\n")
	f.write(g.script2+" Maximum: " +str(secondMax)+"\n")
	f.write(g.script2+" Average: " +str(secondAvg)+"\n")


