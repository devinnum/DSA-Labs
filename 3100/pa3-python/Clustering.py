# CS3100 - Fall 2023 - Programming Assignment 3
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
# Sources: Introduction to Algorithms, Cormen, https://betterprogramming.pub/how-to-use-comparable-classes-in-python-a897f9bccf25
#################################

import heapq as pq

class Clustering:
    def __init__(self):
        return

     # This is the method that should compute the maximum possible
     # spacing. It takes as input an integer k and an nxn array of
     # distances. 
     #
     # @return the maximum possible spacing 
    def compute(self, k, distances):
        # print(distances)
        nodes = []
        for i in range(len(distances)):
            node = Node(i, None, distances[i], float('inf'))
            pq.heappush(nodes, node)
            
        # print(nodes)
        # for i in nodes:
        #     print(i.id)

        nodes[0].d = 0
        # print(nodes[0].d)
        T = []
        
        # print(len(nodes))

        # for i in nodes:
        #     print(i.parent)
        
        # print("################")

        while len(nodes) != 0:
            v = pq.heappop(nodes)
            T.append(v)
            for i in nodes:
                if i.neighbors[v.id] < i.d:
                    i.d = i.neighbors[v.id]
                    i.parent = v
                    pq.heapify(nodes)

        edges = []
        for i in T:
            if i.parent is None:
                pass
            else:
                # print(i.id)
                # print(i.neighbors[i.parent.id])
                edges.append(i.neighbors[i.parent.id])

        edges.sort()
        edges = edges[(len(edges) - k + 1):]

        return edges[0]

class Node:
    def __init__(self, id, parent, neighbors, d):
        self.id = id
        self.parent = parent
        self.neighbors = neighbors
        self.d = d
        return
    
    #https://betterprogramming.pub/how-to-use-comparable-classes-in-python-a897f9bccf25
    def __lt__(self, other):
        return self.d < other.d