import tkinter as tk
from tkinter import messagebox
from math import inf as infinity
from random import choice

# Constants for the players
HUMAN = -1
COMP = +1

# Initialize the board
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

# Global variables for the game
player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]


def evaluate(state):
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0
    return score


def wins(state, player):
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state


def game_over(state):
    return wins(state, HUMAN) or wins(state, COMP)


def empty_cells(state):
    cells = [[i, j] for i in range(3) for j in range(3) if state[i][j] == 0]
    return cells


def valid_move(x, y):
    return [x, y] in empty_cells(board)


def set_move(x, y, player):
    if valid_move(x, y):
        board[x][y] = player
        return True
    return False


def minimax(state, depth, alpha, beta, player):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, alpha, beta, -player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score
            alpha = max(alpha, score[2])
        else:
            if score[2] < best[2]:
                best = score
            beta = min(beta, score[2])

        if beta <= alpha:
            break

    return best


def btn_click(btn, x, y):
    global player

    if board[x][y] == 0:
        btn["text"] = player
        set_move(x, y, HUMAN)
        
        if game_over(board):
            messagebox.showinfo("Game Over", "You win!")
            reset_game()
        elif len(empty_cells(board)) == 0:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            ai_turn()


def ai_turn():
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    move = minimax(board, depth, -infinity, infinity, COMP)
    x, y = move[0], move[1]

    set_move(x, y, COMP)
    buttons[x][y]["text"] = "O"

    if game_over(board):
        messagebox.showinfo("Game Over", "You lose!")
        reset_game()
    elif len(empty_cells(board)) == 0:
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game()


def reset_game():
    global board, player
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = " "


# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons and add them to the grid
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=3,
                                  command=lambda i=i, j=j: btn_click(buttons[i][j], i, j))
        buttons[i][j].grid(row=i, column=j)

# Start the main loop
root.mainloop()
