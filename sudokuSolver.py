"""Sudoku Solver"""

#change the board here.
board = [
    [6,5,0,0,3,0,0,7,9],
    [0,0,0,0,0,8,0,0,2],
    [0,0,1,0,6,0,5,0,0],
    [0,0,6,4,2,0,0,1,0],
    [1,7,9,0,0,0,0,0,0],
    [0,0,4,0,1,0,0,0,7],
    [0,1,0,0,0,9,0,2,6],
    [0,0,0,8,0,0,0,0,5],
    [0,0,7,0,0,0,0,9,0],
]

def solver (Board: list) :
    pos = getEmpty(Board)
    if not pos : return True #if can't find the empty then it's done
    
    for i in range(1,9+1) : # try 1 to 9 
        if isValid(Board,i,pos) :
            Board[pos[0]][pos[1]] = i
            
            if solver(Board) :
                return True
            
            #if the next pos can't possible then set self to empty agian
            Board[pos[0]][pos[1]] = 0
            
    return False
    

def isValid (Board: list, num: int, pos: tuple):
    """Check is number is valid for the board in position"""
    
    #Check Column
    for i in range(len(Board[0])): #not matter which row, every row is the same length.
        if Board[pos[0]][i] == num and i != pos[1]:
            return False
        
    #Check Row
    for i in range(len(Board[0])):
        if Board[i][pos[1]] == num and i != pos[0] :
            return False
    #Check Block
    """
    block
    |  0,0  |  0,1  |  0,2  |
    |  0,0  |  1,1  |  1,2  |
    |  0,0  |  2,1  |  2,2  |
    """
    block_x = pos[0] // 3         
    block_y = pos[1] // 3    
    
    for i in range(block_x * 3, block_x * 3 + 3):
        for j in range(block_y * 3, block_y * 3 + 3):
            if Board[i][j] == num and (i,j) != pos :
                return False
    
    return True
    
def showBoard (Board: list) :
    """Print visual Board to console"""
    for i in range(len(Board)):
        if i % 3 == 0 :
            print("- - - - - - - - - - - - -")
        for j in range(len(Board)):
            if j == 8 :
                print(Board[i][j], end= " |\n")
            elif j == 0 or (j % 3 == 0 and j != 0):
                print( "| "+ str(Board[i][j]), end=" ")
            else :
                print(Board[i][j], end=" ")
    print("- - - - - - - - - - - - -")

def getEmpty (Board: list) :
    """return Position of empty value else None"""
    for i in range(len(Board)):
        for j in range(len(Board)):
            if Board[i][j] == 0 :
                return (i,j) #row,column
    return None
print("Board :")
showBoard(board)
solver(board)
print("solve :")
showBoard(board)