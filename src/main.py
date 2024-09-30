import os
import random
import time

# Hauptfunktion
def main():
    clear_console()

    print('Willkommen!')
    print('\nIn welcher Klasse bist du?\n')
    print('1. Klasse 3')
    print('2. Klasse 4')

    choice = input()

    if choice == '1':
        confirm_class(3)
    elif choice == '2':
        confirm_class(4)
    else:
        print('Ungültige Auswahl. Bitte versuche es erneut.')
        time.sleep(1)
        main()

# Klasse bestätigen und Menü starten
def confirm_class(klasse):
    print(f'Du bist in der {klasse}. Klasse (ja/nein)?')
    confirmation = input().lower()

    if confirmation in ['j', 'ja']:
        print('Super, fangen wir an!')
        clear_console()
        menu(klasse)
    else:
        main()

# Menü anzeigen
def menu(klasse):
    print('Was möchtest du tun?\n')
    print('1. Lernen')
    print('2. Spielen')
    print('3. Klasse ändern')
    print('4. Beenden')

    choice = input()

    if choice == '1':
        learning(klasse)
    elif choice == '2':
        games()
    elif choice == '3':
        main()  # Zurück zur Klassenauswahl
    elif choice == '4':
        save_data(klasse)
        quit()
    else:
        print('Ungültige Auswahl. Bitte versuche es erneut.')
        time.sleep(1)
        menu(klasse)

# Lernmodus basierend auf der Klasse
def learning(klasse):
    clear_console()
    print(f"Du lernst jetzt Aufgaben der {klasse}. Klasse\n")

    if klasse == 3:
        print('Löse 5 Aufgaben in jeder Kategorie: Addition, Subtraktion, Multiplikation, Division.')
        print('Du hast 5 Leben. Bei null verlierst du. Wenn du 5 richtige Antworten in einer Kategorie hast, bekommst du eine Münze!\n')
        lives = 5
        coins = 0

        for _ in range(5):
            if lives == 0:
                print('Du hast verloren.')
                break
            lives, coins = math_problems(lives, coins)
        
        print(f'Du hast {coins} Münzen gesammelt.')
        time.sleep(2)
        menu(klasse)

# Mathematikaufgaben generieren
def math_problems(lives, coins):
    zahl_1 = random.randint(1, 500)
    zahl_2 = random.randint(1, 500)
    result = zahl_1 + zahl_2  # Nur Addition für Beispiel

    print(f'{zahl_1} + {zahl_2} = ?')
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

# Daten speichern (Platzhalter)
def save_data(klasse):
    print(f"Speichern der Daten für Klasse {klasse}...")
    # Implementiere die Speicherfunktion hier
    time.sleep(1)

# Konsole leeren je nach Betriebssystem
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()
