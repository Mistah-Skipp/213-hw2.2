# hw 2.3. create a program to display a 2D list formation on screen for each each tictactoe end game saved in a given text file where each end game is represented in a line of one-d array.
tttable = None
def createboard():
    global tttable
    tttable = list()
    for i in range (3):
        row = list()
        for t in range (3): 
            row.append(t)
            tttable.append(row)
#createboard_End

def fillboard(fileName):
    cnt = 0
    gameNum =1
    endGame = open("endgame.txt",'w')
    print("endGame File Created...")
    try:#if invalid filename for games, doesnt run
        with open(fileName) as fileobj:

            for line in fileobj:  
                endGame.write("Game {}:\n".format(gameNum) )
                for ch in line: 
                    if (ch !='\n'):#while not end of line (new line == new game in text file)
                        endGame.write(ch)
                        cnt+=1
                        if (cnt%3 == 0):#every 3rd index breaks to a new line
                            endGame.write('\n')
                    else:
                        endGame.write("--------------------\n")
                        gameNum +=1
    except FileNotFoundError:
        print("Invalid File Name!")

            
                    #endgame.write('\n')
    #tttEnd = open("endgame.txt", "w")
    #mList = [ttt.readLine()]
    #with open(str(ttt) ) as games:
    #    cnt = 0
    #    for lines in games:
#
#            if len(lines.strip()) == 0:
#                break
#            cnt+=1
#            print("line {}: {}".format(cnt,line.strip('\n')))
            


#fillTable_End

#Entry_Point
fileName = input("Enter tic tac toe file name [include .txt]: ")
fillboard(fileName)
print("Finished!")
#Entry_Point_End
