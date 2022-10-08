import numpy as np
import math
import random
def create_board():
    return np.zeros((6,7))

def avail_row(board,col):
    for row in range(len(board)-1,-1,-1):
        if board[row][col] == 0:
            return row
    return

def is_col_valid(board,col):
    if avail_row(board,col) == None:
        return False
    else:
        return True
def valid_cols(board):
    cols = []
    for col in range(0,len(board[0])):
        if is_col_valid(board,col):
            cols += [col]
    return cols

def drop_piece(board,col,piece):
    # 1 red, -1 yellow
    new_board = np.copy(board)
    if piece != 1 and piece != -1:
            return False
    row = avail_row(new_board,col)
    if row != None:
        new_board[row][col] = piece
        return new_board
    else:
        return False

def check_win(board):
    # horizontal
    for row in range(0,len(board)):
            for col in range(0,len(board[row])):
                if col<=3:
                    if board[row][col]!=0 and board[row][col] == board[row][col+1] and board[row][col+1] == \
                            board[row][col+2] and board[row][col+2] == board[row][col+3]:
                        return int(board[row][col])
                if row<=2:
                    if board[row][col] != 0 and board[row][col] == board[row+1][col] and board[row+1][col] == \
                            board[row+2][col] and board[row+2][col] == board[row+3][col]:
                        return int(board[row][col])
                if col<=3 and row<=2:
                    if board[row][col] != 0 and board[row][col] == board[row+1][col+1] and board[row+1][col+1] == \
                            board[row+2][col+2] and board[row+2][col+2] == board[row+3][col+3]:
                        return int(board[row][col])
                if col>=3 and row<=2:
                    if board[row][col] != 0 and board[row][col] == board[row+1][col-1] and board[row+1][col-1] == \
                            board[row+2][col-2] and board[row+2][col-2] == board[row+3][col-3]:
                        return int(board[row][col])
    return 0

def check_tie(board):

    r = check_win(board)
    if r!=0:
        return False
    for row in board:
        for col in row:
            if col==0:
                return False
    return True


def eval_domain(domain): # Positive For Player 1
    """
    score = 0
    if np.array_equal(domain, np.array([1,1,1,1])):
        score+=1000
    if np.array_equal(domain, np.array([0,1,1,1])):
        score+=80
    if np.array_equal(domain, np.array([1,1,1,0])):
        score+=80
    if np.array_equal(domain, np.array([0,1,1,0])):
        score += 5
    if np.array_equal(domain, np.array([0,0,1,1])):
        score+=5
    if np.array_equal(domain, np.array([1,1,0,0])):
        score += 5

    if np.array_equal(domain, np.array([-1,-1,-1,-1])):
        score-=1000
    if np.array_equal(domain, np.array([0,-1-1,-1])):
        score-=80
    if np.array_equal(domain, np.array([-1,-1,-1,0])):
        score-=80
    if np.array_equal(domain, np.array([0,-1,-1,0])):
        score -= 5
    if np.array_equal(domain, np.array([0,0,-1,-1])):
        score -= 5
    if np.array_equal(domain, np.array([-1,-1,0,0])):
        score -= 5
    return score
    """
    score = 0
    opp_piece = -1
    piece = 1
    EMPTY = 0
    if np.array_equal(domain, np.array([1,1,1,1])):
        score += 100
    elif np.array_equal(domain, np.array([0,1,1,1])) or np.array_equal(domain, np.array([1,1,1,0])):
        score += 5
    elif np.array_equal(domain, np.array([0,1,1,0])) or np.array_equal(domain, np.array([1,1,0,0])) or np.array_equal(domain, np.array([0,0,1,1])):
        score += 2
    if np.array_equal(domain, np.array([-1,-1,-1,-1])):
        score -= 100
    elif np.array_equal(domain, np.array([0,-1,-1,-1])) or np.array_equal(domain, np.array([-1,-1,-1,0])):
        score -= 5
    elif np.array_equal(domain, np.array([0,-1,-1,0])) or np.array_equal(domain, np.array([-1,-1,0,0])) or np.array_equal(domain, np.array([0,0,-1,-1])):
        score -= 2

    return score

def eval_board(board): # return scores for player 1
    """
    score = 0

    # center columns, 2,3,4th
    column2 = []
    column3 = []
    column4 = []
    for i in board:
        column2 += [i[2]]
        column3 += [i[3]]
        column4 += [i[4]]

    score += (column2.count(1)+column3.count(1)+column4.count(1))


    for i in range(0, 3):
        score += 2 * eval_domain(column2[i:i + 4])
        score += 2 * eval_domain(column3[i:i + 4])
        score += 2 * eval_domain(column4[i:i + 4])

    # score for rows
    for i in range(0,len(board)):
        for j in range(0,4):
            score += eval_domain(board[i][j:j+4])

    #score for side-columns
    column0 = []
    column1 = []
    column5 = []
    column6 = []
    for i in board:
        column0 += [i[0]]
        column1 += [i[1]]
        column5 += [i[5]]
        column6 += [i[6]]
    for i in range(0,3):
        score += eval_domain(column0[i:i + 4])
        score += eval_domain(column1[i:i + 4])
        score += eval_domain(column5[i:i + 4])
        score += eval_domain(column6[i:i + 4])

    # diagonal score
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if col <= 3 and row <= 2:
                pos_diag = [board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]]
                score += eval_domain(pos_diag)

            if col >= 3 and row <= 2:
                neg_diag = [board[row][col], board[row+1][col-1], board[row+2][col-2], board[row+3][col-3]]
                score += eval_domain(neg_diag)
    return score
    """
    score = 0
    COLUMN_COUNT = 7
    ROW_COUNT = 6
    WINDOW_LENGTH = 4
    piece = 1
    ## Score center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    ## Score Horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT - 3):
            window = row_array[c:c + WINDOW_LENGTH]
            score += eval_domain(window)

    ## Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - 3):
            window = col_array[r:r + WINDOW_LENGTH]
            score += eval_domain(window)

    ## Score posiive sloped diagonal
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += eval_domain(window)

    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
            score += eval_domain(window)

    return score

def minimax(board, depth, alpha, beta, maximizingPlayer): # computer is 1, player is -1
    valid_locations = valid_cols(board)  # 可以走的列的集合 [1...6] [4,6,1,2,0,3..]
    random.shuffle(valid_locations)
    is_terminal = check_win(board) or check_tie(board) # 有没有结束
    if depth == 0 or is_terminal:
        if is_terminal:
            if check_win(board)==1: # 代表电脑赢
                return (None, 1000000)
            elif check_win(board)==-1:
                return (None, -1000000)
            else:  # Game is over, no more valid moves
                return (None, 0)
        else:  # Depth is zero
            return (None, eval_board(board)) # 返回score
    if maximizingPlayer: # 如果没有停下来，如果
        value = -100000
        column = valid_locations[0]
        for col in valid_locations:
            #row = avail_row(board, col)
            b_copy = board.copy()
            b_copy = drop_piece(b_copy, col, 1)
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1] # 递归
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:  # Minimizing player
        value = 10000
        column = valid_locations[0]
        for col in valid_locations:
            #row = avail_row(board, col)
            b_copy = board.copy()
            b_copy = drop_piece(b_copy, col, -1)
            new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col

            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


"""
b = create_board()
print(b)

while True:
    col = int(input("Which Col For you>> "))
    b = drop_piece(b,col,-1)

    if check_win(b) == -1:
        print("You win")
        break
    col, minimax_score = minimax(b,50,-math.inf,math.inf,True)
    print(minimax_score)
    b = drop_piece(b, col, 1)
    print(b)
    if check_win(b) == 1:
        print("1 wins")
        break
"""
