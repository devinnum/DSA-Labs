# CS3100 - Fall 2023 - Programming Assignment 1
#################################
# Collaboration Policy: You may discuss the problem and the overall
# strategy with up to 4 other students, but you MUST list those people
# in your submission under collaborators.  You may NOT share code,
# look at others' code, or help others debug their code.  Please read
# the syllabus carefully around coding.  Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: dau4eb
# Collaborators: None
# Sources: Introduction to Algorithms, Cormen
#################################
from queue import Queue

def bfs(graph, s, t):
        layer = 0
        depth = [-1] * len(graph)
        toVisit = Queue(maxsize=len(graph))
        toVisit.put(s)
        seen = []
        seen.append(s)
        depth[s] = 0
        parent = [-1] * len(graph)
        while not toVisit.empty():
            current = toVisit.get()
            layer = depth[current] 
            if current == t:
                path = []
                pointer = t
                while pointer != -1:
                    path.append(pointer)
                    pointer = parent[pointer]
                path.reverse()
                return path
            for v in graph[current]:
                if v not in seen:
                    parent[v] = current
                    seen.append(v) 
                    toVisit.put(v)
                    depth[v] = layer + 1

def collision(graph, a, b):
    switch = False
    if len(a) < len(b):
        t = a
        a = b
        b = t
        switch = True
    paths = [[a[0]],[b[0]]]
    longpointer = 0
    shortpointer = 0
    long = a[longpointer]
    short = b[shortpointer]
    while long != a[-1] or short != b[-1]:

        if long == a[-1]:
            paths[0].append(a[longpointer])
            paths[1].append(b[shortpointer + 1])
            short = b[shortpointer + 1]
            shortpointer += 1
        
        elif short == b[-1]:
            paths[1].append(b[shortpointer])
            paths[0].append(a[longpointer + 1])
            long = a[longpointer + 1]
            longpointer += 1

        elif b[shortpointer + 1] in graph[a[longpointer + 1]]:
            paths[1].append(b[shortpointer])
            paths[0].append(a[longpointer + 1])
            long = a[longpointer + 1]
            longpointer += 1

        elif b[shortpointer + 1] == a[longpointer + 1]:
            paths[0].append(a[longpointer + 1])
            long = a[longpointer + 1]
            longpointer += 1

            neighbor = graph[b[shortpointer]]
            neighbor.remove(a[longpointer])
            dodge = neighbor[0]
            paths[1].append(dodge)

            paths[0].append(a[longpointer + 1])
            long = a[longpointer + 1]
            longpointer += 1

            paths[1].append(b[shortpointer])

        elif a[longpointer + 1] not in graph[b[shortpointer + 1]]:
            paths[0].append(a[longpointer + 1])
            paths[1].append(b[shortpointer + 1])
            long = a[longpointer + 1]
            short = b[shortpointer + 1]
            longpointer += 1
            shortpointer += 1

        if switch:
            t = paths[0]
            paths[0] = paths[1]
            paths[1] = t
    return paths

class Marriage:
    lukePath = []
    lorelaiPath = []

    def __init__(self):
        return

    def getLukePath(self):
        return self.lukePath

    def getLorelaiPath(self):
        return self.lorelaiPath

    # This is the method that should set off the computation
    # of marriage.  It takes as input a list lines of input
    # as strings.  You should parse that input and then compute 
    # the shortest paths that both Luke and Lorelai should take.
    # The class fields of lukePath and lorelaiPath should be filled
    # with their respective paths.  The getters above will be called
    # by the grader script.
    #
    # @return the length of the shortest paths (in rooms)
    def compute(self, file_data):
        graph = []
        for line in file_data[3:]:
            neighbors = line.split()
            for i in range(len(neighbors)):
                neighbors[i] = int(neighbors[i])
            graph.append(neighbors)

    


        lukestart = int(file_data[1].split()[0])
        lukeend = int(file_data[1].split()[1])
        lorstart = int(file_data[2].split()[0])
        lorend = int(file_data[2].split()[1])
        lukepath = bfs(graph, lukestart, lukeend)
        lorpath = bfs(graph, lorstart, lorend)
        print(lukepath)
        print(lorpath)


        shortestpaths = []
        for v in range(len(graph)):
            for u in range(len(graph)):
                shortestpaths.append(bfs(graph, v, u))

        lukeshorter = []

        while None in shortestpaths:
            shortestpaths.remove(None)

        print(shortestpaths)

        for v in shortestpaths:
            print(v[0])
            print(v[-1])
            if v[0] == lukestart:
                for u in shortestpaths:
                    print(u[0])
                    print(u[-1])
                    if v[-1] == u[0] and v[0] == lukestart and u[-1] == lukeend and (len(v) + len(u) - 1) == len(lukepath) and (v + u[1:]) not in lukeshorter:
                        lukeshorter.append(v + u[1:])
                        print(lukeshorter)
        


        while None in lukeshorter:
            lukeshorter.remove(None)
        
        print(lukepath)
        
        if lukepath not in lukeshorter:
            lukeshorter.append(lukepath)
        

        lorshorter = []

        for v in shortestpaths:
            if v[0] == lorstart:
                for u in shortestpaths:
                    if v[-1] == u[0] and v[0] == lorstart and u[-1] == lorend and (len(v) + len(u) - 1) == len(lorpath) and (v + u[1:]) not in lorshorter:
                        lorshorter.append(v + u[1:])

        while None in lorshorter:
            lorshorter.remove(None)

        if lorpath not in lorshorter:
            lorshorter.append(lorpath)
        
        print(lukeshorter)
        print(lorshorter)

       

        paths =[]

        for v in lukeshorter:
            for u in lorshorter:
                paths.append(collision(graph, v, u))

        min = 99999
        for v in paths:
            if len(v[0]) < min:
                min = len(v[0])
        for v in paths:
            if len(v[0]) == min:
                self.lukePath = v[0]
                self.lorelaiPath = v[1]
        return min