# 213-hw2.2
/*code to 213 hw 2.2, problem 4
4. Ask for four integer values and one string for file name: one used for upper bound for x coordinate (xu), one for upper bound for y coordinate (yu), and one for number of points (N). Generate N randome points on the cartesian plane (xy) bounded by (0, xu) horizontally and (0, yu) vertically. Also generate an edge bond for each pair of the nodes whose distance is shorter than the threshold (t). Save the result in the text file using the provided file name in following format.


Please provide four input for x upper bound, y upper bound, number of points, threshold for neighbour bound and file name. 
200 300 4 50 data1.txt

Your program should create a file named as data1.txt under the same directory that has the following content in it.
==================
Vertics
index  x  y
1      10 20
2      30 40
3      30 250
4      34 10
===================
edges
index1 index2   distancevalue
1      2        distancevalue between point 1 and 2
1      4        distancevalue between point 1 and 4


hint: the distance can be calculated using pythogenrean theorm. 
https://en.wikipedia.org/wiki/Pythagorean_theorem
https://math.info/Algebra/Distance_Cartesian_Plane/
*/
