

def showBalance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    while True:
        try:
            amount = float(input("Enter amount to be deposited: "))

            if amount < 0:
                print("Invalid amount")
                continue
            else:
                break 
            
        except ValueError:
            print("Deposit a valid number")
    
    return amount


def withdraw(balance):
    while True:
        try:
            amount = float(input("Enter amount to be withdrawn: "))

            if amount > balance:
                print("Insufficient funds")
                continue

            elif amount <= 0:
                print("Invalid input")
                continue

            else:
                break       

        except ValueError:
            print("Deposit a valid number")

    return balance - amount
    




def main():
    
    balance = 0
    is_running = True

    print("**********************************")
    print("Welcome to python banking program")
    print("**********************************")
    print()

    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    
    while is_running:
        try:
            choice  = int(input("Enter a choice(1-4): "))
            if choice < 1 or choice > 4:
                print("Invalid choice")
                continue

            else:
                match(choice):
                    case 1:
                        showBalance(balance)
                    case 2:
                        balance += deposit()
                    case 3:
                        balance = withdraw(balance)
                    case 4:
                        is_running = False     

        except ValueError:
            print("Choice can not be a text")

    
                   


        

if __name__ == '__main__':
    main()