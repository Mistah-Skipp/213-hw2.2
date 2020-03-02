HW 2:  Programming in Python 3.
Read text book first 4 chapters. 

 
Each problem is worth 25 points. Total 100 points.


1. Ask user to provide an integer value N from keyboard, print out N*N time table with row header and col header.
To earn full credit, your result should look like the following sample run result.


Please provide an integer in the range of 1 to 9: 6

   1  2  3  4  5  6
----------------------
1 |1  2  3  4  5  6
2 |2  4  6  8 10 12   
3 |
4 |
5 |
6 |              36 


The following is a sample:

Please input your integer value [1 - 9]: -0
The value needs to be an integer in the range [1-9], please input again: 3
 
	1	2	3
------------------------- 
1|	1	2	3
2|	2	4	6
3|	3	6	9
 



Hint: use the following comment when you don't want to get a new line. 
print(str(i)+"\t", end='')
Please notice that you print out a formation of table that appears to be formatted in a 2-D shape, but internally,
without explicitly using a 2-D array to save anything. Everything can be printed on the fly. 

  

2. Save the closest distance from Earth to each of other planets (in solar system) measured in AU in a list, loop through the list and calculate the average of values in the list and save the average in a variable. Then loop through again the list, and compare each value with the average to find out those planets are within the average distance.    

Hint:
AU astronomical unit, a unit of measurement equal to 149.6 million kilometers, the mean distance from the center of the earth to the center of the sun. You should normalize the distance to AU. 
https://www.universetoday.com/15462/how-far-are-the-planets-from-the-sun/
Use a list (1-d array), initialize a sum to be 0 to start with. Loop through the list, add the current value to the list.



 


3. create a program to display a 2D list formation on screen for each each tictactoe end game saved in a given text file where each end game is represented in a line of one-d array. You have 6 games to show in total.  To test, you also need
to create a different text file containing simulated end games of your own. 

=============================================================================================================

Save the following games in a text file name as endgames.txt in the same directory where your code is located.
 XXX OXOO
 XXXO XOO
OOXXX OOX
OOXXXOOXX
OOXXXOXOX
OOXXXOXXO


Hint: 
You can explicitly use arrays if you want. You can also print out the 2D formation on the fly. 

read each line, and do NOT split,  do NOT strip space, because space character is meaningful here. 
Convert 1-d index pos to 2-d indexes row and col, using 
row=pos//3
col=pos%3

you do need to strip the new line character, which is non-printable tailing each line.
line.strip("\n")

When you save the above text file, make sure there is no empty line. 
In case your text file contains one extra empty line, you need to use that empty line to detect the end of the file, you can use strip function, if the len of the string after stripping tailing and leading spaces gives you 0 length.  


tttgamefilename = 'engames.txt'   # make sure this file exist otherwise need to handle exception (see my tutorial codes)
with open(filepath) as games:
   	cnt=0
	for line in games:
       		
		if len(line.strip())==0:
			break
		cnt += 1
		print("line {}: {}".format(cnt, line.strip('\n')))
	       	
		# show the line in 2d format as we discussed in class
		
		

#Creates a list containing 3 lists, each of 3 items, all set to 0 to start with
width, height = 3, 3;
tttboard = [[0 for x in range(width)] for y in range(height)] 
#after above you got a 2-d array (list), now you can put knot and cross in.

  


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



hint: the distance can be calculated using Pythagorean theorm. 
https://en.wikipedia.org/wiki/Pythagorean_theorem
https://math.info/Algebra/Distance_Cartesian_Plane/


What to submit?
1. Source code with inline comments 75%
2. Test results with reflection: at least test three cases including special cases or wrong input 
and what you have learned from working on this hw. 25%
3. Submit both phyiscal copy to your instructor and electronic version on Blackboard at the beginning of the class of the due date.
4. These requirements are default, ditto for all of the rest assignments, unless otherwise instructed.
