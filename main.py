from models. data import users
from utils.crud import show_users





if __name__ == '__main__':
    print("Witaj uzytkowniku")
    while True:
        print("Menu")
        print("1. Wyswietl co u zanjomych")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == "0":
            print("Program konczy prace")
            break
        if menu_option == "1":
            show_users(users)
