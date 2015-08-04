#! /usr/bin/env python
# This script is for staging ns-3 simulations w/ various parameters
# It will then use a python script to postprocess and output results to a file
# Finally it will Graph results
# USAGE  ./0vrlordSeed.py
# CONSTRANINTS
# ToDo
# -Input via csv where each field represents a specific simulation parameter and each row
#    represents a simulation run-Could even have a simulation generation script
#    that takes a csv where first row represents simulation set parameters
#    OR accept a csv where a field contains value name to change and next field is desired value
#    ie   run, 5, nSinks, 200
from subprocess import call
import sys
import os
tempfilename="2ot.cvs"
outputfilename=sys.argv[1]
nodePauseTime=[0,10,20,30,40,50,60,70,80,90]
nodeMaxSpeed=[20,25,30,35,40,45,50]
nNodes=[10,15,20,25,30,35,40,45,50]
nFlows=[5,10,20,29]
Proto='AODV' #, 'AODV'] #, 'DSDV', 'DSR', 'OLSR']
sFactor=[0,20,40,60,80,100,120,140,160,180,200]
fwdArch=[-200,-150,-100,-50,0,50,100,150,200]
SeedValue=[2,3,4,5,6,7,8,9,10]
SeedRun=[10,200,3,40,500,6,70,800,9]

header="Proto, nodeMaxSpeed, nNodes, Average hops/flow, Average delay (ms), Average PDR\n"
with open(outputfilename, "a") as myfile:
        myfile.write(header)
i=0
while i<len(nodeMaxSpeed):
        j=0
        while j<len(nNodes):
		k=0
		while k<len(SeedRun):
                	settings= "scratch/"+Proto+" --RngRun="+str(SeedRun[k])+ " --nodePauseTime=0 --nFlows=9 --totalTime=100 --nodeMaxSpeed="+str(nodeMaxSpeed)
                	print (settings)
			call(["./waf", "--run" , settings])
			procfile="./0p"+Proto+".py "+Proto+".tr "+tempfilename
                	os.system(procfile)
			k+=1
		deltr="rm "+Proto+".tr"
		os.system(deltr)
		with open(tempfilename) as f:
			lines =  f.read().splitlines()
		temphops=0
		tempdelay=0
		tempPDR=0
		avglen=0
		for line in lines:
			temp=line.split(' ')[0]
			temphops+=float(temp.split(',')[0])
			temp=line.split(' ')[1]
			tempdelay+=float(temp.split(',')[0])
			temp=line.split(' ')[3]
			tempPDR+=float(temp.split(',')[0])
			avglen+=1 
		removetemp="rm "+tempfilename
		os.system(removetemp)
		avglen=float(avglen)
		avghops=temphops/avglen
		avgdelay=tempdelay/avglen
		avgPDR=tempPDR/avglen
    		thistest=Proto+", "+str(nodePauseTime[i])+", "+str(nFlows[j])+", "+str(avghops)+", "+str(avgdelay)+", "+str(avgPDR)+"\n"
		with open(outputfilename, "a") as myfile:
			myfile.write(thistest)			
                j+=1
        i+=1      
