```python id="l1fx5u"
import math
from search_algorithms import *

# ---------------------------------
# Test Minimax Algorithm
# ---------------------------------

def test_minimax():

    board = [

        ["X", "X", " "],
        ["O", "O", " "],
        [" ", " ", " "]
    ]

    score = minimax(board, True)

    print("Minimax Test Score:", score)


# ---------------------------------
# Test Alpha-Beta Algorithm
# ---------------------------------

def test_alpha_beta():

    board = [

        ["X", "O", "X"],
        ["O", "X", " "],
        [" ", " ", "O"]
    ]

    score = alpha_beta(
        board,
        0,
        -math.inf,
        math.inf,
        True
    )

    print("Alpha-Beta Test Score:", score)


# ---------------------------------
# Test Heuristic Alpha-Beta
# ---------------------------------

def test_heuristic():

    board = [

        ["X", " ", "O"],
        [" ", "X", " "],
        ["O", " ", " "]
    ]

    score = heuristic_alpha_beta(
        board,
        0,
        -math.inf,
        math.inf,
        True,
        3
    )

    print(
        "Heuristic Alpha-Beta Score:",
        score
    )


# ---------------------------------
# Test Monte Carlo Tree Search
# ---------------------------------

def test_mcts():

    board = [

        ["X", "O", " "],
        [" ", "X", " "],
        ["O", " ", " "]
    ]

    move = monte_carlo_tree_search(
        board,
        PLAYER_X
    )

    print("MCTS Best Move:", move)


# ---------------------------------
# Main Program
# ---------------------------------

if __name__ == "__main__":

    print("\nRunning Test Cases...\n")

    test_minimax()

    test_alpha_beta()

    test_heuristic()

    test_mcts()
```
