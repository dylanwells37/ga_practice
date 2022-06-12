#!/bin/bash
source=/Users/dylanwells/Scripts/ga_practice/
#choosing the scripts to compare
script1=lowEP_ga
script2=highCross_ga
#moves data from past runs of these scripts
mv $source$script1".csv" $source"OldRuns/"
mv $source$script2".csv" $source"OldRuns/"
#runs each script 1000 times, writing the data to a csv file
for i in {1..1000}
do
	sh $source$script1".sh"
	sh $source$script2".sh"
done
#calls python scripts to analyze the csv files produced, graphs and calculates avg & max
python $source"analysis.py" $source $script1 $script2
#moves the graph into the comparisons directory
mv $source$script1"VS"$script2".png" $source"Comparisons/"$script1"VS"$script2".png"
