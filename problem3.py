# hw 2.3. create a program to display a 2D list formation on screen for each each tictactoe end game saved in a given text file where each end game is represented in a line of one-d array.


#Entry_Point

#1dboard.txt is a arbitrary file that contains a string of the tic-tac-toe games
ttt = open("test.txt","r")
#print (ttt.read() )
#make 2d list, write each game into the list and save to endgame.txt
tttEnd = open("endgame.txt", "w")
temp = list(ttt.read())
tttable = list()
for i in range (3):
    row = list()
    for t in range (3): 
        row.append(t)
        tttable.append(row)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
pos = 0
for r in range (3):
    for c in range (3):
        if (temp[pos] == ' '):
            print ("S")
        else:
            tttable [r][c] = temp[pos]
        pos+=1
        print ( tttable[r][c], end = '' )


'''
temp = ( ttt.read() )
pos = 0
for i in temp:
    print( temp[int(i):3] )
    if pos%3 == i:
        print("~~~~~")
'''

ttt.close()
#Entry_Point_End
