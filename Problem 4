#Ask for four integer values and one string for file name: one used for upper bound for x coordinate (xu),
#one for upper bound for y coordinate (yu), and one for number of points (N). Generate N randome points on the cartesian plane (xy) bounded by (0, xu) horizontally and (0, yu) vertically.
#Also generate an edge bond for each pair of the nodes whose distance is shorter than the threshold (t). Save the result in the text file using the provided file name in following format.
import random
import math
xRange = None
yRange = None
def writeToFile(x, y, n, t, name):#x = upBnd x, y= upBnd y,n =num of points,t = threshold on points, name = filename
    print(x, y, n ,t, name)
    global xRange
    global yRange
    
    xRange = list()
    yRange = list()
    graph = open(name + '.txt','w')
    graph.write("====================\n")
    graph.write("Vertices:\nindex \t x \t y")
    graph.write('\n')
    
    num = 0
    #fills out vertices table within the name.txt
  
    for j in range(int(n)):
        #randomly selects a number betwen 0 and given x/y bound
        xCord = random.randrange (0,int(x))
        xRange.append(xCord)
        
        yCord = random.randrange (0,int(y))
        yRange.append(yCord)
        
        info = (str(int(j+1) ),'\t\t',str(xCord), '\t', str(yCord))
        graph.writelines(info)
        graph.write('\n')
    
    #find threshold 
    #two points [index] , x and y (two numbers after)
    #sqrt( (x2-x1)^2 + (y2-y1)^2 )
    #^ that shorter than threshhold == edge
    #math.sqrt(), **2
    graph.write("====================\n")
    graph.write("Edges:\nindex1: index2: Distance Value:\n")
    for i in range(int(n)-1):#i == x    
        for j in range(int(n)-i-1):#j == y
            # print (f"x={i},y={j}")
            pOne = (xRange[i] -yRange[i+1])**2
            pTwo =  (xRange[j] -yRange[j+1])**2
            # print(f"point1 = {pOne}, point2 = {pTwo}")
            threshTest = (math.sqrt(pOne + pTwo))
            if (threshTest < int(t)):
                print(threshTest)
                edgeInfo = (f"{i+1}\t\t{j+1}\t\tDV between point {i+1} and {j+1}\n")
                graph.write(edgeInfo)
    #make a test lsit w/ example numbers to check if threshtest actually works
    #if does, weird test else debug the math
    
    graph.close()    
#writeToFile_End
    
    
    
#Entry Point
xu = input("Enter upperbound X: ")
yu = input("Enter upperbound Y: ")
num =input("Enter number of wanted points: ")
thresh = input("Enter threshhold for points: ")
fileName = input("Enter file name: ") #appends .txt when file is actually made
fileName = 'name'
writeToFile(xu, yu, num, thresh, fileName)
#Entry_Point_End
