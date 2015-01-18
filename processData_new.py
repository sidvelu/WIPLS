import numpy as np
import time
import math

# find average heading
headingData = np.loadtxt("magData.txt", dtype=float)
avgHeading = np.mean(headingData)
print avgHeading

# get raw signal data
rawSignalData = np.fromfile("FFT.bin", dtype=np.complex64)
seconds = len(rawSignalData)/256
print seconds

#print np.nonzero(rawSignalData)

# create new array to hold strength data
strengthData = np.zeros([1, seconds], dtype=np.complex64)

#for g in range(0, rawSignalData.shape[0]):
#	print rawSignalData[g]
#print ""
# determine strength by summing signal data
for y in range(0, seconds):
    sum = 0
    for x in range(0+(256*y), 256+(256*y)):
        sum = sum + rawSignalData[x]
    strengthData[0, y] = sum

strengthData = np.absolute(strengthData) / seconds
avgStrength = np.mean(strengthData)
print avgStrength
minStrength = np.amin(strengthData)
maxStrength = np.amax(strengthData)
print minStrength
print maxStrength
#print strengthData.shape
#print strengthData

# write to file, to be plotted by MATLAB
f = open('rawData_new.txt', 'a')
f.write(str(avgHeading) + "  " + str(avgStrength) + "\n")
f.write(str(minStrength) + "  " + str(maxStrength) + "\n\n")
f.close()
