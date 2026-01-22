# CS3100 - Fall 2023 - Programming Assignment 5
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
import networkx as nx

class TilingDino:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of tiling dino.  It takes as input a list lines of input
    # as strings.  You should parse that input, find a tiling,
    # and return a list of strings representing the tiling
    #
    # @return the list of strings representing the tiling
    def compute(self, lines):
        G = nx.DiGraph()
        rows = len(lines)
        cols = len(lines[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if lines[r][c] == "#":
                    count += 1
                    if (r+c)%2 == 0:
                        G.add_edge("x", str(c) + " " + str(r), capacity=1.0)
                        side = "x"
                    else:
                        G.add_edge(str(c) + " " + str(r), "y", capacity=1.0)
                        side = "y"
                    if r == 0 and c == 0:
                        if lines[r][c+1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c+1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r+1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r+1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                    elif r == 0 and c == cols - 1:
                        if lines[r][c-1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c-1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r+1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r+1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                    elif r == rows - 1 and c == 0:
                        if lines[r][c+1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c+1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r-1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r-1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                    elif r == rows - 1 and c == cols - 1:
                        if lines[r][c-1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c-1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r-1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r-1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                    elif r == 0:
                        if lines[r][c-1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c-1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r][c+1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c+1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r+1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r+1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                    elif c == 0:
                        if lines[r-1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r-1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r+1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r+1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r][c+1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c+1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                    elif r == rows - 1:
                        if lines[r][c-1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c-1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r][c+1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c+1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r-1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r-1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                    elif c == cols - 1:
                        if lines[r][c-1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c-1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r-1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r-1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r+1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r+1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                    else:
                        if lines[r][c-1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c-1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r][c+1] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c+1) + " " + str(r)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r+1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r+1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
                        if lines[r-1][c] == "#":
                            start = str(c) + " " + str(r)
                            end = str(c) + " " + str(r-1)
                            if side == "x":
                                G.add_edge(start, end, capacity=1.0)
                            else:
                                G.add_edge(end, start, capacity=1.0)
        flow_value, flow_dict = nx.maximum_flow(G, "x", "y")
        list = []
        for edge in G.edges:
            if edge[0] != "x" and edge[0] != "y" and edge[1] != "x" and edge[1] != "y" and flow_dict[edge[0]][edge[1]] == 1.0:
                list.append(edge[1] + " " + edge[0])
        
        if count / 2 == flow_value:
            return list
        else:
            return ["impossible"]
