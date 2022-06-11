import pandas as pd
from matplotlib import pyplot as plt
source="/Users/dylanwells/Scripts/ga_practice/"
#Setting the column names  
column_names = ["Z", "X", "Y"]
lmCSV = pd.read_csv(source+"linearMaxes.csv", names=column_names)
smCSV = pd.read_csv(source+"squareMaxes.csv", names=column_names)
linMaxes = lmCSV.Z.to_list()
squareMaxes = smCSV.Z.to_list()
plt.plot([i for i in range(len(linMaxes))], linMaxes, ".")
plt.plot([i for i in range(len(squareMaxes))], squareMaxes, ".")
plt.title('Square vs Linear Survivorship')
plt.xlabel('Run #')
plt.ylabel('Max Value')
plt.legend(["Linear", "Squared"])
plt.show()
plt.savefig('Comparison Plot')

#Calculations
linTot = 0
for num in linMaxes:
	linTot = linTot + num
linAvg = linTot / len(linMaxes)
linMax = max(linMaxes)

squareTot = 0
for num in squareMaxes:
	squareTot = squareTot + num
squareAvg = squareTot / len(squareMaxes)
squareMax = max(squareMaxes)

print("Linear Maximum:", linMax)
print("Linear Average:", linAvg)
print("Square Maximum:", squareMax)
print("Square Average:", squareAvg)


