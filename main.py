from models. data import users
from utils.crud import show_users, add_new_user, search_user, remove_user, update_user





if __name__ == '__main__':
    print("Witaj uzytkowniku")
    while True:
        print("Menu")
        print("0. Zakoncz program")
        print("1. Wyswietl co u zanjomych")
        print("2. Dodaj uzytkownika")
        print("3. Znajdz uzytkownika")
        print("4. Usun uzytownika")
        print("5. Dodaj uzytkownika ")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == "0":
            print("Program konczy prace")
            break
        if menu_option == "1":
            show_users(users)
        if menu_option == "2":
            add_new_user(users)
        if menu_option == "3":
            search_user(users)
        if menu_option == "4":
            remove_user(users)
        if menu_option == "5":
            remove_user(users)


            def update_user(users) -> None:
                Kogo_szukasz = input("Kogo szukasz: ")
                for user in users:
                    if user['name'] == Kogo_szukasz:
                        user["name"] = input("podaj nowe imie:  ")
                        user["surename"] = input("podaj nowe nazwisko: ")
                        user["posts"] = input("podaj liczbe postow: ")