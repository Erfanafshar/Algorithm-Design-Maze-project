# Classes
# Room class with name and color and number fields and also corridors that starts from this room
class Room:
    def __init__(self, name, color, number):
        self.corridors = []
        self.name = name
        self.color = color
        self.number = number

    def insertCorridors(self, corridor):
        self.corridors.append(corridor)


# Corridor class with color and destinationRoom fields
# That destinationRoom indicates the Room that this Corridor reach to that
class Corridor:
    def __init__(self, color, destinationRoom):
        self.color = color
        self.destinationRoom = destinationRoom


# Methods
# Find paths from two given start point to the end point
# And call recursively each possible next state in each call of function
def findPath(start1, start2):
    if start1.name == "GOAL" or start2.name == "GOAL":
        return True
    else:
        for z in checkedPaths:
            if start1.name == z[0] and start2.name == z[1]:
                return False
        checkedPaths.append((start1.name, start2.name))
        for x in start2.corridors:
            if x.color == start1.color:
                if findPath(start1, x.destinationRoom):
                    path2.append(x.destinationRoom)
                    priorities.append("2")
                    return True

        for y in start1.corridors:
            if y.color == start2.color:
                if findPath(y.destinationRoom, start2):
                    path1.append(y.destinationRoom)
                    priorities.append("1")
                    return True

    return False


# print the Path that reach to goal
def printPath():
    j = 1
    k = 1
    for i in priorities:
        if i == "1":
            print("R " + str(path1[j].number))
            j = j + 1
        if i == "2":
            print("L " + str(path2[k].number))
            k = k + 1


# Set some names form A to Z
# And form AA to ZZ for name of rooms
def setRoomsNames():
    for i in range(65, 91):
        roomsNames.append(chr(i))
    for i in range(65, 91):
        for j in range(65, 91):
            roomsNames.append(chr(i) + chr(j))


# Set the List of the Rooms
def setRoomsList():
    for i in range(int(n) - 1):
        roomsList.append(Room(roomsNames[i], roomsColors[i], int(i) + 1))
    roomsList.append(Room("GOAL", "NULL", int(n)))


# Set the Corridors in Rooms that the Corridors start from them
def setCorridors():
    for i in range(int(m)):
        thisEdge = inputFile.readline().replace("\n", "").split(" ")
        roomsList[int(thisEdge[0]) - 1].insertCorridors(Corridor(thisEdge[2], roomsList[int(thisEdge[1]) - 1]))


# Print the graph adjacency list
def showGraphAdjacencyList():
    for x in roomsList:
        print(x.name, end=" -> ")
        for y in x.corridors:
            print(y.destinationRoom.name, end="  ")
        print()


# Variables declaration
roomsNames = []
roomsList = []
checkedPaths = []
path1 = []
path2 = []
priorities = []

setRoomsNames()

# Get inputs from file
inputFile = open("input.txt")

# Line 1 input
(n, m) = inputFile.readline().replace("\n", "").split(" ")

# Line 2 input
roomsColors = inputFile.readline().replace("\n", "").split(" ")
setRoomsList()

# Line 3 input
(s1, s2) = inputFile.readline().replace("\n", "").split(" ")

# Next m line of input
setCorridors()

inputFile.close()

# Find and print the path
findPath(roomsList[int(s1) - 1], roomsList[int(s2) - 1])

path1.append(roomsList[int(s1) - 1])
path2.append(roomsList[int(s2) - 1])
path1.reverse()
path2.reverse()
priorities.reverse()

printPath()

# Can use this method for drawing matrix Adjacency List and watch that the matrix drawing in correct or not
# print()
# print("AdjacencyList : ")
# showGraphAdjacencyList()
