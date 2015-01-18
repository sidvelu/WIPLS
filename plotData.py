import numpy as np
import matplotlib.pyplot as plt
import sys

counter = 0
heading = list()
strength = list()
fileName = sys.argv[1]

with open(fileName) as fp:
    for line in fp:
        line = line.strip()
        if line != "":
            line = line.split()
            if counter == 0:
                heading.append(float(line[0]))
                strength.append(abs(complex(line[1])))
#            elif counter == 1:
#                strength.append(abs(complex(line[0])))
        counter += 1
        counter %= 3

# save start and end points
start = tuple([heading[0], strength[0]])
end = tuple([heading[len(heading)-1], strength[len(strength)-1]])

# sort both lists by heading so our graph looks nice
pairs = zip(heading, strength)
pairs.sort()
heading = [ x[0] for x in pairs ]
strength = [ x[1] for x in pairs ]

# save the min point
minIndex = strength.index(min(strength))

# create plot
plt.plot(heading, strength, 'x-', markersize=12) # data
plt.plot(heading[minIndex], strength[minIndex], 'yo', markersize=12) # min point
plt.plot(start[0], start[1], 'go', markersize=12) # start point
plt.plot(end[0], end[1], 'ro', markersize=12) # end point
plt.xlim(0, 359.99)
plt.title('Signal strength vs heading', fontsize=20)
plt.xlabel('Heading', fontsize=16)
plt.ylabel('Signal strength', fontsize=16)
plt.grid(True)
plt.show()
