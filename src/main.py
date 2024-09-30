import os
import time
import random

# Hauptfunktion
def main():

    clear_console()

    print('Willkommen!')
    print()
    print('In welcher Klasse bist du?')
    print()
    print('1. Klasse 3')
    print('2. Klasse 4')

    choice = input()

    if choice == '1':
        print('Du bist in der 3. Klasse (ja/nein)?')
        
        confirmation = input()

        if confirmation.lower() in ['j', 'ja']:
            klasse = 3
            print('Super, fangen wir an!')
            clear_console()
            menu(klasse)
        else:
            main()
    elif choice == '2':
        print('Du bist in der 4. Klasse (ja/nein)?')
        
        confirmation = input()

        if confirmation.lower() in ['j', 'ja']:
            klasse = 4
            print('Super, fangen wir an!')
            clear_console()
            menu(klasse)
        else:
            main()

def menu(klasse):

    print('Was möchtest du tun?')
    print()
    print('1. Lernen')
    print('2. Spielen')
    print('3. Klasse ändern')
    print('4. Beenden')
    
    choice = input()

    if choice == '1':
        learning(klasse)
    elif choice == '2':
        games(coins)
    elif choice == '3':
        change_class(klasse)
    elif choice == '4':
        save(Klasse, coins)
        quit()

def learning(klasse):

    print(f"Du lernst jetzt Aufgaben der {klasse}. Klasse")
    print()

    if klasse == '3':
        print('Hier musst du gleich fünf aufgaben von jeder art lösen also Plus minus mal geteilt')
        print('Du hast 5 leben bei null verlierst du alles. wenn du alle 5 aufgaben eines themas richtig hast bekommst du eine münze!')

        lives = 5

        for i in range(5):
            zahl_1 = random.randint(1, 500)
            zahl_2 = random.randint(1,500)
            result = zahl_1 + zahl_2
            print





# Konsole leeren je nach Betriebssystem
def clear_console():

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()
