import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell in ["X", "O"] for row in board for cell in row)

def get_empty_cells(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 10 - depth
    if check_winner(board, "X"):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = "O"
            score = minimax(board, depth + 1, False)
            board[r][c] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for r, c in get_empty_cells(board):
            board[r][c] = "X"
            score = minimax(board, depth + 1, True)
            board[r][c] = " "
            best_score = min(best_score, score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None
    for r, c in get_empty_cells(board):
        board[r][c] = "O"
        score = minimax(board, 0, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)

    while True:
        # Player's turn
        print("Your turn (X).")
        try:
            row, col = map(int, input("Enter row and column (0-2) separated by a space: ").split())
            if board[row][col] != " ":
                print("Cell already taken, go again")
                continue
        except (ValueError, IndexError):
            print("Not a valid input, please enter numbers between 0 and 2")
            continue

        board[row][col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("You are the winner")
            break
        if is_draw(board):
            print("It's a tie")
            break

        # Computer's turn
        print("Computer's turn (O).")
        move = find_best_move(board)
        if move:
            board[move[0]][move[1]] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("You Lose :()")
            break
        if is_draw(board):
            print("It's a tie")
            break

if __name__ == "__main__":
    tic_tac_toe()
