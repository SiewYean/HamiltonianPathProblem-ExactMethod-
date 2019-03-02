import random,time

class Graph:

    def __init__(self, numOfNodes):
        if numOfNodes > 0:
            self.numOfNodes = numOfNodes
        else:
            print("Error")

    def calculateMaxPairs(self):
        self.maxPairs = self.numOfNodes*(self.numOfNodes - 1)//2

    def generatePairs(self):
        self.calculateMaxPairs()

        self.pairs = []
        startRange = self.numOfNodes
        endRange = (self.numOfNodes - 10)*3 + 18
        numOfPairs = random.randint(startRange, endRange)
        print("Random total of pairs:", numOfPairs)

        while len(self.pairs) != numOfPairs:
            try:
                startNode = random.randint(1, self.numOfNodes)
                endNode = random.randint(1, self.numOfNodes)
                if startNode == endNode:
                    raise ValueError
            except ValueError:
                pass
            else:
                pair = (startNode, endNode)
                invertedPair = (endNode, startNode)

                if pair not in self.pairs and invertedPair not in self.pairs:
                    self.pairs.append(pair)
        self.hamiltonianPath = []
        print("Pairs:", self.pairs)

    def generatePathLink(self):
        self.graphLink = {}
        for x in self.pairs:
            x = str(x)
            splitNode = x.split(', ')
            a = int(splitNode[0][1:])
            b = int(splitNode[1][:-1])
            try:
                if b not in self.graphLink[a]:
                    self.graphLink[a].append(b)
            except KeyError:
                self.graphLink[a] = []
                self.graphLink[a].append(b)
            finally:
                try:
                    if a not in self.graphLink[b]:
                        self.graphLink[b].append(a)
                except KeyError:
                    self.graphLink[b] = []
                    self.graphLink[b].append(a)
                finally:
                    pass
        print("Graph linkage:", self.graphLink)

    def findPaths(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphLink:
            return []
        paths = []
        for node in self.graphLink[start]:
            if node not in path:
                newpaths = self.findPaths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
                    if (len(newpath) == self.numOfNodes):
                        self.hamiltonianPath = newpath
                        raise OverflowError
        return paths

    def exhaustiveSearch(self):
        try:
            allPaths = []
            for startNode in self.graphLink:
                for endNode in self.graphLink:
                    newPaths = self.findPaths(startNode, endNode)
                    for path in newPaths:
                        if (len(path) == self.numOfNodes):
                            allPaths.append(path)
            return allPaths
        except OverflowError:
            return self.hamiltonianPath
        else:
            pass

    def isHamiltonianPathExist(self):
        time_start = time.clock()
        self.generatePathLink()
        print("Finding Hamiltonian Paths...")

        if len(self.graphLink) != self.numOfNodes:
            time_elapsed = (time.clock() - time_start)
            print("The graph is not connected.\nHence, there is no Hamiltonian Paths.")
            print("Computing time:", round(time_elapsed, 2), "seconds\n")
            return [[], time_elapsed]
        else:
            result = self.exhaustiveSearch()
            time_elapsed = (time.clock() - time_start)
            if len(result) == 0:
                print("There is no Hamiltonian Paths.")
                print("Computing time:", round(time_elapsed, 2), "seconds\n")
            else:
                print("Example of a Hamiltonian Path:", result)
                print("Computing time:", round(time_elapsed, 2), "seconds\n")
            return [result, time_elapsed]


yes = 0
no = 0
total_computing_time = 0
numOfNodes = 10
numOfProblems = 50

for x in range(1, numOfProblems + 1):
    print(x)
    graph = Graph(numOfNodes)
    graph.generatePairs()
    output = graph.isHamiltonianPathExist()
    total_computing_time += output[1]
    if len(output[0]) == 0:
        no += 1
    else:
        yes += 1

print("Have HP:", yes)
print("No HP:", no)
print("Total computing time for %s problems: %s s"%(numOfProblems, str(round(total_computing_time, 2))))
