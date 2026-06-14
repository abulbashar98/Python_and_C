import random


def spinRow(symbols):
    return [random.choice(symbols) for _ in range(3)]

def printRow(row):
    print("Spinning...\n")
    print(" | ".join(row))
    

def getPayout(row, bet):
    if row[0] == row[1] == row[2]:
        print("You won!!!")
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    else:
        print("You lost this round!")
        return 0   
        
def play_again():

    while True: 
        choice = input("Do you want to play again?(Y/N)\n").upper()

        if choice in ("Y","N"):
            return choice
        else:
            print("Enter (Y/N)")
    
            

def main():
    balance = 100
    symbols = ['🍒','🍉','🔔','⭐']
    while True:
        print("***********************************")
        print("Welcome to python slot machine game")
        for symbol in symbols:
            print(symbol,end="         ") 
        print()    
        print("***********************************")
        print()

        print(f"Your current balance is: ${balance}")

        while True:
            try:
                bet = int(input("Enter your bet amount: "))
                
                if bet <= 0:
                    print("Invalid bet amount")
                    continue

                elif bet > balance:
                    print("Insufficient funds")
                    continue

                else:
                    balance -= bet
                    break

            except ValueError:
                print("Input a valid number")    
        
        row = spinRow(symbols)
        printRow(row)
        balance += getPayout(row, bet);
        print(f"Your current balance is: {balance}")
        
        if balance > 0:
            choice = play_again()

            if choice == 'Y':
                continue
            else:
                break 


if __name__ == '__main__':
    main()