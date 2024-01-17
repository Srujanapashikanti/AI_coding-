import math

def print_board(board):
    symbols = {0: '', 1: 'X', -1: 'O'}
    for row in board:
        row_str = [symbols[cell] for cell in row]
        print("|".join(row_str))
        print("-----")

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != 0 for row in board for cell in row)

def get_empty_cells(board):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                empty_cells.append((i, j))
    return empty_cells

def minimax(board, depth, is_maximizing, alpha, beta):
    scores = {1: 1, -1: -1, 0: 0}

    if is_winner(board, 1):
        return scores[1]
    if is_winner(board, -1):
        return scores[-1]
    if is_draw(board):
        return scores[0]

    if is_maximizing:
        max_score = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = 1
            score = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = 0
            max_score = max(max_score, score)
            alpha = max(alpha, max_score)
            if beta <= alpha:
                break
        return max_score
    else:
        min_score = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = -1
            score = minimax(board, depth + 1, True, alpha, beta)
            board[i][j] = 0
            min_score = min(min_score, score)
            beta = min(beta, min_score)
            if beta <= alpha:
                break
        return min_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 1
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[i][j] = 0
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    while True:
        print_board(board)
        
        if is_winner(board, 1):
            print("AI wins!")
            break
        if is_winner(board, -1):
            print("Human wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        if len(get_empty_cells(board)) % 2 == 0:
            i, j = find_best_move(board)
            board[i][j] = 1
        else:
            move = input("Enter your move (row[0-2] column[0-2]): ")
            i, j = map(int, move.split())
            
            if board[i][j] == 0:
                board[i][j] = -1
            else:
                print("Cell already occupied. Try again.")

if __name__ == "__main__":
    main()
