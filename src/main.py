import os
import random
import time
import json

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'user_data.json')

def load_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r') as file:
            return json.load(file)
    return {"klasse": 3, "coins": 0}

def save_data(data):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, 'w') as file:
        json.dump(data, file)

def main():
    user_data = load_data()
    clear_console()

    print(f'Willkommen! Deine aktuelle Klasse ist {user_data["klasse"]} und du hast {user_data["coins"]} Münzen.')
    print('\nIn welcher Klasse bist du?\n')
    print('1. Klasse 3')
    print('2. Klasse 4')

    choice = input()

    if choice == '1':
        confirm_class(3, user_data)
    elif choice == '2':
        confirm_class(4, user_data)
    else:
        print('Ungültige Auswahl. Bitte versuche es erneut.')
        time.sleep(1)
        main()

def confirm_class(klasse, user_data):
    print(f'Du bist in der {klasse}. Klasse (ja/nein)?')
    confirmation = input().lower()

    if confirmation in ['j', 'ja']:
        user_data['klasse'] = klasse
        print('Super, fangen wir an!')
        clear_console()
        menu(user_data)
    else:
        main()

def menu(user_data):
    clear_console()
    print(f'Was möchtest du tun? (Münzen: {user_data["coins"]})\n')
    print('1. Lernen')
    print('2. Spielen')
    print('3. Klasse ändern')
    print('4. Beenden')

    choice = input()

    if choice == '1':
        choose_difficulty(user_data)
    elif choice == '2':
        games(user_data)
    elif choice == '3':
        main()
    elif choice == '4':
        save_data(user_data)
        clear_console()
        quit()
    else:
        print('Ungültige Auswahl. Bitte versuche es erneut.')
        time.sleep(1)
        menu(user_data)

def choose_difficulty(user_data):
    clear_console()
    print('Wähle den Schwierigkeitsgrad:\n')
    print('1. Leicht')
    print('2. Normal')
    print('3. Schwer')

    choice = input()
    if choice == '1':
        learning(user_data, 'leicht')
    elif choice == '2':
        learning(user_data, 'normal')
    elif choice == '3':
        learning(user_data, 'schwer')
    else:
        print('Ungültige Auswahl. Bitte versuche es erneut.')
        time.sleep(1)
        choose_difficulty(user_data)

def learning(user_data, difficulty):
    clear_console()
    klasse = user_data['klasse']
    print(f"Du lernst jetzt Aufgaben der {klasse}. Klasse mit dem Schwierigkeitsgrad: {difficulty}\n")

    print('Löse 5 Aufgaben in jeder Kategorie: Addition, Subtraktion, Multiplikation, Division.')
    print('Du hast 5 Leben. Bei null verlierst du. Für jede richtige Antwort bekommst du eine Münze!\n')
    lives = 5

    for _ in range(5):
        if lives == 0:
            print('Du hast verloren.')
            break
        lives, user_data['coins'] = math_problems(lives, user_data['coins'], klasse, difficulty)
    
    print(f'Du hast {user_data["coins"]} Münzen gesammelt.')
    time.sleep(2)
    menu(user_data)

def math_problems(lives, coins, klasse, difficulty):
    clear_console()
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)

    if klasse == 3:
        if difficulty == 'leicht':
            zahl_1 = random.randint(1, 10)
            zahl_2 = random.randint(1, 10)
        elif difficulty == 'normal':
            zahl_1 = random.randint(10, 50)
            zahl_2 = random.randint(1, 50)
        else:
            zahl_1 = random.randint(50, 100)
            zahl_2 = random.randint(10, 50)
    else:
        if difficulty == 'leicht':
            zahl_1 = random.randint(10, 50)
            zahl_2 = random.randint(1, 10)
        elif difficulty == 'normal':
            zahl_1 = random.randint(50, 100)
            zahl_2 = random.randint(1, 50)
        else:
            zahl_1 = random.randint(100, 500)
            zahl_2 = random.randint(10, 100)

    if operation == '+':
        result = zahl_1 + zahl_2
        print(f'{zahl_1} + {zahl_2} = ?')
    elif operation == '-':
        result = zahl_1 - zahl_2
        print(f'{zahl_1} - {zahl_2} = ?')
    elif operation == '*':
        result = zahl_1 * zahl_2
        print(f'{zahl_1} * {zahl_2} = ?')
    elif operation == '/':
        zahl_1 = zahl_1 * zahl_2
        result = zahl_1 // zahl_2
        print(f'{zahl_1} / {zahl_2} = ?')

    answer = input()

    if answer.isdigit() and int(answer) == result:
        print('Richtig!')
        coins += 1
    else:
        print(f'Falsch! Die richtige Antwort war {result}.')
        lives -= 1
    
    return lives, coins

def games(user_data):
    clear_console()
    if user_data['coins'] < 5:
        print('Nicht genug Münzen, um zu spielen.')
        menu(user_data)
    else:
        print('Was möchtest du spielen?')
        print('1. Tic Tac Toe')
        print('2. Noch ein Spiel')
        print('3. Zurück')

        choice = input()
        print()

        if choice == '1':
            print('Viel Spaß!')
            user_data['coins'] -= 5
            clear_console()
            print(f'Du hast jetzt noch {user_data["coins"]} Münzen!')
            time.sleep(2)
            game_1(user_data)
        
        elif choice == '2':
            print('Viel Spaß!')
            user_data['coins'] -= 5
            clear_console()
            print(f'Du hast jetzt noch {user_data["coins"]} Münzen!')
            time.sleep(2)
            game_2(user_data)

        elif choice == '3':
            clear_console()
            menu(user_data)
        
        else:
            print('Ungültige Eingabe.')
            time.sleep(1)
            games(user_data)

def game_1(user_data):
    board = [' ' for _ in range(9)]
    player = 'X'
    bot = 'O'

    def print_board():
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")

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
    print_board()

    while True:
        while True:
            try:
                move = int(input("Gib deine Zugposition (0-8) ein: "))
                if board[move] == ' ':
                    board[move] = player
                    break
                else:
                    print("Diese Position ist bereits belegt. Wähle eine andere.")
            except (ValueError, IndexError):
                print("Ungültige Eingabe. Bitte gib eine Zahl zwischen 0 und 8 ein.")

        print_board()

        if (winner := check_winner()) is not None:
            print(f"Glückwunsch! {winner} hat gewonnen!")
            time.sleep(2)
            menu(user_data)
            break
        if is_draw():
            print("Das Spiel endet unentschieden!")
            time.sleep(2)
            menu(user_data)
            break

        while True:
            bot_move = random.randint(0, 8)
            if board[bot_move] == ' ':
                board[bot_move] = bot
                break

        print("Der Bot hat seinen Zug gemacht:")
        print_board()

        if (winner := check_winner()) is not None:
            print(f"Der Bot hat gewonnen! {winner} gewinnt.")
            time.sleep(2)
            menu(user_data)
            break
        if is_draw():
            print("Das Spiel endet unentschieden!")
            time.sleep(2)
            menu(user_data)
            break

    # Warte 2 Sekunden und gehe zurück zum Menü
    time.sleep(2)
    menu(user_data)

def game_2(user_data):
    print("Dies ist ein weiteres Spiel!")
    # Hier kann der Code für ein weiteres Spiel eingefügt werden.

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
