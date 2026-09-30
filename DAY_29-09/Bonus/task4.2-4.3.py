import random

EMPTY = "."
HUMAN = "X"
BOT = "O"
DIRECTIONS = [(0, 1), (1, 0), (1, 1), (1, -1)]   # right, down, diagonal \, diagonal /


def win_length(rows, cols):
    # Winning rule for any size: line up min(rows, cols, 4) marks
    return min(rows, cols, 4)


def show(board):
    cols = len(board[0])
    print("\n   " + "".join(f"{c + 1:>3}" for c in range(cols)))
    for r, row in enumerate(board):
        print(f"{r + 1:>3}" + "".join(f"{cell:>3}" for cell in row))


def has_won(board, p, k):
    # From every cell, look for k marks of p in a row in each direction
    rows, cols = len(board), len(board[0])
    for r in range(rows):
        for c in range(cols):
            for dr, dc in DIRECTIONS:
                count = 0
                for i in range(k):
                    rr, cc = r + dr * i, c + dc * i
                    if 0 <= rr < rows and 0 <= cc < cols and board[rr][cc] == p:
                        count += 1
                    else:
                        break
                if count == k:
                    return True
    return False


def free_cells(board):
    return [(r, c) for r, row in enumerate(board)
            for c, cell in enumerate(row) if cell == EMPTY]


def ask_move(board, player):
    rows, cols = len(board), len(board[0])
    while True:
        move = input(f"Player {player}, type row and column (e.g. 1 3): ").split()
        if len(move) != 2 or not all(m.isdigit() for m in move):
            print("Invalid move: type two numbers.")
            continue
        r, c = int(move[0]) - 1, int(move[1]) - 1
        if not (0 <= r < rows and 0 <= c < cols):
            print("Invalid move: out of the board.")
        elif board[r][c] != EMPTY:
            print("Invalid move: cell already taken.")
        else:
            return r, c


def minimax(board, turn, k):
    # Perfect play on small boards: +1 bot wins, -1 human wins, 0 draw
    if has_won(board, BOT, k):
        return 1
    if has_won(board, HUMAN, k):
        return -1
    cells = free_cells(board)
    if not cells:
        return 0
    scores = []
    for r, c in cells:
        board[r][c] = turn                        # try the move...
        scores.append(minimax(board, HUMAN if turn == BOT else BOT, k))
        board[r][c] = EMPTY                       # ...then undo it
    return max(scores) if turn == BOT else min(scores)


def bot_move(board, k):
    cells = free_cells(board)
    if len(board) * len(board[0]) <= 9:          # 3x3: unbeatable bot
        best_score, best = -2, None
        for r, c in cells:
            board[r][c] = BOT
            score = minimax(board, HUMAN, k)
            board[r][c] = EMPTY
            if score > best_score:
                best_score, best = score, (r, c)
        return best
    # Bigger boards: win if possible, else block the human, else random
    for p in (BOT, HUMAN):
        for r, c in cells:
            board[r][c] = p
            wins = has_won(board, p, k)
            board[r][c] = EMPTY
            if wins:
                return r, c
    return random.choice(cells)


def tictactoe(rows, cols, players):
    k = win_length(rows, cols)
    print(f"\nRule: line up {k} marks in a row (horizontal, vertical or diagonal).")
    board = [[EMPTY] * cols for _ in range(rows)]
    player = HUMAN

    while True:
        show(board)
        if player == BOT and players == 1:
            r, c = bot_move(board, k)
            print(f"Bot plays {r + 1} {c + 1}")
        else:
            r, c = ask_move(board, player)
        board[r][c] = player

        if has_won(board, player, k):
            show(board)
            print(f"Player {player} wins!")
            return
        if not free_cells(board):
            show(board)
            print("It's a draw!")
            return
        player = BOT if player == HUMAN else HUMAN


def ask_number(question, allowed):
    while True:
        answer = input(question)
        if answer.isdigit() and int(answer) in allowed:
            return int(answer)
        print("Invalid answer.")


while True:
    players = ask_number("How many players? (1 or 2): ", [1, 2])
    rows = ask_number("Number of rows (3-10): ", range(3, 11))
    cols = ask_number("Number of columns (3-10): ", range(3, 11))
    tictactoe(rows, cols, players)
    if input("Play again? (y/n): ").strip().lower() != "y":
        break