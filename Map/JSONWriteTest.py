import json
from datetime import datetime

with open('Map/templates/data.json') as data_file:
    data = json.load(data_file)

input = open('Map/fakeinput.txt')

error = False
tracker = -1
for line in input:
    if (line == ""):
        continue

    data["lastupdate"] = datetime.now().strftime("%m/%d %H:%M:%S")

    #print line
    if line[0] == "1":
        tracker = 1
    elif line[0] == "2":
        tracker = 2
    elif line[0] == "3":
        tracker = 3
    else:
        print "Input parse failed: Invalid tracker"
        continue

    if "ERROR" in line:
        #error found
        data["error"] += (line + "!")
        error = True
    elif "coords" in line:
        #Coords
        coords = line.split(":")[1].strip("( )\n")
        lat, long = coords.split(",")
        #print "Tracker " + str(tracker) + " Lat = " + str(lat) + ", Long = " + str(long)
        data["antenna" + str(tracker) + "Coords"]["lat"] = float(lat)
        data["antenna" + str(tracker) + "Coords"]["long"] = float(long)
    elif "angle" in line:
        #Angle
        phi = line.split(":")[1].strip()
        #print "Tracker " + str(tracker) + " Phi = " + str(phi)
        data["antenna" + str(tracker) + "Coords"]["phi"] = float(phi)
    elif "tilt" in line:
        #Tilt
        theta = line.split(":")[1].strip()
        #print "Tracker " + str(tracker) + " Theta = " + str(theta)
        data["antenna" + str(tracker) + "Coords"]["theta"] = float(theta)
    else:
        print "Input parse failed"
        continue

    import Map.TriangulationAlgorithm
    try:
        Corner1, Corner2, Corner3, Avgguess = Map.TriangulationAlgorithm.start(
            data["antenna1Coords"]["lat"],
            data["antenna1Coords"]["long"],
            data["antenna1Coords"]["ele"],
            data["antenna1Coords"]["phi"],
            data["antenna1Coords"]["theta"],

            data["antenna2Coords"]["lat"],
            data["antenna2Coords"]["long"],
            data["antenna2Coords"]["ele"],
            data["antenna2Coords"]["phi"],
            data["antenna2Coords"]["theta"],

            data["antenna3Coords"]["lat"],
            data["antenna3Coords"]["long"],
            data["antenna3Coords"]["ele"],
            data["antenna3Coords"]["phi"],
            data["antenna3Coords"]["theta"]
        )

        data["beaconGuessCoords"]["lat"] = Avgguess.lat
        data["beaconGuessCoords"]["long"] = Avgguess.long
        data["beaconGuessCoords"]["ele"] = Avgguess.height
        data["guessVector"] = []
        data["guessVector"].insert(0, {})
        data["guessVector"].insert(0, {})
        data["guessVector"].insert(0, {})
        data["guessVector"][0]["lat"] = Corner1.lat
        data["guessVector"][0]["long"] = Corner1.long
        data["guessVector"][0]["ele"] = Corner1.height
        data["guessVector"][1]["lat"] = Corner2.lat
        data["guessVector"][1]["long"] = Corner2.long
        data["guessVector"][1]["ele"] = Corner2.height
        data["guessVector"][2]["lat"] = Corner3.lat
        data["guessVector"][2]["long"] = Corner3.long
        data["guessVector"][2]["ele"] = Corner3.height
    except Exception as e:
        print e.message
        continue

if (not error):
    data["error"] = ""

with open('Map/templates/data.json', 'w') as data_file2:
    json.dump(data, data_file2, separators=(',', ': '), indent=4)
