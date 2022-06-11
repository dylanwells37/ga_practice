#!/bin/bash
#Defining variables and operators to send into the python script
source=/Users/dylanwells/Scripts/ga_practice
pop=50
death=40
#immi cross and muta must add up to death
immi=15
cross=10
muta=15
runs=100
python $source"/lin_ga.py" $source $pop $death $immi $cross $muta $runs



