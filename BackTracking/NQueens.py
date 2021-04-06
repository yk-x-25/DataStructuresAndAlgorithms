'''

How I represent the chessboard with queen

Column  [ 0 , 1 , 2 , 3 ] 
Row       0   1   2   3

i -> row arr[i] -> column

check for diag 
    |__||_Q||__||__|
    |__||__||__||_Q|
    |Q_||__||__||__|
    |__||__||_Q||__|
|r1-r2| = |r2-c2|

check for row  -> r1= r2
check for col -> c1=c2
'''

def DiagonnalCheck(r1,r2,c1,c2):
    return  abs(r1-r2)!=abs(c1-c2)

def SameColCheck(r1,r2,c1,c2):
    return  c1!=c2

def SameRowCheck(r1,r2,c1,c2):
    return  r1!=r2

def IsValidPostion(r1,c1,r2,c2):
    return DiagonnalCheck(r1,r2,c1,c2) and SameColCheck(r1,r2,c1,c2) and SameRowCheck(r1,r2,c1,c2)


def IsSafe(row,col,placedQueen):
    res = True
    # Check for valid position wrt all the queens placed above
    for i in range(row):
        res= res and IsValidPostion(i,placedQueen[i],row,col)
    return res
 
def representInBoard(res):
    length = len(res)
    noQueen =  "|__"
    Queen   =  "|Q_"
    rightBorder = "|"
    board= [[noQueen for _ in range(length)] for _ in range(length) ]

    for i in range(length):
        board[i][res[i]] =  Queen
    # UnComment for extra padding while usinng chessboard number representation 
    #print("  ",end="")
    
    print("___"*length)
    
    for i in range(length):
        # UnComment for chessboard number representation at the side
        #print(length-i,end="")
        for j in range(length):
            print(board[i][j],end= rightBorder if j==length-1 else "")
        print()
    
    
    # Uncommennt for chess board character representation at the bottom
    # print("  ",end="")
    # for i in range(length):
    #     print(" {} ".format(chr(97+i)),end="")
    # print()





def BackTrackAndFindPlace(n,depth,placedQueen):
    # We have placed All our queens at the right place !
    if depth >= n :
        return True
    
    for i in range(n):
        placedQueen[depth]=i
        # You need not check for validity of the first position    
        if depth ==0:
            if BackTrackAndFindPlace(n,depth+1,placedQueen):
                return True
        else:
            if  IsSafe(depth,i,placedQueen):
                if BackTrackAndFindPlace(n,depth+1,placedQueen):
                    return True
            #Not the right place reset the positionn
            placedQueen[depth]=0
    #Could not place the queen , step back and try other position
    return False

# Change here for simulating other nxn nqueens
n=9

placedQueen = [0 for _ in range(n)]
if BackTrackAndFindPlace(n,0,placedQueen):
    representInBoard(placedQueen)
else:
    print("impossible")

