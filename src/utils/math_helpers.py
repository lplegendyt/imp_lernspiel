import random
import time
from utils.ui_helpers import clear_console

def choose_difficulty(user_data):
    clear_console()
    print("Wähle den Schwierigkeitsgrad:\n")
    print("1. Leicht")
    print("2. Normal")
    print("3. Schwer")

    choice = input()
    if choice == "1":
        learning(user_data, "leicht")
    elif choice == "2":
        learning(user_data, "normal")
    elif choice == "3":
        learning(user_data, "schwer")
    else:
        print("Ungültige Auswahl. Bitte versuche es erneut.")
        choose_difficulty(user_data)

def learning(user_data, difficulty):
    clear_console()
    klasse = user_data['klasse']
    print(f"Du lernst jetzt Aufgaben der {klasse}. Klasse mit dem Schwierigkeitsgrad: {difficulty}\n")

    print("Löse 5 Aufgaben in jeder Kategorie: Addition, Subtraktion, Multiplikation, Division.")
    print("Du hast 5 Leben. Bei null verlierst du. Für jede richtige Antwort bekommst du eine Münze!\n")
    lives = 5

    for _ in range(5):
        if lives == 0:
            print("Du hast verloren.")
            break
        lives, user_data['coins'] = math_problems(lives, user_data['coins'], klasse, difficulty)
    
    print(f"Du hast {user_data['coins']} Münzen gesammelt.")
    time.sleep(2)

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
    elif operation == '-':
        result = zahl_1 - zahl_2
    elif operation == '*':
        result = zahl_1 * zahl_2
    elif operation == '/':
        zahl_1 = zahl_1 * zahl_2
        result = zahl_1 // zahl_2

    print(f"{zahl_1} {operation} {zahl_2} = ?")
    answer = input()

    if answer.isdigit() and int(answer) == result:
        print("Richtig!")
        coins += 1
    else:
        print(f"Falsch! Die richtige Antwort war {result}.")
        lives -= 1
    
    return lives, coins
