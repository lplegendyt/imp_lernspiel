import os
import random
import time
from utils.ui_helpers import clear_console

def games(user_data):
    clear_console()
    if user_data['coins'] < 5:
        print("Nicht genug Münzen, um zu spielen.")
        return

    print("Was möchtest du spielen?")
    print("1. Tic Tac Toe")
    print("2. Zurück")

    choice = input("\nWähle eine Option: ")

    if choice == '1':
        clear_console()
        user_data['coins'] -= 5
        print(f"Du spielst Tic Tac Toe! (Münzen: {user_data['coins']})\n")
        tic_tac_toe(user_data)
    elif choice == '2':
        return
    else:
        print("Ungültige Eingabe.")
        time.sleep(1)
        games(user_data)


def tic_tac_toe(user_data):
    board = [' ' for _ in range(9)]
    player = 'X'
    bot = 'O'

    # Visualisiertes Layout für Positionen
    positions = [str(i) for i in range(9)]

    def print_board():
        print("\nSpielfeld:")
        print(f"{board[0]} | {board[1]} | {board[2]}      {positions[0]} | {positions[1]} | {positions[3]}")
        print("--+---+--      ------------")
        print(f"{board[3]} | {board[4]} | {board[5]}      {positions[3]} | {positions[4]} | {positions[5]}")
        print("--+---+--      ------------")
        print(f"{board[6]} | {board[7]} | {board[8]}      {positions[6]} | {positions[7]} | {positions[8]}\n")

    def check_winner():
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
                return board[combo[0]]
        return None

    def is_draw():
        return ' ' not in board

    print("Willkommen zu Tic-Tac-Toe!")
    print("Du spielst als 'X' und der Bot spielt als 'O'.")
    print("Gib die Position (0-8) ein, um deinen Zug zu machen.")
    time.sleep(2)
    clear_console()

    print_board()

    while True:
        # Spielerzug
        while True:
            try:
                move = int(input("Gib deine Zugposition (0-8) ein: "))
                if 0 <= move <= 8 and board[move] == ' ':
                    board[move] = player
                    print("\nDein Zug:")
                    print_board()
                    break
                elif 0 <= move <= 8:
                    print("Diese Position ist bereits belegt. Wähle eine andere.")
                else:
                    print("Bitte wähle eine Zahl zwischen 0 und 8.")
            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 0 und 8 ein.")

        if (winner := check_winner()) is not None:
            print(f"🎉 Glückwunsch! {winner} hat gewonnen! 🎉")
            time.sleep(2)
            return
        if is_draw():
            print("Das Spiel endet unentschieden!")
            time.sleep(2)
            return

        # Botzug
        while True:
            bot_move = random.randint(0, 8)
            if board[bot_move] == ' ':
                board[bot_move] = bot
                break

        print("Der Bot hat seinen Zug gemacht:")
        print_board()

        if (winner := check_winner()) is not None:
            print(f"Der Bot hat gewonnen! 😞 {winner} hat gewonnen!")
            time.sleep(2)
            return
        if is_draw():
            print("Das Spiel endet unentschieden!")
            time.sleep(2)
            return

