import os
import random
import time
import json

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'user_data.json')

# Daten laden
def load_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r') as file:
            return json.load(file)
    return {"klasse": 3, "coins": 0}

# Daten speichern
def save_data(data):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, 'w') as file:
        json.dump(data, file)

# Hauptfunktion
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

# Klasse bestätigen und Menü starten
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

# Menü anzeigen
def menu(user_data):
    print(f'Was möchtest du tun? (Münzen: {user_data["coins"]})\n')
    print('1. Lernen')
    print('2. Spielen')
    print('3. Klasse ändern')
    print('4. Beenden')

    choice = input()

    if choice == '1':
        learning(user_data)
    elif choice == '2':
        games()
    elif choice == '3':
        main()  # Zurück zur Klassenauswahl
    elif choice == '4':
        save_data(user_data)
        quit()
    else:
        print('Ungültige Auswahl. Bitte versuche es erneut.')
        time.sleep(1)
        menu(user_data)

# Lernmodus basierend auf der Klasse
def learning(user_data):
    clear_console()
    klasse = user_data['klasse']
    print(f"Du lernst jetzt Aufgaben der {klasse}. Klasse\n")

    print('Löse 5 Aufgaben in jeder Kategorie: Addition, Subtraktion, Multiplikation, Division.')
    print('Du hast 5 Leben. Bei null verlierst du. Wenn du 5 richtige Antworten in einer Kategorie hast, bekommst du eine Münze!\n')
    lives = 5

    for _ in range(5):
        if lives == 0:
            print('Du hast verloren.')
            break
        lives, user_data['coins'] = math_problems(lives, user_data['coins'], klasse)
    
    print(f'Du hast {user_data["coins"]} Münzen gesammelt.')
    time.sleep(2)
    menu(user_data)

# Mathematikaufgaben generieren
def math_problems(lives, coins, klasse):
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)

    if klasse == 3:
        zahl_1 = random.randint(1, 20)
        zahl_2 = random.randint(1, 20)
    else:
        zahl_1 = random.randint(10, 100)
        zahl_2 = random.randint(1, 10)

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
        # Division soll immer ganzzahlig sein
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

# Spielmodul (Platzhalter)
def games():
    print("Spielmodul ist noch in Arbeit...")
    time.sleep(2)
    main()

# Konsole leeren je nach Betriebssystem
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()
