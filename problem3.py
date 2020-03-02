# hw 2.3. create a program to display a 2D list formation on screen for each each tictactoe end game saved in a given text file where each end game is represented in a line of one-d array.
tttable = None

def createboard():
    global tttable
    tttable = list()
    for i in range (4):
        row = list()
        for t in range (4): 
            row.append(t)
            tttable.append(row)

    print("____________________")
#createboard_End

def displayboard():
    for r in range(0,4):
        print()
        for c in range(0,4):
            print(tttable[r][c], end = " ")
    print()

    print("____________________")
#displayboard_End
def fillboard():
    global tttable
    for c in range (4):
        #templist to store games
        tttable [0][c] = masterList[c]

#fillTable_End


#Entry_Point
createboard()
displayboard()
ttt = open("test.txt","r")
#print (ttt.read() )
#make 2d list, write each game into the list and save to endgame.txt
tttEnd = open("endgame.txt", "w")#makes endgame.txt and opens writable
masterList = list(ttt.read())
print(masterList, ' ')
displayboard()

print("G1:")
createboard()
fillboard()
displayboard()

print("G2:")
createboard()
fillboard()
displayboard()


'''
def loadGame(gameid):   adapt to 3x3
    load = open(gameid, 'r')
    row = 0
    for rank in load:
        for col in range (8):
            chessboard[row][col] = rank[col]
        row+=1
        if row == 8:
            break
            '''

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
