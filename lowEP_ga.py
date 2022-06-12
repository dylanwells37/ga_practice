#This is a test python program to gain practice writing genetic algorithms
#This program will use a genetic algorithm to find the maximum of
#an equation in a certain parameter space (maximize z)
#importing python thingys
import numpy as np
import math
import random
import argparse
import csv
#importing variables from the bash script
parser = argparse.ArgumentParser()
parser.add_argument("source", help="Name of source folder from home directory", type=str)
parser.add_argument("pop", help="Population size", type=int)
parser.add_argument("death", help="Death per generation", type=int)
parser.add_argument("immi", help="immigration per generation", type=int)
parser.add_argument("cross", help="crosspop per generation", type=int)
parser.add_argument("muta", help="mutations per generation", type=int)
parser.add_argument("runs", help="number of runs", type=int)
g = parser.parse_args()
#defining the variable space
xmin = 0
ymin = 0
ymax = 10
xmax = 10
survivors = g.pop-g.death
#defining the function we are finding the max of
def fxy(x, y):
	return np.sin(7*x + np.pi) + np.sin(5*y - np.pi/4)
#Creating the intial population and calculating their values
minions = []
for i in range(g.pop):
	x = random.random()*xmax
	y = random.random()*ymax
	z = fxy(x, y)
	minions.append([z, x, y])
#Ranking the minions by their z values
minions.sort()
#print("Initial population:",minions)
#Who lives Who Dies, Who Tells Your Story
def theCulling(minions):
	minions.sort()
	totalNum = int(((g.pop-2)*(g.pop-1)*(2*g.pop-3))/6) #sum of 0 to g.pop, used to get weights equal to 1
	weights = [(j**2)/totalNum for j in range(g.pop-1)] #creates an array of weights, giving one to each minion
	#creats a 1d ndarray of randomly chosen indicies np.random.choie(a, size, replace, p)
	choices = np.random.choice([i for i in range(g.pop-1)], survivors-1, replace=False, p=weights)
	tempMinions = [minions[-1]] #Max value always survives culling
	for i in range(survivors-1):
		tempMinions.append(minions[choices[i]])
	return tempMinions

#produces a new generation of minions from the last
def newGen():
	#this loop cross populates by taking 2 random survivors and making a new baby with one parent's x and one parent's y 
	for i in range(g.cross):
		#seeds are choosing the parents at random
		seed1 = random.randint(0, survivors-1)
		seed2 = random.randint(0, survivors-1)
		while seed2 == seed1: #rerolls the second seed until it doesn't equal the first
			seed2 = random.randint(0, survivors-1)
		x = minions[seed1][1]
		y = minions[seed2][2]
		z = fxy(x, y)
		minions.append([z, x, y])
	#this loop adds to the population by randomly mutating the point of a survivor by a small amount
	for i in range(g.muta):
		#seed chooses a single survivor to mutate both values of
		seed = random.randint(0, survivors-1)
		x = minions[seed][1] + (random.random()-0.5)/(xmax**2) #subtracting by 0.5 changes range of epsilon to -0.5 to 0.5
		y = minions[seed][2] + (random.random()-0.5)/(ymax**2)
		z = fxy(x, y)
		minions.append([z, x, y])
	#this loop adds to the population by randomly sampling more points in the paramter space
	for i in range(g.immi):
		x = random.random()*xmax
		y = random.random()*ymax
		z = fxy(x, y)
		minions.append([z, x, y])
#this loop runs for n generations
runcount = 0
while runcount < g.runs:
	minions = theCulling(minions)
	newGen()
	runcount = runcount+1
	minions.sort()
	with open(g.source+'/Runs/Run'+str(runcount)+'.csv', 'w') as file:
		mywriter = csv.writer(file, delimiter=',')
		mywriter.writerows(minions)
minions.sort()
print("Maximum value found:", minions[-1])
with open(g.source+'/lowEP_ga.csv', 'a') as file:
	mywriter = csv.writer(file, delimiter=',')
	mywriter.writerow(minions[-1])
