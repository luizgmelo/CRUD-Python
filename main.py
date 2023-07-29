from crud import *


def menu():
    print("="*20)
    print("""    SISTEMA CRUD
    [1] - CREATE
    [2] - READ
    [3] - UPDATE
    [4] - DELETE
    [5] - QUIT """)
    print("="*20)


def main():
    while True:
        menu()
        choice = str(input("Type menu option: "))

        if choice not in '12345':
            print("\nInvalid Option. See Menu\n")
            continue
        
        if choice == '1':
            create()
        elif choice == '2':
            read()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        elif choice == '5':
            break


main()
