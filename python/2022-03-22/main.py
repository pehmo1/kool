import os

nrs = [".",".",".",".",".",".",".",".","."]
moveCount = 0
nextMove = "X"
while moveCount < 10:
    os.system("cls")
    print("""
    New table:
    {nr1} {nr2} {nr3}
    {nr4} {nr5} {nr6}
    {nr7} {nr8} {nr9}""".format(nr1=nrs[0],nr2=nrs[1],nr3=nrs[2],
    nr4=nrs[3],nr5=nrs[4],nr6=nrs[5],
    nr7=nrs[6],nr8=nrs[7],nr9=nrs[8]))

    nextSpot = int(input("""
    Next move: {nextMove} 
    1 2 3
    4 5 6
    7 8 9

    Select the next square: """.format(nextMove=nextMove)))
    nrs[nextSpot-1] = nextMove
    
    if nextMove == "X":
        nextMove = "O"
    else:
        nextMove == "X"
    moveCount += 1

    # Check if game over
    #if(nrs[])