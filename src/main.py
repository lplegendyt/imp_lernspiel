import os
import time

# Hauptfunktion
def main():

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
        

def learning(klasse):
    print(f"Du bist in der {klasse}. Klasse")

# Konsole leeren je nach Betriebssystem
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()
