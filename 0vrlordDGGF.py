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
nodePauseTime=[0,200,500,800]
#nSinks=[5,10,20,29]
nNodes=[10,15,20,25,30,35,40,45,50]
sFactor=[0,20,40,60,80,100,120,140,160,180,200]
fwdArch=[-200,-150,-100,-50,0,50,100,150,200]
#run=[10]
header="nodePauseTime, nNodes, ,sFactor , fwdArch, Average hops/flow, Average delay (ms), # of packets delivered, delivered rate, # of packets dropped, dropped rate, BW efficiency\n"

with open(outputfilename, "a") as myfile:
        myfile.write(header)
i=0
while i<len(nNodes):
        j=0
        while j<len(nodePauseTime):
                print "nNodes=%d  nodePauseTime=%d \n" %(nNodes[i],nodePauseTime[j])
                settings= "scratch/myss --nodePauseTime="+str(nodePauseTime[j])+" --nNodes="+str(nNodes[i])
                thistest=str(nodePauseTime[j])+", "+str(nNodes[i])+", "+str(sFactor[6])+", "+str(fwdArch[3])+", "
                with open(outputfilename, "a") as myfile:
                        myfile.write(thistest)
                call(["./waf", "--run" , settings])
                call(["./0proc.py", "1.tr", outputfilename])
                j+=1
        i+=1
