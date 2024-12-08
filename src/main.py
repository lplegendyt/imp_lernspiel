from utils.data_handler import load_data, save_data
from utils.ui_helpers import clear_console
from utils.math_helpers import choose_difficulty, learning
from utils.games import games

def main():
    user_data = load_data()
    clear_console()

    print(f"Willkommen! Deine aktuelle Klasse ist {user_data['klasse']} und du hast {user_data['coins']} Münzen.")
    print("\nIn welcher Klasse bist du?\n")
    print("1. Klasse 3")
    print("2. Klasse 4")

    choice = input()

    if choice == "1":
        confirm_class(3, user_data)
    elif choice == "2":
        confirm_class(4, user_data)
    else:
        print("Ungültige Auswahl. Bitte versuche es erneut.")
        main()

def confirm_class(klasse, user_data):
    print(f"Du bist in der {klasse}. Klasse (ja/nein)?")
    confirmation = input().lower()

    if confirmation in ["j", "ja"]:
        user_data["klasse"] = klasse
        print("Super, fangen wir an!")
        clear_console()
        menu(user_data)
    else:
        main()

def menu(user_data):
    clear_console()
    print(f"Was möchtest du tun? (Münzen: {user_data['coins']})\n")
    print("1. Lernen")
    print("2. Spielen")
    print("3. Klasse ändern")
    print("4. Beenden")

    choice = input()

    if choice == "1":
        choose_difficulty(user_data)
    elif choice == "2":
        games(user_data)
    elif choice == "3":
        main()
    elif choice == "4":
        save_data(user_data)
        clear_console()
        quit()
    else:
        print("Ungültige Auswahl. Bitte versuche es erneut.")
        menu(user_data)

if __name__ == "__main__":
    main()
