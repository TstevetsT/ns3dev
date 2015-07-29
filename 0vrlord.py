#! /usr/bin/env python
# This script is for staging ns-3 simulations w/ various parameters
# It will then use a python script to postprocess and output results to a file
# Finally it will Graph results 
# USAGE  ./0proc.py
# CONSTRANINTS
# ToDo
# -Input via csv where each field represents a specific simulation parameter and each row 
#    represents a simulation run-Could even have a simulation generation script
#    that takes a csv where first row represents simulation set parameters
#    OR accept a csv where a field contains value name to change and next field is desired value
#    ie   run, 5, nSinks, 200
from subprocess import call
import sys
outputfilename=sys.argv[1]
nodePauseTime=[0,100,200,300,400,500,600,700,800,900]
nFlows=[5,10,20,29]
#nNodes=[30,60,90,120]
#sFactor=[0,20,40,60,80,100,120,140,160,180,200]
#fwdArch=[-600,-400,-200,0,200,400,600]
#run=[10]
header="nodePauseTime, nFlows, Average hops/flow, Average delay (ms), # of packets delivered, delivered rate, # of packets dropped, dropped rate, BW efficiency\n"
with open(outputfilename, "a") as myfile:
	myfile.write(header)
i=0
while i<len(nFlows):
	j=0
	while j<len(nodePauseTime):
		#print "nFlows=%d  nodePauseTime=%d \n" %(nFlows[i],nodePauseTime[j])
		settings= "scratch/DGGF --nodePauseTime="+str(nodePauseTime[j])+" --nFlows="+str(nFlows[i])
                print(settings)
		thistest=str(nodePauseTime[j])+", "+str(nFlows[i])+", "
		with open(outputfilename, "a") as myfile:
			myfile.write(thistest)
		call(["./waf", "--run" , settings])
		call(["./0proc.py", "1.tr", outputfilename])
		j+=1
	i+=1
#
#print(settings)
