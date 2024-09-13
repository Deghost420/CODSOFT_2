import math

board = [' ' for _ in range(9)]  

def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]             # Diagonal
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_board_full(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'X'):
        return 1 
    elif check_winner(board, 'O'):
        return -1 
    elif is_board_full(board):
        return 0  

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'X'

def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                raise ValueError
            if board[move] == ' ':
                board[move] = 'O'
                break
            else:
                print("Invalid move. Cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number from 1 to 9.")

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
      
        human_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        ai_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

play_game()
