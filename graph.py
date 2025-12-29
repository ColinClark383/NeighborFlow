import random
import heapq
from collections import deque

class Node:
    def __init__(self, name, path, values):
        self.name = name
        self.path = path
        self.values = values
        self.neighbors = set()

class Graph:
    def __init__(self):
        self.dimensionValues = []
        self.nodes = set()
        self.loadConfig()
        self.loadNodes()
        self.setNeighbors()
        self.printNodes()
        self.curNode = None
        self.recentQueue = deque()
    
    def loadConfig(self):
        i = 0
        with open("settings.cfg", "r") as file:
            for rawLine in file:
                line = rawLine.strip()
                match i:
                    case 0:
                        self.dimension = int(line)
                    case 1:
                        self.tracklist = line
                    case 2:
                        self.maxNeighbors = int(line)
                    case 3:
                        self.queueSize = int(line)
                    case _:
                        self.dimensionValues.append(line)
                i += 1

    def loadNodes(self):
        with open(self.tracklist, "r") as file:
            lines = file.read().splitlines()
        i = 0
        while i < len(lines):
            songName = lines[i]
            songPath = lines[i + 1]
            songVals = []
            for j in range(self.dimension):
                songVals.append(int(lines[i + 2 + j]))
            newNode = Node(songName, songPath, songVals)
            self.nodes.add(newNode)
            i += 2 + self.dimension


    def setNeighbors(self):
        for n in self.nodes:
            potentialNeighbors = list(self.nodes - {n})
            chosen = self.k_closest(potentialNeighbors, n, self.maxNeighbors)
            for c in chosen:
                n.neighbors.add(c)
                c.neighbors.add(n)

    def k_closest(self, points, target, k):
        return heapq.nsmallest(
            k,
            points,
            key=lambda p: self.squared_euclidean(p, target)
        )

    def squared_euclidean(self, a, b):
        return sum((x - y) ** 2 for x, y in zip(a.values, b.values))
    
    def chooseNext(self):
        if self.curNode == None:
            self.curNode = random.choice(list(self.nodes))
        else:
            self.recentQueue.append(self.curNode)
            if len(self.recentQueue) > self.queueSize:
                self.recentQueue.popleft()
            nextNode = None
            while nextNode == None:
                nextNode = random.choice(list(self.curNode.neighbors))
                if nextNode in self.recentQueue:
                    nextNode = None
            self.curNode = nextNode
        print(f"now playing: {self.curNode.name}")
        return self.curNode.path
    
    def printConfigs(self):
        print(f"how many dimensions? {self.dimension}")
        print(self.dimensionValues)
        print(f"max number of neighbors? {self.maxNeighbors}")
        print(f"no repeat queue size? {self.queueSize}")
        print(f"track information found in {self.tracklist}")

    def printNodes(self):
        for n in self.nodes:
            print(f"song name: {n.name}")
            print(f"song location: {n.path}")
            for i in range(self.dimension):
                print(f"value for {self.dimensionValues[i]}: {n.values[i]}")
            print(f"number of neighbors: {len(n.neighbors)}")
            for i in n.neighbors:
                print(i.name)
            print("")

    

