"""Exercise 5.12-5-16. TicTacToe."""
def get_game_state(board: list) -> str:
    """Check if a player has won the game, if it's a draw, or if it's ongoing.

    :param board: List of lists of strings representing the game board.
    :return: A string which is 'X' if player 'X' won, 'O' if player 'O' has won, 'Draw' if the game is a draw, or '-' if the game is ongoing.
    """
    flat = [item for row in board for item in row]

    # Check win conditions
    # 0 1 2
    # 3 4 5
    # 6 7 8
    win_conditions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for t in win_conditions:
         if (flat[t[0]] != '-') and (flat[t[0]] == flat[t[1]] == flat[t[2]]):
             return flat[t[0]]
    if flat.count('-') > 0:
        return '-'
    return 'Draw'

def update_board(board : list, player: str, position: list) -> list:
    """Update the game board with the player's move.

    :param board: List of lists of strings representing the game board.
    :param player: Player making the move ('X' or 'O').
    :param position: List containing two integer indices [row, column] indicating the position to make a move.
    :return: Updated game board after the move.
    """
    if board[position[0]][position[1]] != '-':
        print("Invalid move!")
    else:
        board[position[0]][position[1]] = player
    return board

def print_board(board: list):
    """Print the current state of the game board.
    
    :param board: List of lists of strings representing the game board.
    """
    print('\n'.join((''.join(row) for row in board)))

def tictactoe(board: list, player: str, position: list) -> list:
    """Play a move in the Tic-Tac-Toe game and determine the winner.
    
    :param board: List of lists of strings representing the game board.
    :param player: Player making the move ('X' or 'O').
    :param position: List containing two integer indices [row, column] indicating the position to make a move.
    :return: Updated game board after the move.
    """
    board = update_board(board, player, position)
    print_board(board)
    state = get_game_state(board)
    if state == 'X' or state == 'O':
        print(f'Player {state} won!')
    elif state == 'Draw':
        print('Draw!')
    return board

def minimax(board: list, depth: int, maximizing: bool, player: str, opponent: str) -> int:
    score = get_game_state(board)
    if score == player:
        return 10 - depth
    if score == opponent:
        return depth - 10
    if score == 'Draw':
        return 0

    if maximizing:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not maximizing, player, opponent))
                    board[i][j] = '-'
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not maximizing, player, opponent))
                    board[i][j] = '-'
        return best

def find_best_move(board: list, player: str, opponent: str) -> list:
    best_val = -float('inf')
    best_move = [-1, -1]
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = player
                move_val = minimax(board, 0, False, player, opponent)
                print(f'Move {i},{j} has value {move_val}')
                board[i][j] = '-'
                if move_val > best_val:
                    best_move = [i, j]
                    best_val = move_val
    return best_move

def interactive_game():
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    player, opponent = 'X', 'O'
    print("Welcome to Tic-Tac-Toe! You are 'X'. Enter your move as 'row,col' where top left corner is 0,0")
    print_board(board)

    players = input("Enter number of players (0, 1, or 2): ")

    while True:
        move = input("Enter your move (or press Enter to let the computer start): ")
        
        if move:
            row, col = map(int, move.split(','))
            update_board(board, player, [row, col])
        else:
            print("Computer starts.")
        
        state = get_game_state(board)
        if state != '-':
            print(f"Game over: {state}")
            break
        
        print("Computer's move:")
        best_move = find_best_move(board, opponent, player)
        update_board(board, opponent, best_move)
        print_board(board)
        
        state = get_game_state(board)
        if state != '-':
            print(f"Game over: {state}")
            break


if __name__ == "__main__":
    interactive_game()
    # testcases = [ ('eval', "print_board([['X', 'X', 'X'], ['-', 'O', '-'], ['-', 'O', '-']])"),
    #               ('exec', "board = tictactoe([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']], 'X', [0, 1])"),
    #               ('exec', "board = tictactoe(board, 'O', [0, 2])"),
    #               ('exec', "board = tictactoe(board, 'X', [1, 0])"),
    #               ('exec', "board = tictactoe(board, 'O', [1, 1])"),
    #               ('exec', "board = tictactoe(board, 'X', [1, 1])"),
    #               ('exec', "board = tictactoe(board, 'X', [1, 2])"),
    #               ('exec', "board = tictactoe(board, 'O', [2, 0])")
    #             ]
    # prices = [3, 2, 1, 3, 5]
    # for t in testcases:
    #     if t[0] == 'eval':
    #         print(f'{t[1]}: {eval(t[1])}')
    #     elif t[0] == 'exec':
    #         print(f'Exec: {t[1]}')
    #         exec(t[1])
