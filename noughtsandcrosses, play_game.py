import random
import os.path
import json
random.seed()

def draw_board(board):
    print(" {} | {} | {} ".format(board[0][0], board[0][1], board[0][2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[1][0], board[1][1], board[1][2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[2][0], board[2][1], board[2][2]))

def welcome(board):
    print("Welcome to Tic Tac Toe")
    draw_board(board)

def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board

def get_player_move(board):
    row = int(input("Enter row (0, 1, 2): "))
    col = int(input("Enter col (0, 1, 2): "))
    board[row][col] = 'X'
    return row, col

def choose_computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return row, col

def check_for_win(board, mark):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)],
    ]
    for win_condition in win_conditions:
        if all(board[row][col] == mark for row, col in win_condition):
            return True
    return False

board = [[' ' for x in range(3)] for y in range(3)]
welcome(board)
initialise_board(board)
while True:
    row, col = get_player_move(board)
    draw_board(board)
    if check_for_win(board, 'X'):
        print("Player wins!")
        break
    row, col = choose_computer_move(board)
    print("Computer chose: ({}, {})".format(row, col))
    draw_board(board)
    if check_for_win(board, 'O'):
        print("Computer wins!")
        break
    
def check_for_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def play_game(board):
    initialise_board(board)
    draw_board(board)
    while True:
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            return 1
        if check_for_draw(board):
            return 0
        computer_row, computer_col = choose_computer_move(board)
        board[computer_row][computer_col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            return -1
        if check_for_draw(board):
            return 0

def menu():
    choice = input("Enter either '1', '2', '3' or 'q': ")
    return choice

def load_scores():
    leaders = {}
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r") as file:
            leaders = json.load(file)
    else:
        print("File 'leaderboard.json' not found.")
    return leaders

def save_score(score):
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open("leaderboard.json", "w") as file:
        json.dump(leaders, file, indent=4)
    return

def display_leaderboard(leaders):
    for name, score in leaders.items():
        print(f"{name}: {score}")
        
def main():
    while True:
        choice = menu()
        if choice == '1':
            result = play_game(board)
            if result == 1:
                save_score(1)
            elif result == -1:
                save_score(-1)
        elif choice == '2':
            display_leaderboard(load_scores())
        elif choice == '3':
            leaders = load_scores()
            leaders = {k: v for k, v in sorted(leaders.items(), key=lambda item: item[1], reverse=True)}
            display_leaderboard(leaders)
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
