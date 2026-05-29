```python
import math
import random
import copy

EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

# -----------------------------
# Tic Tac Toe Utility Functions
# -----------------------------

def print_board(board):

    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board):

    # Rows
    for row in board:

        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]

    # Columns
    for col in range(3):

        if (
            board[0][col] ==
            board[1][col] ==
            board[2][col]
            and board[0][col] != EMPTY
        ):
            return board[0][col]

    # Diagonals

    if (
        board[0][0] ==
        board[1][1] ==
        board[2][2]
        and board[0][0] != EMPTY
    ):
        return board[0][0]

    if (
        board[0][2] ==
        board[1][1] ==
        board[2][0]
        and board[0][2] != EMPTY
    ):
        return board[0][2]

    return None


def is_full(board):

    for row in board:

        if EMPTY in row:
            return False

    return True


def available_moves(board):

    moves = []

    for i in range(3):

        for j in range(3):

            if board[i][j] == EMPTY:
                moves.append((i, j))

    return moves


# -----------------------------
# Minimax Algorithm
# -----------------------------

def minimax(board, is_maximizing):

    winner = check_winner(board)

    if winner == PLAYER_X:
        return 1

    elif winner == PLAYER_O:
        return -1

    elif is_full(board):
        return 0

    if is_maximizing:

        best_score = -math.inf

        for move in available_moves(board):

            i, j = move

            board[i][j] = PLAYER_X

            score = minimax(board, False)

            board[i][j] = EMPTY

            best_score = max(score, best_score)

        return best_score

    else:

        best_score = math.inf

        for move in available_moves(board):

            i, j = move

            board[i][j] = PLAYER_O

            score = minimax(board, True)

            board[i][j] = EMPTY

            best_score = min(score, best_score)

        return best_score


# -----------------------------
# Alpha Beta Pruning
# -----------------------------

def alpha_beta(board, depth, alpha, beta, maximizing):

    winner = check_winner(board)

    if winner == PLAYER_X:
        return 1

    elif winner == PLAYER_O:
        return -1

    elif is_full(board):
        return 0

    if maximizing:

        value = -math.inf

        for move in available_moves(board):

            i, j = move

            board[i][j] = PLAYER_X

            value = max(
                value,
                alpha_beta(
                    board,
                    depth + 1,
                    alpha,
                    beta,
                    False
                )
            )

            board[i][j] = EMPTY

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for move in available_moves(board):

            i, j = move

            board[i][j] = PLAYER_O

            value = min(
                value,
                alpha_beta(
                    board,
                    depth + 1,
                    alpha,
                    beta,
                    True
                )
            )

            board[i][j] = EMPTY

            beta = min(beta, value)

            if beta <= alpha:
                break

        return value


# -----------------------------
# Heuristic Evaluation
# -----------------------------

def heuristic(board):

    winner = check_winner(board)

    if winner == PLAYER_X:
        return 10

    if winner == PLAYER_O:
        return -10

    return 0


def heuristic_alpha_beta(
        board,
        depth,
        alpha,
        beta,
        maximizing,
        max_depth):

    score = heuristic(board)

    if abs(score) == 10 or is_full(board) or depth == max_depth:
        return score

    if maximizing:

        best = -math.inf

        for move in available_moves(board):

            i, j = move

            board[i][j] = PLAYER_X

            best = max(
                best,
                heuristic_alpha_beta(
                    board,
                    depth + 1,
                    alpha,
                    beta,
                    False,
                    max_depth
                )
            )

            board[i][j] = EMPTY

            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:

        best = math.inf

        for move in available_moves(board):

            i, j = move

            board[i][j] = PLAYER_O

            best = min(
                best,
                heuristic_alpha_beta(
                    board,
                    depth + 1,
                    alpha,
                    beta,
                    True,
                    max_depth
                )
            )

            board[i][j] = EMPTY

            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


# -----------------------------
# Monte Carlo Tree Search
# -----------------------------

def random_playout(board, player):

    temp_board = copy.deepcopy(board)

    current_player = player

    while True:

        winner = check_winner(temp_board)

        if winner == PLAYER_X:
            return 1

        elif winner == PLAYER_O:
            return -1

        elif is_full(temp_board):
            return 0

        move = random.choice(
            available_moves(temp_board)
        )

        i, j = move

        temp_board[i][j] = current_player

        current_player = (
            PLAYER_O
            if current_player == PLAYER_X
            else PLAYER_X
        )


def monte_carlo_tree_search(
        board,
        player,
        simulations=100):

    best_move = None
    best_score = -math.inf

    for move in available_moves(board):

        total_score = 0

        for _ in range(simulations):

            temp_board = copy.deepcopy(board)

            i, j = move

            temp_board[i][j] = player

            score = random_playout(
                temp_board,
                PLAYER_O
                if player == PLAYER_X
                else PLAYER_X
            )

            total_score += score

        if total_score > best_score:

            best_score = total_score
            best_move = move

    return best_move


# -----------------------------
# Main Program
# -----------------------------

if __name__ == "__main__":

    board = [

        ["X", "O", "X"],
        [" ", "O", " "],
        [" ", " ", "X"]
    ]

    print("Current Board:")

    print_board(board)

    print(
        "\nMinimax Score:",
        minimax(board, True)
    )

    print(
        "Alpha-Beta Score:",
        alpha_beta(
            board,
            0,
            -math.inf,
            math.inf,
            True
        )
    )

    print(
        "Heuristic Alpha-Beta Score:",
        heuristic_alpha_beta(
            board,
            0,
            -math.inf,
            math.inf,
            True,
            3
        )
    )

    print(
        "MCTS Best Move:",
        monte_carlo_tree_search(
            board,
            PLAYER_X
        )
    )
```
