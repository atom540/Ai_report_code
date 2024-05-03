player, opponent = 'x', 'o'
nodes_evaluated_minimax = 0  # Global variable to count the number of nodes evaluated in minimax
nodes_evaluated_alpha_beta = 0  # Global variable to count the number of nodes evaluated in alpha-beta pruning

# This function returns true if there are moves remaining on the board. It returns false if there are no moves left to play.
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False

def evaluate(b):
    # Checking for Rows for X or O victory.
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == player):
                return 10
            elif (b[row][0] == opponent):
                return -10
    # Checking for Columns for X or O victory.
    for col in range(3):
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
            if (b[0][col] == player):
                return 10
            elif (b[0][col] == opponent):
                return -10
    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if (b[0][0] == player):
            return 10
        elif (b[0][0] == opponent):
            return -10
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        if (b[0][2] == player):
            return 10
        elif (b[0][2] == opponent):
            return -10
    # Else if none of them have won then return 0
    return 0

# This is the minimax function. It considers all the possible ways the game can go and returns the value of the board
def minimax(board, depth, isMax):
    global nodes_evaluated_minimax
    score = evaluate(board)
    # If Maximizer has won the game return his/her evaluated score
    if (score == 10):
        return score
    # If Minimizer has won the game return his/her evaluated score
    if (score == -10):
        return score
    # If there are no more moves and no winner then it is a tie
    if (isMovesLeft(board) == False):
        return 0
    # If this maximizer's move
    if (isMax):
        best = -1000
        # Traverse all cells
        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if (board[i][j] == '_'):
                    # Make the move
                    board[i][j] = player
                    nodes_evaluated_minimax += 1  # Increment the node count for minimax
                    # Call minimax recursively and choose the maximum value
                    best = max(best, minimax(board, depth + 1, not isMax))
                    # Undo the move
                    board[i][j] = '_'
        return best
    # If this minimizer's move
    else:
        best = 1000
        # Traverse all cells
        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if (board[i][j] == '_'):
                    # Make the move
                    board[i][j] = opponent
                    nodes_evaluated_minimax += 1  # Increment the node count for minimax
                    # Call minimax recursively and choose the minimum value
                    best = min(best, minimax(board, depth + 1, not isMax))
                    # Undo the move
                    board[i][j] = '_'
        return best

# This is the alpha-beta pruning function.
def alpha_beta_pruning(board, depth, alpha, beta, isMax):
    global nodes_evaluated_alpha_beta
    score = evaluate(board)
    # If Maximizer has won the game return his/her evaluated score
    if (score == 10):
        return score
    # If Minimizer has won the game return his/her evaluated score
    if (score == -10):
        return score
    # If there are no more moves and no winner then it is a tie
    if (isMovesLeft(board) == False):
        return 0
    # If this maximizer's move
    if (isMax):
        best = -1000
        # Traverse all cells
        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if (board[i][j] == '_'):
                    # Make the move
                    board[i][j] = player
                    nodes_evaluated_alpha_beta += 1  # Increment the node count for alpha-beta pruning
                    # Call alpha-beta pruning recursively and choose the maximum value
                    best = max(best, alpha_beta_pruning(board, depth + 1, alpha, beta, not isMax))
                    # Undo the move
                    board[i][j] = '_'
                    alpha = max(alpha, best)
                    if alpha >= beta:
                        break
        return best
    # If this minimizer's move
    else:
        best = 1000
        # Traverse all cells
        for i in range(3):
            for j in range(3):
                # Check if cell is empty
                if (board[i][j] == '_'):
                    # Make the move
                    board[i][j] = opponent
                    nodes_evaluated_alpha_beta += 1  # Increment the node count for alpha-beta pruning
                    # Call alpha-beta pruning recursively and choose the minimum value
                    best = min(best, alpha_beta_pruning(board, depth + 1, alpha, beta, not isMax))
                    # Undo the move
                    board[i][j] = '_'
                    beta = min(beta, best)
                    if alpha >= beta:
                        break
        return best

# This will return the best possible move for the player using minimax
def findBestMove_minimax(board):
    global nodes_evaluated_minimax
    bestVal = -1000
    bestMove = (-1, -1)
    # Traverse all cells, evaluate minimax function for all empty cells. And return the cell with optimal value.
    for i in range(3):
        for j in range(3):
            # Check if cell is empty
            if (board[i][j] == '_'):
                # Make the move
                board[i][j] = player
                # compute evaluation function for this move.
                moveVal = minimax(board, 0, False)
                # Undo the move
                board[i][j] = '_'
                # If the value of the current move is more than the best value, then update best.
                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal
    print("Number of nodes evaluated in minimax:", nodes_evaluated_minimax)
    return bestMove

# This will return the best possible move for the player using alpha-beta pruning
def findBestMove_alpha_beta(board):
    global nodes_evaluated_alpha_beta
    bestVal = -1000
    bestMove = (-1, -1)
    alpha = -1000
    beta = 1000
    # Traverse all cells, evaluate alpha-beta pruning function for all empty cells. And return the cell with optimal value.
    for i in range(3):
        for j in range(3):
            # Check if cell is empty
            if (board[i][j] == '_'):
                # Make the move
                board[i][j] = player
                # compute evaluation function for this move.
                moveVal = alpha_beta_pruning(board, 0, alpha, beta, False)
                # Undo the move
                board[i][j] = '_'
                # If the value of the current move is more than the best value, then update best.
                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal
    print("Number of nodes evaluated in alpha-beta pruning:", nodes_evaluated_alpha_beta)
    return bestMove

print("Minimax:")

# Driver code
board = [
    ['X', 'X', 'O'],
    ['X', '', ''],
    ['','O','']
]
bestMove_minimax = findBestMove_minimax(board)


print("\nAlpha-Beta Pruning:")
bestMove_alpha_beta = findBestMove_alpha_beta(board)

