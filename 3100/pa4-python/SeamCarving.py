# CS3100 - Fall 2023 - Programming Assignment 4
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
import math

class SeamCarving:
    def __init__(self):
        self.seam = []
        self.path = []
        return

    # This method is the one you should implement.  It will be called to perform
    # the seam carving.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the seam's weight
    
    def compute(self, image):
        rows = len(image)
        cols = len(image[0])
        self.seam = [0 for i in range(cols)]
        self.path = [0 for i in range(rows)]

        energy = [[0 for i in range(cols)] for j in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i > 0 and i < rows - 1 and j > 0 and j < cols - 1:
                        e = 0
                        for r in range(i-1,i+2):
                            for c in range(j-1, j+2):
                                e += math.sqrt(pow((image[i][j][0]-image[r][c][0]),2) + pow((image[i][j][1]-image[r][c][1]),2) + pow((image[i][j][2]-image[r][c][2]),2))
                        energy[i][j] = e/8
                elif i == 0 and j == 0:
                    e = 0
                    for r in range(i,i+2):
                        for c in range(j, j+2):
                            e += math.sqrt(pow((image[i][j][0]-image[r][c][0]),2) + pow((image[i][j][1]-image[r][c][1]),2) + pow((image[i][j][2]-image[r][c][2]),2))
                    energy[i][j] = e/3
                elif i == 0 and j == cols-1:
                    e = 0
                    for r in range(i,i+2):
                        for c in range(j-1, j+1):
                            e += math.sqrt(pow((image[i][j][0]-image[r][c][0]),2) + pow((image[i][j][1]-image[r][c][1]),2) + pow((image[i][j][2]-image[r][c][2]),2))
                    energy[i][j] = e/3
                elif i == rows-1 and j == 0:
                    e = 0
                    for r in range(i-1,i+1):
                        for c in range(j, j+2):
                            e += math.sqrt(pow((image[i][j][0]-image[r][c][0]),2) + pow((image[i][j][1]-image[r][c][1]),2) + pow((image[i][j][2]-image[r][c][2]),2))
                    energy[i][j] = e/3
                elif i == rows-1 and j == cols-1:
                    e = 0
                    for r in range(i-1,i+1):
                        for c in range(j-1, j+1):
                            e += math.sqrt(pow((image[i][j][0]-image[r][c][0]),2) + pow((image[i][j][1]-image[r][c][1]),2) + pow((image[i][j][2]-image[r][c][2]),2))
                    energy[i][j] = e/3
                elif i == 0:
                    e = 0
                    for r in range(i,i+2):
                        for c in range(j-1, j+2):
                            e += math.sqrt(pow((image[i][j][0]-image[r][c][0]),2) + pow((image[i][j][1]-image[r][c][1]),2) + pow((image[i][j][2]-image[r][c][2]),2))
                    energy[i][j] = e/5
                elif i == rows-1:
                    e = 0
                    for r in range(i-1,i+1):
                        for c in range(j-1, j+2):
                            e += math.sqrt(pow((image[i][j][0]-image[r][c][0]),2) + pow((image[i][j][1]-image[r][c][1]),2) + pow((image[i][j][2]-image[r][c][2]),2))
                    energy[i][j] = e/5
                elif j == 0:
                    e = 0
                    for r in range(i-1,i+2):
                        for c in range(j, j+2):
                            e += math.sqrt(pow((image[i][j][0]-image[r][c][0]),2) + pow((image[i][j][1]-image[r][c][1]),2) + pow((image[i][j][2]-image[r][c][2]),2))
                    energy[i][j] = e/5
                elif j == cols-1:
                    e = 0
                    for r in range(i-1,i+2):
                        for c in range(j-1, j+1):
                            e += math.sqrt(pow((image[i][j][0]-image[r][c][0]),2) + pow((image[i][j][1]-image[r][c][1]),2) + pow((image[i][j][2]-image[r][c][2]),2))
                    energy[i][j] = e/5

        seams = [[None] * cols for i in range(rows)]

        seams[-1] = energy[-1][:]

        # for i in range(rows-2, -1, -1):
        #     seams[i] = [energy[i][j] + min(seams[i+1][js] for js in (j-1, j, j+1) if 0 <= js < cols) for j in range(cols)]

        # least = min(seams[0])
        # start = seams[0].index(min(seams[0]))
        # self.path[0] = start

        # for i in range(1,rows):
        #     start = seams[i].index(min(seams[i][starts] for starts in (start-1, start, start+1) if 0 <= starts < cols))
        #     self.path[i] = start
        # return least

        seams[0] = energy[0][:]

        for i in range(1,rows):
            seams[i] = [energy[i][j] + min(seams[i-1][js] for js in (j-1, j, j+1) if 0 <= js < cols) for j in range(cols)]

        least = min(seams[-1])
        start = seams[-1].index(least)
        self.path[-1] = start

        for i in range(rows-2,-1,-1):
            if start == 0:
                start = min((start,seams[i][start]), (start+1,seams[i][start+1]), key=lambda x:x[1])[0]
                self.path[i] = start
            elif start == cols-1:
                start = min((start-1,seams[i][start-1]), (start,seams[i][start]), key=lambda x:x[1])[0]
                self.path[i] = start
            else:
                start = min((start-1,seams[i][start-1]), (start,seams[i][start]), (start+1,seams[i][start+1]), key=lambda x:x[1])[0]
                self.path[i] = start
            #start = seams[i].index(min(seams[i][starts] for starts in (start-1, start, start+1) if 0 <= starts < cols))
            #self.path[i] = start
        return least

    # Get the seam, in order from top to bottom, where the top-left corner of the
    # image is denoted (0,0).
    # 
    # Since the y-coordinate (row) is determined by the order, only return the x-coordinate
    # 
    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    #         as an array
    def getSeam(self):
        return self.path

