# CS3100 - Fall 2023 - Programming Assignment 2
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
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen, https://stackoverflow.com/questions/37111798/how-to-sort-a-list-of-x-y-coordinates
#################################
import math

class RobotMulcher:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest tree.  It takes as input a list lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest distance
    # and return that value from this method
    #
    # @return the distance between the closest trees 
    
    def compute(self, file_data):
        out = com(file_data)
        return out

    
def com(file_data):

        points = []
        for line in file_data:
            point = line.split()
            point[0] = float(point[0])
            point[1] = float(point[1])
            points.append(point)

        points.sort()
        xcoords = []
        for point in points:
            xcoords.append(point[0])
        
        if len(xcoords) % 2 == 0:
            median = (xcoords[len(xcoords)//2] + xcoords[(len(xcoords)//2) - 1])/2
        else:
            median = xcoords[len(xcoords)//2]
    
        return closest(points, median)

def closest(points, median):
    if len(points) == 2:
        dist = math.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2)
        return dist 
    elif len(points) == 3:
        dist1 = math.sqrt((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1])**2)
        dist2 = math.sqrt((points[2][0] - points[0][0])**2 + (points[2][1] - points[0][1])**2)
        dist3 = math.sqrt((points[1][0] - points[2][0])**2 + (points[1][1] - points[2][1])**2)
        minimum = min(dist1, dist2, dist3)
        return minimum

    else:
        leftpoints = []
        rightpoints = []
        for point in points:
            if point[0] < median:
                leftpoints.append(point)
            else:
                rightpoints.append(point)
        if len(leftpoints) % 2 == 0:
            leftmedian = (leftpoints[len(leftpoints)//2][0] + leftpoints[(len(leftpoints)//2) - 1][0])/2
        else:
            leftmedian = leftpoints[len(leftpoints)//2][0]
        if len(rightpoints) % 2 == 0:
            rightmedian = (rightpoints[len(rightpoints)//2][0] + rightpoints[(len(rightpoints)//2) - 1][0])/2
        else:
            rightmedian = rightpoints[len(rightpoints)//2][0]

        d = min(closest(leftpoints, leftmedian), closest(rightpoints, rightmedian))
        runway = []
        left = median - d
        right = median + d
        for point in points:
            if point[0] > left and point[0] < right:
                runway.append(point)

        runway = sorted(runway , key=lambda k: [k[1], k[0]])
        minimum = 99999999
        for i in range(len(runway)):
            if len(runway) - i - 1 >= 15:
                
                for j in range(i + 1, i + 16):
                    dist = math.sqrt((runway[j][0] - runway[i][0])**2 + (runway[j][1] - runway[i][1])**2)
                    if dist < minimum:
                        minimum = dist
            else:
                
                for j in range(i + 1, len(runway)):
                    dist = math.sqrt((runway[j][0] - runway[i][0])**2 + (runway[j][1] - runway[i][1])**2)
                    if dist < minimum:
                        minimum = dist
        

        return min(d, minimum)