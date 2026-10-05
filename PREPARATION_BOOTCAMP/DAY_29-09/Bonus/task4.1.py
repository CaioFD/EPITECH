def show(board):
    print("\n  1 2 3")
    for i, row in enumerate(board):
        print(i + 1, " ".join(row))


def has_won(board, p):
    lines = []
    lines += board                                               # 3 rows
    lines += [[board[l][c] for l in range(3)] for c in range(3)] # 3 columns
    lines.append([board[i][i] for i in range(3)])                # diagonal \
    lines.append([board[i][2 - i] for i in range(3)])            # diagonal /
    return any(all(cell == p for cell in line) for line in lines)


def is_full(board):
    return all(cell != "." for row in board for cell in row)

board = [["."] * 3 for _ in range(3)]
player = "X"

while True:
    show(board)
    move = input(f"Player {player}, type row and column (Example:. 1 3): ").split()

    if len(move) != 2 or not all(m.isdigit() for m in move):
        print("Invalid move: type two numbers.")
        continue
    l, c = int(move[0]) - 1, int(move[1]) - 1        # the player counts from 1
    if not (0 <= l < 3 and 0 <= c < 3):
        print("Invalid move: out of the board.")
        continue
    if board[l][c] != ".":
        print("Invalid move: cell already taken.")
        continue

    board[l][c] = player
    if has_won(board, player):
        show(board)
        print(f"Player {player} wins!")
        break
    if is_full(board):
        show(board)
        print("It's a draw!")
        break
    player = "O" if player == "X" else "X"          # next player