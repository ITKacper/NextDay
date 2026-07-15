import math
import random
import time


def Deposit(balance, deposited):
    return balance + deposited


def Withdraw(balance, deposited):
    return balance - deposited


def Place(balance):
    bet = int(input("How much money do you want to place?"))
    while bet < 0 or bet > balance:
        print("Invalid choice")
        bet = int(input("How much money do you want to place?"))
    print("spinning")
    diference = (balance + bet) - balance
    return diference


def inputval(inp):
    while True:
        if inp == "Y":
            return
        elif inp == "N":
            return True
        else:
            print("Invalid choice")
            return False


def Quit():
    print("Thank you for playing")


def main():
    slots = {1: "🍐", 2: "🍎", 3: "🍌", 4: "🍇", 5: "🍉", 6: "🫐", 7: "🍑", 8: "🍒"}
    balance = 0
    chosen = []
    print("***************")
    print("Welcome to Python slots")
    print("symbols:", end=' ')
    for symbol in slots.values():
        print(symbol, end=' ')
    print()
    while True:
        print("***************")
        print(f"Current balance: {balance}")
        print("1. Deposit to balance")
        print("2. Withdraw from balance")
        print("3. Place bet")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice > 4 or choice < 1:
            print("Invalid choice")
        elif choice == 1:
            new = int(input("How much money do you want to deposit?"))
            if new < 0:
                print("Invalid choice")
            else:
                balance = Deposit(balance, new)
        elif choice == 2:
            new = int(input("How much money do you want to withdraw?"))
            if new > balance or new < 0:
                print("Invalid choice")
            elif new <= balance:
                balance = Withdraw(balance, new)
        elif choice == 3:
            plays = True
            while plays == True:
                diference = Place(balance)
                print("Symbols: ")
                for i in range(0, 3):
                    chosen.append(slots.get(random.randint(1, 8)))
                    print(chosen[i], end=' ')
                print()
                if chosen[0] == chosen[1] and chosen[1] == chosen[2]:
                    print("You win!")
                    balance = balance + diference * 10
                    again = input("Try again?(Y/N) ")
                    if again.upper() == "N":
                        plays = False
                    while again.upper().isalpha() == False or again.upper() != "Y" and again.upper() != "N":
                        again = input("Try again?(Y/N) ")


                else:
                    print("You lose!")
                    balance = balance - diference
                    again = input("Try again?(Y/N) ")
                    if again.upper() == "N":
                        plays = False
                    while again.upper().isalpha() == False or again.upper() != "Y" and again.upper() != "N":
                        again = input("Try again?(Y/N) ")

                chosen.clear()
        elif choice == 4:
            print("Thank you for playing")
            break


main()
