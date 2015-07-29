#! /usr/bin/env python
# This script is for staging ns-3 simulations w/ various parameters
# It will then use a python script to postprocess and output results to a file
# Finally it will Graph results 
# USAGE  ./0pyg.py <input.cvs> <xcolumnnumber> <ycolumnnumber> <multilinecolumnnumber>
# CONSTRANINTS
# ToDo
# -Input via csv where each field represents a specific simulation parameter and each row 
#    represents a simulation run-Could even have a simulation generation script
#    that takes a csv where first row represents simulation set parameters
#    OR accept a csv where a field contains value name to change and next field is desired value
#    ie   run, 5, nSinks, 200
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
#Disable interactive plotting
#plt.ioff()
#create a new figure
#fig = plt.figure()
inputfile=sys.argv[1]
xcol=int(sys.argv[2])
ycol=int(sys.argv[3])
multiline=int(sys.argv[4])
with open(inputfile, 'rb') as f:
	reader = csv.reader(f)
	alldata = list(reader)
plt.xlabel(alldata[0][xcol])
plt.ylabel(alldata[0][ycol])
multilabel=alldata[0][multiline]
datalength=len(alldata)
x=[]
y=[]
mlf=[]
for i in range(1,datalength-1):
	mlf.append(alldata[i][multiline])
mlfnew=list(set(mlf))
mlfnew.sort()
print(mlfnew)
for j in mlfnew:
	for i in range(1,datalength-1):
		if alldata[i][multiline]==j:
			x.append(int(alldata[i][xcol]))
			y.append(float(alldata[i][ycol]))
	plt.plot(x,y)
	x=[]
	y=[]
plt.legend(mlfnew, title=multilabel)
plt.set_ylim([0.84,1.00])
#plt.set_ylim([0.50,1.00])    #yaxis for NODESvsPDR

#Next line will plot an interactive plot
plt.show()

#Nextline will save a plot to file
#plt.savefig('3siftPausePDR.png')
#plt.close(fig)
